family = []

print(type(family))
# type list

# Remplis la liste family
family = [['Thomas',21.6],['Sara',24.7],['Robert',15.4],['Pierre',13.6 ]]

# Affiche la liste family
print(family)

# Rempli la liste family
family = [
            ['Thomas',21.6, 5, True],
            ['Sara',24.7, 2, True],
            ['Robert',15.4, 18, False],
            ['Pierre',13.6, 13, True] 
        ]

# Affiche la liste  family
print(family)

# ACCEDER A UNE LISTE

# La Liste family 
family = ['Thomas',21.6,'Robert',24.7,'Sara',15.4,'Pierre',13.6 ]

# Affiche le second élément de family
print(family[1])

# Affiche le dernier élément de family 
print(family[-1])

# Affiche le prénom Robert depuis l'index
print(family[2])

# La liste family 
family = ['Thomas',21.6,'Sara',24.7,'Robert',15.4,'Pierre',13.6 ]

# Additionne la taille des deux parents
length_parents = family[1] + family[3]

# Affiche length_parents
print(length_parents)

# La liste family 
family = ['Thomas',21.6,'Sara',24.7,'Robert',15.4,'Pierre',13.6 ]


parents = family[0:4]


children = family[4:8]

# Affichage des listes 
print('La liste parents dhakios est : ', parents)
print('La liste children dhakios est : ', children)
print('La liste entiere est ', parents + children)


# La liste family 
family = [['Thomas',21.6],['Sara',24.7],['Robert',15.4],['Pierre',13.6 ]]

# Affiche 'Thomas' le 1er élément de la 1ère sous liste
print(family[0][0])

# Affiche 24.7
print(family[1][1])

# Affiche 15.4
print(family[2][1])

# MANIPULATION DE LISTE

family = ['Thomas',21.6,'Robert',24.7,'Sara',15.4,'Pierre',13.6 ]

# Ajouter à la fin de la liste
family_complete = family + ['Michel', 22.3]

print(family_complete)

# .append ajoute un seul élément

family = ['Thomas',21.6,'Robert',24.7,'Sara',15.4,'Pierre',13.6 ]

# Ajoute 'Michel'
family.append('Michel')

# Ajoute  22.3
family.append(22.3)

print(family)

# Supprimer un élément avec del()

# Liste family 
family = ['Thomas',21.6,'Robert',24.7,'Sara',15.4,'Pierre',13.6,'Michel', 22.3 ]

# Affiche le nom et mesure du dernier membre de la family 
print(family[-2], family[-1])

# Efface 'Michel' et 22.3
del(family[8:10])

# Affiche de nouveau le nom et mesure du dernier membre de la family 
print(family[-2], family[-1])

# Copier une list avec list(), var.copy() et [ : ]

# La liste family
family = ['Thomas',21.6,'Sara',24.7,'Robert',15.4 ]


# Assigne à fausse_family la variable family
fausse_family = list(family)

# Supprime 'Robert' et 15.4  de fausse_family
del(fausse_family[-1])
del(fausse_family[-1])

# Affiche family
print('family : ',family)

# Affiche fausse_family
print('fausse_family : ',fausse_family)

family = ['Thomas',21.6,'Sara',24.7,'Robert',15.4 ]

# Crée 3 copies de family avec les 3 méthodes
family_copy1 = list(family)
family_copy2 = family.copy()
family_copy3 = family[ : ]

# Supprime le premier élément de family_copy1
del(family_copy1[0])
# Supprime le second élément de family_copy2
del(family_copy2[1])
# Supprime le troisème élément de family_copy3
del(family_copy3[2])
# Affiche family et ses trois copies
print('family :')
print(family)

print('family_copy1 : ')
print(family_copy1)

print('family_copy2 : ')
print(family_copy2)

print('family_copy3 :')
print(family_copy3)


