import socket
import sys

def send_data(ip, port, data):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ip, port))
    client.sendall(len(data).to_bytes(4, 'little'))
    client.send(data)
    client.close()

if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])
    data = sys.argv[3].encode("utf-8")
    send_data(ip, port, data)    
