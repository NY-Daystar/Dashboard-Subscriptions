"""main module"""

from flask import Flask, render_template, request, url_for

from core import (
    APPLICATION,
    PROJECT_LINK,
    VERSION,
)

# from db.database import init_db, db
# from db.models import Item

app = Flask(__name__)
# init_db(app)

# TODO: temporaire avant la BDD
items = [
    {
        "name": "Abonnement mensuel",
        "price": 19.99,
        "provider": "Fortuneo",
        "frequency": "1 mois",
    },
    {
        "name": "Abonnement annuel",
        "price": 199.99,
        "provider": "Paypal",
        "frequency": "12 mois",
    },
]


@app.route("/")
def index() -> None:
    """Main page"""
    # items = Item.query.all()
    return render_template(
        "index.html",
        items=items,
        version=VERSION,
        application=APPLICATION,
    )


@app.route("/about")
def about() -> None:
    """About page"""
    return render_template(
        "about.html",
        application=APPLICATION,
        version=VERSION,
        link=PROJECT_LINK,
    )


@app.route("/health")
def healthcheck() -> dict:
    """Verify if application is running"""
    return {
        "status": "ok",
        "message": "Application running",
    }, 200


@app.route(
    "/add",
    methods=["POST"],
)
def add() -> None:
    # """api route to add subscription in database"""
    data = request.get_json()

    name = data.get("name")
    price = data.get("price")
    provider = data.get("provider")
    frequency = data.get("frequency")

    if not (name and price and frequency):
        return {
            "status": "error",
            "message": "Missing fields",
        }, 400

    new_item = {
        "name": name,
        "price": float(price),
        "provider": provider,
        "frequency": frequency,
    }
    items.append(new_item)

    return {
        "status": "ok",
        "item": new_item,
    }, 200


@app.route(
    "/delete/<int:num>",
    methods=["DELETE"],
)
def delete(
    num: int,
) -> None:
    """Api route to delete subscription in database"""
    if 0 <= num < len(items):
        removed = items.pop(num)
        return {
            "status": "ok",
            "removed": removed,
        }, 200

    return {
        "status": "error",
        "message": "Index out of range",
    }, 400


with app.test_request_context():
    # TODO: mettre un logger
    # print(url_for("index"))
    # print(url_for("about"))
    # print(url_for("healthcheck"))

    url_for("index")
    url_for("about")
    url_for("healthcheck")
