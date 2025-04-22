import socket

def get_ip() -> str:
    return input("Enter your partener IP (should be IPv4): ")

def get_port():
    while True:
        port = input("Enter your partener PORT (choose between 49152 and 65535): ")
        if port.isdigit() and 49152 <= int(port) <= 65535:
            break
        else:
            print("Enter a VAILD PORT.")
            continue
    return int(port)

def create_sending_socket(dest_ip: str, dest_port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((dest_ip, dest_port))
    return s

def create_receving_socket(PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(1)  
    return s
