# Whatsdown

Whatsdown is a lightweight, LAN-based CLI messaging app built with Python. With Whatsdown, you can easily create or join chatrooms on your local network. It uses Python's standard libraries along with `prompt_toolkit` for a smooth, non-interruptive user interface.

---

## Features

- **Create or Join Chatrooms:** Choose to either host a chatroom or join an existing one.
- **LAN Networking:** Connect with a partner on the same local network.
- **Asynchronous Messaging:** Enjoy uninterrupted typing while incoming messages are handled seamlessly.
- **Clean CLI Interface:** Uses `prompt_toolkit` to ensure incoming messages do not interfere with your input.

---

## Requirements

Whatsdown is built with Python and requires the following libraries:

- `socket`
- `threading`
- `time`
- [`prompt_toolkit`](https://python-prompt-toolkit.readthedocs.io/) (includes `prompt` and `patch_stdout`)

### Installation via Package Managers

Depending on your operating system, you can install `prompt_toolkit` using your system's package manager:

- **Debian/Ubuntu:**
  ```bash
  sudo apt install python3-prompt_toolkit
  ```

- **Arch Linux (Pacman):**
  ```bash
  sudo pacman -S python-prompt_toolkit
  ```

- **Fedora:**
  ```bash
  sudo dnf install python3-prompt_toolkit
  ```

If your distribution doesn’t support these packages directly, you can always install via pip:

```bash
pip install prompt_toolkit
```

---

## How It Works

1. **Room Selection:**  
   When you start Whatsdown, you’ll be prompted with the following message to choose whether to create a chatroom or join one:
   ```plaintext
   do you want:
       1. Create chatroom.
       2. Join to chatroom.
   Enter a valid option:
   ```
   This organizes the port configuration for sending and receiving messages.

2. **Enter Partner IP:**  
   Next, you will be prompted to enter your partner’s IP address (must be within the same LAN):
   ```plaintext
   Enter your partner IP:
   ```

3. **Enter Partner Port:**  
   The app will then ask for a port number, with a suggestion to choose one between 49152 and 65535:
   ```plaintext
   Enter your partner PORT (choose between 49152 and 65535):
   ```

4. **Establish Connection:**  
   After entering the details, Whatsdown waits for a connection. Once your partner connects, the chat session starts!

---

## Usage

Simply run the Whatsdown Python script. The app will guide you through creating or joining a chatroom with clear prompts in your terminal.

```bash
python main.py
```

---

## Troubleshooting

- **Incoming Messages Interrupting Your Input:**  
  If you experience input interruptions when a message is received, ensure that you're using `prompt_toolkit`’s `patch_stdout()` within your receive thread. This helps to temporarily redirect stdout and prevent overlapping with your input prompt.

- **Connection Issues:**  
  - Verify that both parties are on the same LAN.
  - Ensure the IP address and port number are correct and not in use by another service.
  - Check firewall settings that might be blocking the connection.

- **Port Selection:**  
  If you experience issues related to port binding, remember to choose a port between 49152 and 65535, which are typically available for user applications.

---

## FAQ

**Q: Do I need to install any additional software besides Python?**  
A: No, Whatsdown only requires Python and the listed libraries. For `prompt_toolkit`, you can use your system's package manager or pip.

**Q: Can I use Whatsdown over the internet?**  
A: Whatsdown is designed for LAN usage. For internet usage, you would need to configure port forwarding and take additional security measures.

**Q: What happens if my partner disconnects?**  
A: The app will print a connection error. You can restart the app and try reconnecting.

---

Enjoy chatting on your LAN with Whatsdown! If you encounter any issues or have further questions, feel free to consult this README for guidance.
