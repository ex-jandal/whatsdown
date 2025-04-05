from prompt_toolkit import prompt
# from prompt_toolkit.patch_stdout import patch_stdout

def sending_massege(sender_socket, is_true: bool):
    while True:
        user_input = prompt("->> : ")
        print("-> ", user_input)


        if not user_input:  
            break
        elif is_true:
            sender_socket.send(user_input.encode('utf-8'))
        else:
            print("<<Something went wrong..>>")
    sender_socket.close()
    print("You have closed.")

