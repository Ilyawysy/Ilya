import socket
PORT = 9090
 
sock = socket.socket()
sock.bind(('', PORT))
sock.listen()
 
while True:
    print("Слушаем порт", PORT)
    conn, addr = sock.accept()
    print(addr)
    
    request = conn.recv(1024).decode()
    print(request)
    
    response = process(request)
    conn.send(response.encode())
 
sock.close()