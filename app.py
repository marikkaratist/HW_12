from flask import Flask, send_from_directory
from main.views import post_photo_blueprint
from loader.views import loader_photo_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(post_photo_blueprint)
app.register_blueprint(loader_photo_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run()
