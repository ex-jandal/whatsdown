import socket

distantion_ip = input("Enter the destrantion IP: ")
send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:
    send_socket.connect((distantion_ip, 5000))
    massege = input("$ ")
    send_socket.send(massege.encode('utf-8'))
    print(type(massege))
    # send_socket.close()
