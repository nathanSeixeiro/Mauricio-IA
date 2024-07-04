from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import ia
api = Flask(__name__)
CORS(api)

@api.route('/api/procurar', methods=['POST'])
def search():  
    data = request.get_json()
    
    response = ia.retrieve_and_generate(data)
    return make_response(jsonify({'ChatBot': response}), 200)

if __name__ == '__main__':
    api.run(debug=True)