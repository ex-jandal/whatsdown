import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    my_socket.bind(('', 5000))
    my_socket.listen()
    conn, addr = my_socket.accept()
    recevid_massege = conn.recv(1024).decode('utf-8')
    print(str(recevid_massege))
    my_socket.close()

