from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Allowed extensions for file uploads
ALLOWED_EXTENSIONS = {"json"}

def allowed_file(filename):
    """Check if uploaded file has a valid extension"""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "followers" not in request.files or "following" not in request.files:
        return jsonify({"error": "Both followers and following files are required"}), 400

    followers_file = request.files["followers"]
    following_file = request.files["following"]

    if followers_file.filename == "" or following_file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if allowed_file(followers_file.filename) and allowed_file(following_file.filename):
        followers_filename = secure_filename(followers_file.filename)
        following_filename = secure_filename(following_file.filename)

        followers_path = os.path.join(app.config["UPLOAD_FOLDER"], followers_filename)
        following_path = os.path.join(app.config["UPLOAD_FOLDER"], following_filename)

        followers_file.save(followers_path)
        following_file.save(following_path)

        return jsonify({"message": "Files uploaded successfully", 
                        "followers_file": followers_filename, 
                        "following_file": following_filename}), 200
    else:
        return jsonify({"error": "Invalid file type. Only JSON files are allowed."}), 400

if __name__ == "__main__":
    app.run(debug=True)
