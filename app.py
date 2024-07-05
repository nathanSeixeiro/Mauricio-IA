from flask import Flask, jsonify, make_response, request
import ia
from contentsafety import analyze_text
api = Flask(__name__)


@api.route('/api/procurar', methods=['POST'])
def search():  
    data = request.get_json()
    
    if analyze_text(data) == False:
        response = ia.retrieve_and_generate(data)
        return make_response(jsonify({'ChatBot': response}), 200)
    else:
        response = ia.retrieve_and_generate(data)
        return make_response(jsonify({'ChatBot': "Sua mensagem contem conteúdo violento. Por favor mude sua mensagem."}), 400)

if __name__ == '__main__':
    api.run(debug=True)