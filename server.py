from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/register_hwid', methods=['POST'])
def register_hwid():
    data = request.json
    cpu_serial = data.get('cpu_serial')
    motherboard_serial = data.get('motherboard_serial')
    disk_serial = data.get('disk_serial')

    # Salvar os dados em um arquivo
    with open('hwid_records.txt', 'a') as file:
        file.write(f"CPU Serial: {cpu_serial}\n")
        file.write(f"Motherboard Serial: {motherboard_serial}\n")
        file.write(f"Disk Serial: {disk_serial}\n")
        file.write("\n")

    return jsonify({'message': 'HWID registrado com sucesso!'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)