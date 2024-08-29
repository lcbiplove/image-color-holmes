from flask import render_template, jsonify
from app.main import bp
from flask import request
from app.main.detector import detect_colors
import tempfile
from app.main.aws import s3_client, BUCKET_NAME
import uuid

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

        with open(temp_file.name, "rb") as data:
            random_filename = str(uuid.uuid4()) + "." + file.filename.rsplit(".", 1)[1]
            s3_client.upload_fileobj(data, BUCKET_NAME, random_filename)

        return jsonify({"data": colors})
    return jsonify({"error": "Error processing file."})
