import i2cComm

def ledMatrice (matrice):
    for ligne in matrice:
        for led in ligne:
            i2cComm.writeNumber(led)
