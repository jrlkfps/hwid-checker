import os
import requests

# Executa o script .bat para obter os HWIDs
os.system('get_hwid.bat')

# Lê o conteúdo do arquivo hwid.txt
hwid_data = {}
with open('hwid.txt', 'r') as file:
    for line in file:
        if "CPU ID:" in line:
            hwid_data['cpu_serial'] = line.split(":")[1].strip()
        elif "Motherboard ID:" in line:
            hwid_data['motherboard_serial'] = line.split(":")[1].strip()
        elif "Hard Drive ID:" in line:
            hwid_data['disk_serial'] = line.split(":")[1].strip()

# Exibe os seriais coletados
print(f"CPU Serial: {hwid_data['cpu_serial']}")
print(f"Motherboard Serial: {hwid_data['motherboard_serial']}")
print(f"Disk Serial: {hwid_data['disk_serial']}")

# URL do servidor
url = "http://localhost:5000/api/register_hwid"

# Envia os dados para o servidor
try:
    response = requests.post(url, json=hwid_data)
    if response.status_code == 200:
        print("HWID registrado com sucesso!")
    else:
        print(f"Falha ao registrar HWID: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao conectar ao servidor: {e}")