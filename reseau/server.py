import network
import ledArduino
import dicoMatrice2D

IP = "10.0.0.188"
PORT = 1111

socket = network.newServerSocket()
socket.bind((IP,PORT))

while True :
    socket.listen(10)
    print("en ecoute...")

    thread = network.newThread(socket.accept())

    message = thread.clientsocket.recv(4096)
    lettre = message.decode("utf-8")
    print("message recu :", lettre)

    matrice = dicoMatrice2D.dico2D[lettre]
    ledArduino.ledMatrice(matrice)