import platform
import psutil
import requests
import socket

# Replace with your Discord webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1158098275375796405/KzaB30FBeSoBWzpTpOP8HrPPqvJejVe8ZHkTEV72k4cyH2iuz51kPiyM4vZruoxSfuHu'

def get_system_info():
    info = {
        "Hostname": socket.gethostname(),
        "OS": f"{platform.system()} {platform.release()}",
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Logical CPUs": psutil.cpu_count(logical=True),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB",
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Uptime": f"{round(psutil.boot_time() / 3600 / 24, 2)} days (since epoch)"
    }
    return info

def format_info(info):
    return '\n'.join([f"**{key}**: {value}" for key, value in info.items()])

def send_to_discord(content):
    data = {
        "content": f"📊 **System Information** 📊\n{content}"
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("✅ Message sent successfully.")
    else:
        print(f"❌ Failed to send message: {response.status_code}\n{response.text}")

if __name__ == '__main__':
    system_info = get_system_info()
    formatted_info = format_info(system_info)
    send_to_discord(formatted_info)
