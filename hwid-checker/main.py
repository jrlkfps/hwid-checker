import os
import requests
import wmi

# Inicializa o WMI
c = wmi.WMI()

# Obtém o HWID da CPU
for cpu in c.Win32_Processor():
    cpu_id = cpu.ProcessorId.strip()

# Obtém o HWID da placa-mãe
for board in c.Win32_BaseBoard():
    motherboard_id = board.SerialNumber.strip()

# Obtém o HWID do HD principal (C:)
for disk in c.Win32_DiskDrive():
    if 'PHYSICALDRIVE0' in disk.DeviceID:
        hd_id = disk.SerialNumber.strip()

# Exibe os IDs coletados
print(f"CPU Serial: {cpu_id}")
print(f"Motherboard Serial: {motherboard_id}")
print(f"Disk Serial: {hd_id}")

# Combina os IDs em um único HWID
hwid = f"{cpu_id}-{motherboard_id}-{hd_id}"

# Solicita o login do usuário
username = input("Digite seu nome de usuário: ")
password = input("Digite sua senha: ")

# Dados para enviar ao servidor
hwid_data = {
    "username": username,
    "password": password,
    "cpu_serial": cpu_id,
    "motherboard_serial": motherboard_id,
    "disk_serial": hd_id
}

# URL do servidor Flask (substitua pelo seu URL do Heroku)
url = "https://hwid-checker-f8d4951224a8.herokuapp.com/api/register_hwid"

# Envia o HWID e os dados do usuário para o servidor
response = requests.post(url, json=hwid_data)

# Exibe a resposta do servidor
if response.status_code == 200:
    print(response.json())
else:
    print(f"Erro: {response.status_code} - {response.text}")

# Salva o HWID em um arquivo (opcional)
with open("hwid.txt", "w") as file:
    file.write(f"CPU Serial: {cpu_id}\n")
    file.write(f"Motherboard Serial: {motherboard_id}\n")
    file.write(f"Disk Serial: {hd_id}\n")
    file.write(f"HWID: {hwid}\n")
