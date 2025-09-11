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