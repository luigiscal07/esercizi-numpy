# Esercizio:
# 1. Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
# 2. Verifica il tipo di dato dell'array e stampa il risultato.
# 3. Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
# 4. Stampa la forma dell'array.

# import numpy as np
# arrayrange=np.arange(10,50)
# print(arrayrange)
# print("Il tipo di dato dell'array è",arrayrange.dtype)

# #adesso cambiamo tipo in float
# arrayrange=np.arange(10,50,dtype=float)
# print("Il tipo di dato dell'array è",arrayrange.dtype)
# print("La forma dell'array è:",arrayrange.shape)

import numpy as np
# 1. Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.
arraycasuale=np.random.randint(10,50,size=20)
# 2. Utilizza lo slicing per estrarre i primi 10 elementi
print(arraycasuale[0:10])

ultimicinque=arraycasuale[-5:]
print(ultimicinque)

#Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
print(arraycasuale[5:15])

# stampare ogni terzo elemento
print(arraycasuale[2::3])
#Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
arraycasuale[5:10]=99
print(arraycasuale)



