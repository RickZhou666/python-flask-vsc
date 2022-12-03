import os
import redis
import secrets
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from dotenv import load_dotenv
# from flask_swagger_ui import get_swaggerui_blueprint
from rq import Queue

from db import db
from blocklist import BLOCKLIST
import models

from resources.item import blp as ItemBluePrint
from resources.store import blp as StoreBluePrint
from resources.tag import blp as TagBluePrint
from resources.user import blp as UserBluePrint


def create_app(db_url=None):
    app = Flask(__name__)
    load_dotenv()

    connection = redis.from_url(
        os.getenv("REDIS.URL")
    )

    app.queue = Queue("emails", connection=connection)
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui" # URL for exposing Swagger UI (without trailing '/')
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/" # Our API url (can of course be a local resource)

    # app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api/docs" # URL for exposing Swagger UI (without trailing '/')
    # app.config["OPENAPI_SWAGGER_UI_URL"] = "http://petstore.swagger.io/v2/swagger.json" # Our API url (can of course be a local resource)

    # app.config["OPENAPI_SWAGGER_UI_URL"] = "https://github.com/swagger-api/swagger-ui"
    # app.config["OPENAPI_SWAGGER_UI_URL"] = "https://github.com/swagger-api/swagger-ui/blob/master/dist"
    # app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist"
    # app.config["OPENAPI_SWAGGER_UI_URL"] = "http://infrasrv-uat-skynet-vip.us-central1.gcp.dev.paypalinc.com/"

    # define db uri
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    # migrate = Migrate(app, db, compare_type=True)
    migrate = Migrate(app, db)

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "jose"
    # app.config["JWT_SECRET_KEY"] = secrets.SystemRandom.getrandbits(128)
    jwt = JWTManager(app)

    # whenever we receive JWT request, this function runs
    # true - blocked
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST


    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return(
            jsonify(
                {
                    "description": "The token has been revoked.",
                    "error": "token_revoked"
                }
            )
        )

    @jwt.needs_fresh_token_loader
    def token_not_refresh_callback(jwt_header, jwt_payload):
        return(
            jsonify(
                {
                    "description": "The token is not fresh..",
                    "error": "fresh_token_required"
                }
            )
        )

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        # Look in the database and see whether the user is an admin
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    # jwt - decorator
    # expired_token_loader - decorator function
    # if token expired
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return(
            jsonify(
                {
                    "message": "The token has expired.", 
                    "error": "token_expired"
                }
            ),
            401
        )

    # if user try to change the token
    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return(
            jsonify(
                {
                    "message": "The token has expired.", 
                    "error": "invalid_token"
                }
            ),
            401,
        )

    #  if token was missing
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return(
            jsonify(
                {
                    "description": "Request does not contain an access token.", 
                    "error": "authorization_expired"}
            ),
            401
        )

    # way1:
    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    # way2:
    # with app.app_context():
    #     db.create_all()

    api.register_blueprint(ItemBluePrint)
    api.register_blueprint(StoreBluePrint)
    api.register_blueprint(TagBluePrint)
    api.register_blueprint(UserBluePrint)

    return app