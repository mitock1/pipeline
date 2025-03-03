from flask import Blueprint

# here you will accommodate your views/endpoints

bp = Blueprint("views", __name__, url_prefix="/v1")

bp.route("/hello_world", methods=("GET",))


def hello_word():
    return "hello world"
