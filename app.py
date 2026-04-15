from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/save', methods=['POST'])
def save():
    data = request.json

    name = data.get('name')
    surname = data.get('surname')
    nickname = data.get('nickname')

    with open('users.txt', 'a', encoding='utf-8') as f:
        f.write(f"{name} | {surname} | {nickname}\n")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)