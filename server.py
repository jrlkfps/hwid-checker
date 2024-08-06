from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor Flask está rodando!"

@app.route('/api/register_hwid', methods=['POST'])
def register_hwid():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Verificar usuário e senha
    if not valid_credentials(username, password):
        return jsonify({'status': 'error', 'message': 'Invalid credentials'}), 401

    cpu_id = data.get('cpu_id')
    motherboard_id = data.get('motherboard_id')
    hd_id = data.get('hd_id')

    # Aqui você processa os dados do HWID (salvar em um banco de dados, por exemplo)
    # Esta parte do código depende da sua implementação específica
    # Por exemplo:
    # save_hwid_to_database(username, cpu_id, motherboard_id, hd_id)
    
    return jsonify({'status': 'success', 'message': 'HWID registrado com sucesso!'})

def valid_credentials(username, password):
    # Função de verificação de credenciais (substitua pela lógica real)
    # Aqui você deve validar as credenciais do usuário, possivelmente verificando um banco de dados
    # Exemplo simples:
    return username == 'usuario' and password == 'senha'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
