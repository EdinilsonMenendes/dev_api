from flask import Flask, jsonify, request
import json
app = Flask(__name__)

desenvolvedores = [
    {'nome':'Edinilson',
     'habilidades':['Python', 'Flask']},
    {'nome':'Menendes',
     'habilidades':['HTML', 'Javascripts']}
]
#Consulta , altera e deleta pelo ID#
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            resposta = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de id {} não existe!' .format(id)
            resposta = {'status': 'erro', 'mensagem':mensagem}
        return jsonify(resposta)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'excluido com sucesso'})

#Lista todos os desenvolvedores e também inclui um novo desenvolvedor#
@app.route('/dev/', methods=['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        desenvolvedores.append(dados)
        return jsonify({'status': 'sucesso', 'mensagem':'Cadastrado com sucesso'})
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run()
