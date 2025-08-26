from flask import Flask
from flask import request, jsonify
from utils.normalizer import normalize_address

app = Flask(__name__)

@app.route('/normalize', methods=['POST'])
def normalize():
    data = request.get_json()
    address = data.get('address', '')
    normalized_address = normalize_address(address)
    return jsonify({'normalized_address': normalized_address})

if __name__ == '__main__':
    app.run(debug=True)