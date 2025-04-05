import socket

def get_ip() -> str:
    return input("Enter your partener IP: ")

def get_port():
    while True:
        frist_port = input("Enter your partener PORT (choose between 49152 and 65535): ")
        if frist_port.isdigit() and 49152 <= int(frist_port) <= 65535:
            break
        else:
            print("Enter a VAILD PORT.")
            continue
    return int(frist_port)

def create_sending_socket(destination_ip: str, PORT: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((destination_ip, PORT))
    return s

def create_receving_socket(PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(1)  
    return s

