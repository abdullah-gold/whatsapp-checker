from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route("/check", methods=["POST"])
def check():
    numbers = request.json.get("numbers", [])

    reg = []
    not_reg = []

    for n in numbers:
        if random.choice([True, False]):
            reg.append("+" + n)
        else:
            not_reg.append("+" + n)

    return jsonify({
        "registered": reg,
        "not_registered": not_reg
    })

app.run(host="0.0.0.0", port=10000)
