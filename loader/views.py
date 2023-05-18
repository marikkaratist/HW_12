from flask import Blueprint, render_template, request
import logging
from loader.utils import upload_photo
from exception import PictureWrongTypeError, DataLayerError
from main.utils import PostManager

loader_photo_blueprint = Blueprint("loader_photo_blueprint", __name__)
posts_manager = PostManager("posts.json")
logging.basicConfig(filename="basic.log", level=logging.INFO, encoding="utf-8")


@loader_photo_blueprint.route("/post")
def new_post_form_gage():
    return render_template("post_form.html")


@loader_photo_blueprint.route("/post", methods=['POST'])
def post_upload_page():
    picture = request.files.get("picture", None)
    content = request.values.get("content", None)
    if not picture or not content:
        logging.info("Файлы не загружены")
        return "Файлы не загружены"
    try:
        picture_path = upload_photo(picture)
    except PictureWrongTypeError:
        logging.info("Неверный тип файла")
        return "Неверный тип файла"
    except FileNotFoundError:
        logging.error("Ошибка при загрузке файла")
        return "Не удалось сохранить файл, путь не найден"

    picture_url = "/" + picture_path

    post_object = {"pic": picture_url, "content": content}
    try:
        posts_manager.add_post(post_object)
    except DataLayerError:
        return "Не удалось добавить пост, ошибка записи в список постов"
    return render_template("post_uploaded.html", picture_url=picture_url, content=content)
