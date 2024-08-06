import os
import subprocess
import requests

def get_hwid():
    # Obtém o HWID da CPU
    cpu_id = subprocess.check_output("wmic cpu get processorid").decode().split("\n")[1].strip()

    # Obtém o HWID da placa-mãe
    motherboard_id = subprocess.check_output("wmic baseboard get serialnumber").decode().split("\n")[1].strip()

    # Obtém o HWID do HD principal (C:)
    hd_id = subprocess.check_output("wmic diskdrive where \"DeviceID='\\\\.\\PHYSICALDRIVE0'\" get serialnumber").decode().split("\n")[1].strip()

    return cpu_id, motherboard_id, hd_id

cpu_id, motherboard_id, hd_id = get_hwid()

print(f"CPU Serial: {cpu_id}")
print(f"Motherboard Serial: {motherboard_id}")
print(f"Disk Serial: {hd_id}")

# Solicitar login e senha do usuário
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

hwid_data = {
    'cpu_id': cpu_id,
    'motherboard_id': motherboard_id,
    'hd_id': hd_id,
    'username': username,
    'password': password
}

# URL do servidor Flask no Heroku
url = "https://seu-app.herokuapp.com/api/register_hwid"

# Envia os dados para o servidor
response = requests.post(url, json=hwid_data)

# Verifica a resposta do servidor
if response.status_code == 200:
    print("HWID registrado com sucesso!")
else:
    print(f"Erro ao registrar HWID: {response.json()['message']}")
