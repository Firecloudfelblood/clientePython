import socket
import sys
HOST = '127.0.0.1'
# HOST = '199.99.99.29'
# PORT = 64716
PORT = 65432
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
def print_error(e, message):
    print(message, e)
    exit(1)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
        except socket.error as e:
            print_error(e, 'Error relacionado con la direcion IP del servidor')
        for i in range (1,  1000):
            try:
                s.sendall(ip_address.encode())
            except socket.error as e:
                print_error(e, 'Error enviando datos ')

            try:
                data = s.recv(1024).decode()
            except socket.error as e:
                print_error(e, 'Error recibiendo datos' )
            if not data:
                print("Paquete perdido ")
            print(i,' Received: ', repr(data))
except Exception as e:
    print(str(e))

print('Received', repr(data))