from flask import Blueprint


embedding = Blueprint(
    "embedding", __name__)


def page():
    return "Hello, embedding!"


embedding.add_url_rule(
    "/embedding/page", view_func=page)


def get_blueprints():
    return [embedding]
