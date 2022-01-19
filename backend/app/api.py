from flask import Blueprint

blueprint = Blueprint("api", __name__, url_prefix="/api")


@blueprint.route("/hello", methods=["GET"])
def serve_hello():
    return {}
