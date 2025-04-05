from prompt_toolkit import prompt

def sending_massege(sender_socket, is_true: bool):
    while True:
        user_input = prompt(">->> ")

        if not user_input:  
            break
        elif is_true:
            sender_socket.send(user_input.encode('utf-8'))
        else:
            print("<<Something went wrong..>>")
    sender_socket.close()
    print("You have closed.")

