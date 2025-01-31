from flask import Flask, jsonify
from flask_cors import CORS

# app instance
# CORS to enable front and back end communication
app = Flask(__name__)
CORS(app)

# /api/home
@app.route('/api/home', methods=['GET'])
def return_home():
    return jsonify({
        'message': "hello from the backend!"
    })

if __name__ == '__main__':
    app.run(debug=True, port=8079)
