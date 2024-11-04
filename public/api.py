from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/api/catalogue', methods=['GET'])
def get_catalogue():
    with open('public/frontEndData.json', 'r') as file:
        catalogue = json.load(file)
    return jsonify(catalogue)

if __name__ == '__main__':
    app.run(port=5000)
