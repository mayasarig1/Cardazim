import threading
import time
import sys
import socket

lock = threading.Lock()

# handles data from each user seperately using "lock"
def handle_client(conn, addr):
    with lock:
        data_length_bytes = conn.recv(4)
        data_length = int.from_bytes(data_length_bytes, 'little')
        from_client = ''
        while True:
            data = conn.recv(data_length)
            if not data: break
            from_client += data.decode('utf8')
            print (f'From client: {from_client}')
        conn.close()


def run_server(ip, port):
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv.bind((ip, port))
    serv.listen(5)
    while True:
        conn, addr = serv.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
        t.join()

if __name__ == "__main__":
    ip = sys.argv[1]
    port = int(sys.argv[2])
    run_server(ip, port)