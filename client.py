import socket

HEADER=64
PORT=5050
# PORT=14153 (this is the port number that was generated when using ngrok)
FORMAT='utf-8'
DISCONNECT_MESSAGE="!DISCONNECT"
SERVER=socket.gethostbyname(socket.gethostname())
# SERVER="0.tcp.in.ngrok.io"(this is the domain provided by ngrok)
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)  # Encode the message length to bytes
    send_length += b' ' * (HEADER - len(send_length))  # Pad the message length to fit the HEADER size
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("My name is Aravind")
send(DISCONNECT_MESSAGE)

