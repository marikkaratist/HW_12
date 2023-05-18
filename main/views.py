from flask import Blueprint, render_template, request
from main.utils import PostManager
from exception import DataLayerError
import logging
post_photo_blueprint = Blueprint("post_photo_blueprint", __name__)
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf-8")


@post_photo_blueprint.route("/")
def post_photo_page():
    logging.info("Запрошена главная страничка")
    return render_template("index.html")


@post_photo_blueprint.route("/search")
def post_search_page():
    s = request.args.get("s", "")
    posts_manager = PostManager("posts.json")
    try:
        posts = posts_manager.get_posts_by_text(s)
        logging.info("Выполняется поиск")
        return render_template("post_list.html", posts=posts, s=s)

    except DataLayerError:
        return "Файл повреждён"
