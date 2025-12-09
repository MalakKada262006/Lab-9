
import numpy as np
import json
tableau_1d = np.array([1, 2, 3, 4, 5])
print("Tableau 1D :", tableau_1d)
tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
print("Tableau 2D :\n", tableau_2d)

zeros = np.zeros((2, 3))
print("Zeros :\n", zeros)

ones = np.ones((3, 2))
print("Ones :\n", ones)

progression = np.arange(0, 10, 2)  
print("np.arange :", progression)

linspace = np.linspace(0, 1, 5) 
print("np.linspace :", linspace)

print("Tableau 1D + 5 :", tableau_1d + 5)
import numpy as np


tableau_1d = np.array([1, 2, 3, 4, 5])
tableau_2d = np.array([[1, 2, 3],
                       [4, 5, 6]])
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
progression = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)

def inspect(tableau, nom):
    print(f"\n--- {nom} ---")
    print(tableau)
    print("dtype :", tableau.dtype)   
    print("ndim  :", tableau.ndim)   
    print("shape :", tableau.shape)   
    print("size  :", tableau.size)   

inspect(tableau_1d, "Tableau 1D")
inspect(tableau_2d, "Tableau 2D")
inspect(zeros, "Zeros")
inspect(ones, "Ones")
inspect(progression, "np.arange")
inspect(linspace, "np.linspace")


print("\n--- Explications ciblées ---")

print("dtype de zeros :", zeros.dtype)  

mixte = np.array([1, 2, 3.0])
print("np.array([1, 2, 3.0]) :", mixte)
print("dtype :", mixte.dtype) 


print("type(tableau_1d) :", type(tableau_1d))  
print("dtype(tableau_1d) :", tableau_1d.dtype) 
import numpy as np


vecteur = np.arange(1, 10) 
print("Vecteur :", vecteur)


matrice = vecteur.reshape((3, 3))
print("Matrice 3x3 :\n", matrice)

print("Shape :", matrice.shape)  
print("Size  :", matrice.size)   

matrice_auto = vecteur.reshape((3, -1))  
print("Shape auto :", matrice_auto.shape)  

tableau_float = np.array([1, 2, 3], dtype=np.float32)
print("Tableau float32 :", tableau_float)
print("dtype :", tableau_float.dtype)
print("nbytes :", tableau_float.nbytes) 
tableau_int = tableau_float.astype(np.int32)
print("Tableau int32 :", tableau_int)
print("dtype :", tableau_int.dtype)
print("nbytes :", tableau_int.nbytes)


identite = np.eye(4) 
print("Matrice identité :\n", identite)
constant = np.full((2, 2), 7)
print("Tableau constant :\n", constant)
forme_test = np.arange(12).reshape((4, 3))
print("np.arange(12).reshape((4, 3)) :\n", forme_test)


matrice = np.arange(1, 10).reshape((3, 3))
vecteur = np.arange(1, 10)

print("Matrice * 10 :\n", matrice * 10) 
print("Racine carrée du vecteur :", np.sqrt(vecteur)) 
alist = [0] * 6
print("alist (liste Python) :", alist)
print("type(alist) :", type(alist))

zeros = np.zeros(6)
print("np.zeros(6) :", zeros)
print("type(np.zeros(6)) :", type(zeros))
print("Opération vectorisée (zeros + 5) :", zeros + 5)

linspace = np.linspace(0, 1, 5)
print("np.linspace(0, 1, 5) :", linspace)

linspace_no_endpoint = np.linspace(0, 1, 5, endpoint=False)
print("np.linspace(0, 1, 5, endpoint=False) :", linspace_no_endpoint)

vecteur = np.arange(1, 10)  
print("Vecteur :", vecteur)

try:
    matrice_invalide = vecteur.reshape((4, 3))  
except ValueError as e:
    print("Erreur reshape :", e)

tableau = np.array([1, 2, 3])
liste = tableau.tolist()
print("Conversion en liste Python :", liste)

data_json = "[1, 2, 3]"
liste_from_json = json.loads(data_json)
tableau_from_json = np.array(liste_from_json)
print("Conversion JSON -> liste -> tableau NumPy :", tableau_from_json)

print("\nRésumé :")
print("Vous avez exploré la création, inspection, reshape, types et opérations vectorisées avec NumPy.")
print("Prochaines étapes : sum, mean, slicing avancé, masques booléens, et introduction à pandas.")
