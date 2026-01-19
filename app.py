from flask import Flask, request, jsonify, send_file
import tempfile
from qreader import QReader
import cv2
import pathlib
import os

app = Flask(__name__)

@app.route("/qr-reader", methods=["POST"])
def read_qr():
    ALLOWED_MIME_TYPES = {"image/png", "image/jpeg", "image/webp", "image/gif"}
    
    if "file" not in request.files:
        return jsonify({"error": "Envie um arquivo de imagem com o campo 'file'"}), 400

    file = request.files["file"]
    filename = file.filename.lower()
    ext = pathlib.Path(filename).suffix
    content_type = file.mimetype

    if content_type not in ALLOWED_MIME_TYPES:
        return jsonify({
            "error": "Arquivo inválido. Envie uma imagem válida."
        }), 400

    with tempfile.TemporaryDirectory() as tmpdir:
        input_path = os.path.join(tmpdir, "input" + ext)
        file.save(input_path)
        image = cv2.cvtColor(cv2.imread(input_path), cv2.COLOR_BGR2RGB)
    
    qreader = QReader()
    decoded_text = qreader.detect_and_decode(image=image)
    
    if not decoded_text:
        return jsonify({
            "success": False,
            "error": "Nenhum QR Code encontrado"
        }), 200

    return jsonify({
        "success": True,
        "data": decoded_text
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)