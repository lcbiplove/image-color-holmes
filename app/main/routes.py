from flask import render_template, jsonify
from app.main import bp
from flask import request
from app.main.detector import detect_colors
import tempfile

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("image", "")

    if file.filename == "":
        return jsonify({"error": "No selected file"})

    if file:
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        file.save(temp_file.name)

        colors = detect_colors(filename=temp_file.name)
        return jsonify({
            "data": colors
        })
    return jsonify({"error": "Error proecessing file."})
