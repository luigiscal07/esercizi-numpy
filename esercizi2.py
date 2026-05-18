import numpy as np

#Crea una matrice NumPy 2D di dimensioni 6x6 contenente numeri interi casuali compresi tra 1 e 100.
matrice=np.random.randint(1,101,size=(6,6))
#print(matrice)

# 2. Estrai la sotto-matrice centrale 4x4
# Escludiamo la prima e l'ultima riga/colonna
sotto_matrice = matrice[1:5, 1:5]
#print(sotto_matrice)
#print(" ")
# 3. Inverti le righe della matrice estratta
matrice_invertita = sotto_matrice[::-1, :]
print(matrice_invertita)


indici=np.arange(matrice_invertita.shape[0])
diagonale=matrice_invertita[indici,indici]
print(diagonale)



# sostituisce i valori multipli di 3 con -1 della matrice invertita
matrice_invertita[matrice_invertita%3==0]=-1
print(matrice_invertita)

#print finale
# print(matrice)
# print(sotto_matrice)
# print(matrice_invertita)
