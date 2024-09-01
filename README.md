# Python Socket Programming

## Overview
This project demonstrates a simple implementation of socket programming in Python, allowing multiple clients to connect to a server simultaneously. It covers the essential concepts of networking, the client-server model, and message communication.

## Features
- **Multiple Client Connections**: Handle multiple clients using threading.
- **Message Protocols**: Implement protocols for sending and receiving messages between clients and the server.
- **Local and Global Hosting**: Host the server locally or access it globally over the internet with a public IP address.

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
