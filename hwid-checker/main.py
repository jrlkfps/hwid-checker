import os
import requests
import wmi

# Instanciar a interface WMI
c = wmi.WMI()

# Obter o serial da CPU
for cpu in c.Win32_Processor():
    cpu_serial = cpu.ProcessorId.strip()

# Obter o serial da placa-mãe
for board in c.Win32_BaseBoard():
    motherboard_serial = board.SerialNumber.strip()

# Obter o serial do disco
for disk in c.Win32_DiskDrive():
    disk_serial = disk.SerialNumber.strip()

# Pedir login e senha do usuário
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

# Preparar os dados para envio
hwid_data = {
    "username": username,
    "password": password,
    "cpu_serial": cpu_serial,
    "motherboard_serial": motherboard_serial,
    "disk_serial": disk_serial
}

# URL do servidor Flask (substitua pelo seu URL do Heroku)
url = "https://seu-app.herokuapp.com/api/register_hwid"

# Enviar dados para o servidor
response = requests.post(url, json=hwid_data)

# Verificar resposta do servidor
if response.status_code == 200:
    print("HWID registrado com sucesso.")
else:
    print(f"Erro ao registrar HWID: {response.json()}")
