
from flask import Flask, request, jsonify
import json
import datetime

app = Flask(__name__)

@app.route("/remita-webhook", methods=["POST"])
def remita_webhook():
    data = request.get_json()
    timestamp = datetime.datetime.now().isoformat()
    with open("remita_callback_log.json", "a") as f:
        f.write(json.dumps({"timestamp": timestamp, "payload": data}) + "\n")
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    app.run()
