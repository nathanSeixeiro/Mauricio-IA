from flask import Flask, jsonify, make_response, request
import app
api = Flask(__name__)


@api.route('/api/procurar', methods=['POST'])
def search():  
    data = request.get_json()
    
    response = app.retrieve_and_generate(data)
    return make_response(jsonify({'ChatBot': response}), 200)

if __name__ == '__main__':
    api.run(debug=True)