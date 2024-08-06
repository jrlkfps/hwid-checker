from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para registrar HWID
@app.route('/api/register_hwid', methods=['POST'])
def register_hwid():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    cpu_serial = data.get('cpu_serial')
    motherboard_serial = data.get('motherboard_serial')
    disk_serial = data.get('disk_serial')
    
    # Lógica para armazenar HWID no banco de dados (pode ser ajustada conforme necessário)
    # Exemplo simplificado: apenas printar os dados recebidos
    print(f'Username: {username}')
    print(f'Password: {password}')
    print(f'CPU Serial: {cpu_serial}')
    print(f'Motherboard Serial: {motherboard_serial}')
    print(f'Disk Serial: {disk_serial}')
    
    # Resposta de sucesso
    return jsonify({'message': 'HWID registrado com sucesso!'}), 200

# Adicionando suporte para configurar o servidor corretamente no Heroku
if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
