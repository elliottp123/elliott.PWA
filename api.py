from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({"message": "Data retrieved successfully"})

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(port=5000)
