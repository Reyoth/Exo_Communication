import i2cComm

lettre = "a"
matrice = [ [1,1,1,1,1],
            [1,0,0,0,1],
            [1,1,1,1,1],
            [1,0,0,0,1],
            [1,0,0,0,1]
            ]

for ligne in matrice:
    for led in ligne:
        i2cComm.writeNumber(led)
