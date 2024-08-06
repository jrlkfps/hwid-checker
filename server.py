from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemplo de usuários registrados
usuarios_registrados = {
    "usuario1": "senha1",
    "usuario2": "senha2"
}

@app.route('/api/register_hwid', methods=['POST'])
def register_hwid():
    data = request.json
    cpu_serial = data.get('cpu_serial')
    motherboard_serial = data.get('motherboard_serial')
    disk_serial = data.get('disk_serial')
    username = data.get('username')
    password = data.get('password')

    if username not in usuarios_registrados or usuarios_registrados[username] != password:
        return jsonify({'message': 'Credenciais inválidas!'}), 401

    # Salvar os dados em um arquivo
    with open('hwid_records.txt', 'a') as file:
        file.write(f"Username: {username}\n")
        file.write(f"CPU Serial: {cpu_serial}\n")
        file.write(f"Motherboard Serial: {motherboard_serial}\n")
        file.write(f"Disk Serial: {disk_serial}\n")
        file.write("\n")

    # Enviar comando para liberar o acesso (implementar conforme necessidade)
    # Aqui, você poderia adicionar a lógica para notificar o aplicativo sobre a liberação do HWID.

    return jsonify({'message': 'HWID registrado com sucesso!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
