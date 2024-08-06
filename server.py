from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Dados de usuários e HWIDs para simulação
usuarios = {
    "usuario1": "senha1",
    "usuario2": "senha2",
}

hwids_permitidos = []

@app.route('/api/register_hwid', methods=['POST'])
def register_hwid():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    cpu_serial = data.get("cpu_serial")
    motherboard_serial = data.get("motherboard_serial")
    disk_serial = data.get("disk_serial")

    if username not in usuarios or usuarios[username] != password:
        return jsonify({"error": "Usuário ou senha inválidos"}), 401

    hwid = f"{cpu_serial}-{motherboard_serial}-{disk_serial}"
    
    if hwid not in hwids_permitidos:
        hwids_permitidos.append(hwid)
        return jsonify({"status": "HWID registrado com sucesso", "hwid": hwid}), 200
    else:
        return jsonify({"status": "HWID já registrado", "hwid": hwid}), 200

@app.route('/')
def index():
    return "Servidor Flask está funcionando."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
