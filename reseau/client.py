import network

IP = ""
PORT = 1111

while True:
    socket = network.newClientSocket()
    socket.connect((IP,PORT))

    print("Tape la lettre a afficher")
    lettre = input(">>> ")

    socket.send(lettre.encode())

