from flask import render_template, jsonify
from app.main import bp
from flask import request
from app.main.detector import detect_colors

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/upload", methods=["POST"])
def upload():
    image = request.files.get("image", "")
    colors = detect_colors()
    objects = [
        {"id": 1, "name": "Object 1", "description": "This is object 1"},
        {"id": 2, "name": "Object 2", "description": "This is object 2"},
        {"id": 3, "name": "Object 3", "description": "This is object 3"}
    ]
    return jsonify(colors)
