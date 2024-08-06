import subprocess
import requests

# Obtém o HWID da CPU
cpu_serial = subprocess.check_output("wmic cpu get processorid", shell=True).decode().split("\n")[1].strip()

# Obtém o HWID da placa-mãe
motherboard_serial = subprocess.check_output("wmic baseboard get serialnumber", shell=True).decode().split("\n")[1].strip()

# Obtém o HWID do HD principal (C:)
disk_serial = subprocess.check_output("wmic diskdrive where \"DeviceID='\\\\.\\PHYSICALDRIVE0'\" get serialnumber", shell=True).decode().split("\n")[1].strip()

# Solicita login e senha ao usuário
username = input("Digite seu login: ")
password = input("Digite sua senha: ")

# Dados a serem enviados para o servidor
hwid_data = {
    'cpu_serial': cpu_serial,
    'motherboard_serial': motherboard_serial,
    'disk_serial': disk_serial,
    'username': username,
    'password': password
}

# URL do servidor Flask (atualize com a URL do seu servidor)
url = 'https://seu-app-hwid-checker.herokuapp.com/api/register_hwid'

# Envia os dados para o servidor
response = requests.post(url, json=hwid_data)
print(response.json())
