# Taille de l'arbre h_tree
h_tree = 6.34

#Affiche h_tree
print(h_tree)

#Affiche le type de h_tree
print(type(h_tree))

#Change le type de h_tree en int
int_h_tree = int(h_tree)

#Affiche int_h_tree
print(int_h_tree)

# Affiche le type de int_h_tree
print(type(int_h_tree))

phrase_2003 = "jE pEnSE doNc jE sUIs "
# metter en majuscule une variable
phrase_u = phrase_2003.upper()

print(phrase_u)
# en minuscule
phrase_1 = phrase_2003.lower()

print(phrase_1)

# permet d'écrire la première lettre d'une chaîne de caractères en majuscule.
phrase = phrase_2003.capitalize()

print(phrase)

# La variable animals
animals = ['chien','éléphant','hibou','écureuil','canard','éléphant','oiseau','grenouille','éléphant','vache','taureau','cheval','grenouille','abeille','papillon','mouche','singe','tigre','girafe','pandas']
# connaitre la longueur d'une liste
print(len(animals))

# La fonction max() permet de connaître le plus grand élément d'une liste.
# La liste de la taille des arbres
trees_height = [56, 43,43,13,13,31,44.54, 96.5]

# Affiche le plus grand élément de trees_height
print(max(trees_height))

# Ouvre la documentation de round
help(round)

# Crée la variable number
number = 76.4338474755

# Arrondis number a deux chiffres 
print(round(number, 2))
# Arrondis à un chiffre 
print(round(number, 1))
# Arrondis à l'unité
print(round(number))

# La liste de la taille des arbres
trees_height = [56, 43,43,13,13,31,44.54, 96.5]
# Classe trees_height par ordre croissant
increasing_trees_height = sorted(trees_height)

# Classe trees_height par ordre décroissant
decreasing_trees_height = sorted(trees_height, reverse=True)

print(increasing_trees_height)
print(decreasing_trees_height)

# La liste des noms et des temps
names = ['Thomas','Robert','Sara','Pierre' ]
times = [25.4, 21.4, 53.4, 11.2]

# Trouve le plus petit temps
min_time = min(times)
print('Le plus petit temps est', min_time)

# Trouve l'index de min_time
index_min_time = times.index(min_time)
print('Son index est : ', index_min_time)

# Trouve le nom correspondant à l'index
winner = names[index_min_time]
print('Le gagnant est :', winner)

# La liste des pays
es_gold_country = ['Coreée', 'France', 'Italie', 'Russie', 'Hongrie', 'Hongrie', 'Roumanie', 'Russie', 'Russie', 'Russie' ]

print(es_gold_country.count('Russie'))

# La variable liste 
sentence = """La forêt Dhaki SUD contient bien 624 orangers et 512 bananiers. 
            Cet hiver on aura plus de 6000 oranges à récolter! """

# Modifie la variable utilisant la méthode replace()
# pour remplacer les orangers par citronniers et oranges par citrons
new_sentence = sentence.replace("orangers", "citronniers")
new_sentence = new_sentence.replace("oranges", "citrons")

# Affiche new_sentence 
print(new_sentence)

# La liste areas
areas = [12.35, 12.0, 21.0, 11.85, 9.60]

# Utilise append() deux fois pour ajouter les surface de la piscine et le garage
areas.append(24.5)
areas.append(15.45)


# Affiche areas 
print(areas)


# Utilise sort() 
areas.sort()
# Affiche areas 
print(areas)

# Les packages
# connus: NumPy, matplotlib, scikit learn, commande pip pour installer package

# Importe statistics
import statistics

time_circle = [88, 224, 365,687,4333,10759,30685,60189,90465]

#Calcule la moyenne 
mean_time_circle = statistics.mean(time_circle)

#Affiche la moyenne
print(mean_time_circle)


# Importe math
import math

# Caclcule la factorielle de 18
result = math.factorial(18)

# Affiche result
print(result)


# import numpy 
import numpy as np

# La liste x
x =[[1,2],[3,4]]

# Un Array 
numpy_x = np.array(x)

# Tu imaginais peut etre des commentaires en francais....
 # Compute sum of all elements; prints "10"
print(np.sum(x)) 

# Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=0))  

 # Compute sum of each row; prints "[3 7]"
print(np.sum(x, axis=1))

