import network

IP = "10.0.0.188"
PORT = 1111

while True:
    socket = network.newClientSocket()
    socket.connect((IP,PORT))

    print("Tape la lettre a afficher")
    lettre = input(">>> ")

    socket.send(lettre.encode())

