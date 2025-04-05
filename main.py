import threading
import time
import establishing_connection
import receving_side
import sending_side
import sys


ask_user = ["Create chatroom.", "Join to chatroom."]
while True:
    print(f"do you want:")
    ask_user_index = 1
    for q in ask_user:
        print(f"\t{ask_user_index}. {q}")
        ask_user_index += 1

    is_admin = input("Enter a vaild option: ")
    if is_admin.isdigit() and 0 < int(is_admin) <= len(ask_user):
        is_admin = int(is_admin)
        break

dest_ip = establishing_connection.get_ip()
main_port = establishing_connection.get_port()
dest_port = main_port + 1 if is_admin == 1 else main_port
my_port = main_port if is_admin == 1 else main_port + 1

print(dest_port, my_port)

print("Whiting for a connection")
while True:
    try:
        recever_socket = establishing_connection.create_receving_socket(my_port)
        if recever_socket:
            break
    except OSError:
        time.sleep(1)
        continue

while True:
    try:
        sender_socket = establishing_connection.create_sending_socket(dest_ip, dest_port)
        if sender_socket:
            break
    except:
        time.sleep(1)
        continue

# Create a prompt session for a more dynamic input experience.
# session = PromptSession("-> ")
def income():
    print(f"receving from {dest_ip}:{dest_port}")
    receving_side.receving_massege(recever_socket, True)

def outcome():
    sending_side.sending_massege(sender_socket, True)

# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
threading.Thread(target=income).start()
threading.Thread(target=outcome).start()
# outcome()
