import numpy as np

# ici on dispose d'un tableau ou liste
arr = np.array([-3,-4,1,4,5])
# ici on identifie la moyenne de cette liste 
print('mean:',arr.mean())
# ici on identifie le chiffre minimale de cette liste 
print('min:',arr.min())
# ici on identifie le chiffre maximale de cette liste
print('max:',arr.max())
# ici on calcule la mediane de cette liste 
print('median:',np.median(arr))   

# shape ici sers a connaitre la dimension d'un array 
first = np.array([[1, 2, 3], [4, 5, 6]])
# first.shape
print(first.shape)

A = np.array([[5, 0, 3], [3, 7, 9]])
A
print(np.cos(A))
print(A.mean())

np.corrcoef(A) # matrice de correlation moi meme je ne comprend pas du coup esaye de voir la doc
print(np.unique(A, return_counts = True)) # retourne le nombre de fois qu'une entités apparait

