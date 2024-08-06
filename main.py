import requests
import json
import subprocess

# Função para obter o número serial do hardware
def get_serial_number(command):
    try:
        result = subprocess.check_output(command, shell=True).decode().strip().split('\n')[1].strip()
        return result
    except Exception as e:
        print(f"Erro ao obter o serial: {e}")
        return None

# Obtendo os seriais
cpu_serial = get_serial_number("wmic cpu get processorid")
motherboard_serial = get_serial_number("wmic baseboard get serialnumber")
disk_serial = get_serial_number("wmic diskdrive get serialnumber")

# Coletando credenciais do usuário
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

# Dados para envio
hwid_data = {
    "username": username,
    "password": password,
    "cpu_serial": cpu_serial,
    "motherboard_serial": motherboard_serial,
    "disk_serial": disk_serial
}

# URL do servidor Flask no Heroku
url = "https://hwid-checker.onrender.com"

# Enviando solicitação POST para registrar HWID
response = requests.post(url, json=hwid_data)

# Verificando a resposta do servidor
if response.status_code == 200:
    print("HWID registrado com sucesso!")
else:
    print(f"Falha ao registrar HWID: {response.status_code} - {response.text}")
