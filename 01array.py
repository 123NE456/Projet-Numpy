import numpy as np

# ici pour creer un arret ou une liste en nympy utiliser la deuxième commande 
# la troisieme ligne ici montre tout simplement l'affichage et le type pour savoir sa class comme vu a run 

a = np.array([1.0,2,3,4])
print(a)
print(type(a))

# ici on peut avoir d'autres dimensions ici pour la première ligne on observe celui a deux dimensions 

b = np.array([[1,2],[3,4]])
print(b)

# ici on peut creer des arrets de 0 par exemple la ligne suivante 
# ici le premier argument est la taille 

zeros_arr = np.zeros(4)
print(zeros_arr)

# ici on creer un tableau d'un nombre a l'autre et le dernier chiffre est le nombre de sortie 
# ici on attribut 0 au debut puis 15 a la fin et le tableu de sortie le chiffre 4

c = np.linspace(0,15,4)
print(c)

# une autre fonction est arange qui permet de creer un arret compris dans une plage
# ici on peut creer une taille avec par defaut 1 et la valeur par defaut du pas est de 0

# tableau de 0 a 9 par un pas de 1
print(np.arange(10))
# tableau de 5 a 9 par un pas de 1
print(np.arange(5,10))
# tableau de 0 a 8 par un pas de 4
print(np.arange(0,10,4))

# ici avec cette fonction on peut prendre un arret et la transformer en la taille que nouc voulons 
# ici on cree un arret de 0 a 19 avec une transformation en 5 lignes et 4 colonnes 
M = np.arange(20).reshape(5,4)
print(M)


