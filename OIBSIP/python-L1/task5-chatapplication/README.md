# Chat Application

## Objective
Build a real-time messaging application in Python using sockets and threading.

## Technologies Used
- Python
- Socket Programming
- Threading

## Features
- Server accepts client connections.
- Client connects to the server.
- Real-time, bidirectional messaging.
- Messages include timestamps.
- Multiple clients can communicate.
- Graceful client disconnection.
- Runs on localhost.

## How to Run

### 1. Start the Server
Open PowerShell in the project folder and run:

python server.py

### 2. Start Client 1
Open another PowerShell window and run:

python client.py

### 3. Start Client 2
Open another PowerShell window and run:

python client.py

Now messages can be exchanged between the two clients.

## Project Files
- `server.py` – Server-side program
- `client.py` – Client-side program
- `README.md` – Project documentation
- `screenshots/` – Project output screenshots

## Security Transparency
This beginner version uses local socket communication on localhost. Messages are not encrypted end-to-end.
