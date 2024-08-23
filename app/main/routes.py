from flask import render_template
from app.main import bp
import os
from flask import request

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/upload", methods=["POST"])
def upload():
    x = request.files.get("image", "")
    return {"data": x.filename}
