# Python Socket Programming

## Overview and features
This project demonstrates a simple implementation of socket programming in Python, allowing multiple clients to connect to a server simultaneously and send and receive messages.It also deals with hosting a server locally or globally. It covers the essential concepts of networking, the client-server model, and message communication.

## Code Breakdown

### `server.py`
- **Server Initialization**: The server binds to a local IP address and port, then listens for incoming connections.
- **Handling Clients**: Each connected client is handled by a separate thread, allowing multiple clients to connect at the same time.
- **Message Handling**: The server reads the message length first (header) and then reads the actual message.

### `client.py`
- **Client-Server Communication**: The client connects to the server and sends messages using the same protocol (message length followed by the actual message).
- **Disconnection**: A special message (`!DISCONNECT`) is sent to terminate the connection.


### Using Ngrok for Global Access

In addition to running the client and server locally, I've integrated **Ngrok** into this project(commented out) to allow global access to the server.With Ngrok, I can create a secure tunnel to the local server, generating a public URL that clients can use to connect to the server, even if they are on different networks.Ngrok provides a public domain like tcp://0.tcp.ngrok.io:14153, which forwards traffic directly to my local server running on port 5050. This allows clients from any network to connect to my server as if it were hosted online.

Below is a display of the output and the working 

![Screenshot 2024-09-01 164213](https://github.com/user-attachments/assets/afda458b-c977-4066-a9f4-1cb8c80e32db)

![Screenshot 2024-09-01 164350](https://github.com/user-attachments/assets/385e6326-90bc-47d3-8164-9bd63ff13c96)

<img width="407" alt="Screenshot 2024-09-01 164455" src="https://github.com/user-attachments/assets/32aaecb7-fcc9-446a-b40f-2a89641774cc">


