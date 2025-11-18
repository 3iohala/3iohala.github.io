from flask import Flask, render_template, request, jsonify
from logic import process_command

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/command")
def command():
    cmd = request.json.get("cmd", "")
    result = process_command(cmd)

    # Jei grįžo dict — PW request arba meta
    if isinstance(result, dict):
        return jsonify(result)

    # Jei grįžo string — normalus tekstas
    return jsonify({
        "type": "text",
        "text": result
    })

if __name__ == "__main__":
    app.run(debug=True)
