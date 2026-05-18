import numpy as np
parte1 = np.arange(50)
parte2 = np.random.randint(49, 101, 50)

array_finale = np.concatenate([parte1, parte2])

print("Array completo:", array_finale)

print("dtype:", array_finale.dtype)
print("shape:", array_finale.shape)


array_finale = np.concatenate([parte1, parte2], dtype="float64")
print("Nuovo dtype:", array_finale.dtype)
print("Shape dopo conversione:", array_finale.shape)


print("primi 10 " , array_finale[:10])
print("ultimi 7 " , array_finale[-7:])
print("da 5 a 20 indice " , array_finale[5:20])
print("con step di 4 " , array_finale[3::4])


print("Array modificato:", array_finale)
indices = [0, 3, 7, 12, 25, 33, 48]
print("array con indici" , array_finale[indices]) 

print("con pari" , array_finale[array_finale % 2 == 0])
print("media" , np.mean(array_finale))
print("numeri superiori alla media " , array_finale[array_finale  > np.mean(array_finale)])


c = array_finale.copy()
c[10:15] = 999
print("con indici modificati " , c )
print("originale",array_finale)

