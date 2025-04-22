import threading
import time
import establishing_connection
from prompt_toolkit import prompt
from prompt_toolkit.patch_stdout import patch_stdout


# =========================[Establishing the Connection]=========================

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

# ================================[Start Masseging]==============================

def receving_massege(recever_socket):
    conn, addr = recever_socket.accept()
    with patch_stdout():
        print(f"conn: {conn}\naddr: {addr}")

    while True:
        data = conn.recv(1024)
        if data:
            with patch_stdout():
                print(f"<<-| {data.decode("utf-8")}")
        elif not data:
            break

    conn.close()
    recever_socket.close()
    with patch_stdout():
        print("Your Partiner are closed.")


def sending_massege(sender_socket):
    while True:
        user_input = prompt(">->> ")

        if not user_input:  
            break
        elif user_input:
            sender_socket.send(user_input.encode('utf-8'))
        else:
            print("<<Something went wrong..>>")
    sender_socket.close()
    print("You have closed.")


threading.Thread(target=receving_massege, args=(recever_socket,)).start()
sending_massege(sender_socket)
