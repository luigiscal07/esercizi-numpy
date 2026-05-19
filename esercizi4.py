import numpy as np
# arr = np.linspace(0, 1, 12)

# #print(arr)

# matrice=arr.reshape(3,4)

# random_matrix=np.random.rand(3,4)
# print(random_matrix)

# #sommiamo entrambe le matrici 
# somma1=np.sum(matrice)
# print("La somma della prima matrice è",somma1)
# sommarand=np.sum(random_matrix)
# print("La somma della matrice casuale è",sommarand)

# #---------------------------------------------------------------------------------------------------

# #Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.
# arraycinquanta=np.linspace(0,10,50)
# #print(arraycinquanta)

# # Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0 e 1.
# randomarray=np.random.random(50)
# #print(randomarray)

# # somma dei due array elemento per elemento
# somma=arraycinquanta+randomarray
# #print(somma)

# #somma totale degli elementi del nuovo array
# print("la somma vale",np.sum(somma))

# #Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
# somma_maggiore_5=np.sum(somma[somma>5])
# print("La somma degli elementi maggiori di 5 è",somma_maggiore_5)

#-------------------------------------------------------------------------------------------------
#Inversa di una matrice
import numpy as np

# Creazione di una matrice quadrata
A = np.array([[1, 2], [3, 4]])

# Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)
print(A@A_inv)

