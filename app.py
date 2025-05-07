
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LIBRETRANSLATE_URL = "https://libretranslate.de/translate"  # Free instance

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    if not data or "q" not in data or "source" not in data or "target" not in data:
        return jsonify({"error": "Missing parameters"}), 400

    try:
        response = requests.post(LIBRETRANSLATE_URL, json={
            "q": data["q"],
            "source": data["source"],
            "target": data["target"],
            "format": "text"
        })

        return jsonify(response.json())

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)