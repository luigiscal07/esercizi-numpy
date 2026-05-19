#Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
import numpy as np
# array15=np.random.randint(1,101,15)
# print(array15)

# #Calcolare e stampare la somma di tutti gli elementi dell'array.
# somma=np.sum(array15)
# print("la somma vale",somma)
# #Calcolare e stampare la media di tutti gli elementi dell'array.
# media=np.mean(array15)
# print("la media vale",media)

#------------------------------------------------------------------------------------------------------------
#Parte 2
#Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25
array25=np.arange(1,26)
matriceok=np.reshape(array25,(5,5))
#print(matriceok)
  
# Estrarre e stampare la seconda colonna della matrice.
secondacolonna=matriceok[:,1]
#print(secondacolonna)

#Estrarre e stampare la terza riga della matrice.
terzariga=matriceok[2,:]
#print(terzariga)

#Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
indici=np.arange(matriceok.shape[0])
diagonale=matriceok[indici,indici]
somma_diagonale=np.sum(diagonale)
#print(somma_diagonale)

#----------------------------------------------------------------------------------------------------------------
#Parte 3
#Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
matrix50=np.random.randint(10,51,size=(4,4))
print(matrix50)
#Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0)
righe= np.array([0,1,2,3])
colonne=np.array([1,3,2,0])
elementisel=matrix50[righe,colonne]
print("  ")
print(elementisel)

#Utilizzare fancy indexing per selezionare e stampare tutte
#Le righe dispari dell'array (considerando la numerazione delle righe che parte da 0)

