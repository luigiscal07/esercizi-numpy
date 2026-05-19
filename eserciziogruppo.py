import numpy as np
file = open("calcolinumpy.txt" , "w")
iniziamo = input("vuoi iniziare si/no ")

while iniziamo == "si" :
    righe = int(input("di quante righe vuoi la tua matrice: "))
    colonne = int(input("di quante colonne vuoi la tua matrice: "))
    matrice = np.random.rand(righe, colonne)
    print("\nmatrice generata\n" , matrice)

    file.write("Questa e' la matrice")
    file.write( str(matrice))
    



    sottomatrice = matrice[1:righe -1  , 1:colonne -1 ]
    print("\nquesta è la sottomatrice\n" , sottomatrice)

    trasposta = np.transpose(matrice)
    print("\ntrasposta della matrice: \n" , trasposta)
    file.write("Questa e' la matrice trasposta ")
    file.write( str(trasposta))
    

    somma = np.sum(matrice)
    print("la somma della matrice è : " , somma)

    scelta = input("vuoi ripetere si/no: ")
    if scelta != "si" :
        iniziamo = False

    scelta2 = input("vuoi creare una nuova matrice si/no : ")
    if scelta2 == "no" :
         iniziamo = False
    else :
        matrice2 =  np.random.rand(righe, colonne)
        moltiplicazione = matrice*matrice2
        print("la moltiplicazione elemento per elemento fa :  " , moltiplicazione)

        media = np.mean(matrice2)
        print("la media della matrice è: " , media )

        if righe == colonne :
           determinante = np.linalg.det(matrice2)
           print("il determinate è :" , determinante )

        scelta = input("vuoi ripetere si/no: ")
        if scelta != "si" :
            iniziamo = False
