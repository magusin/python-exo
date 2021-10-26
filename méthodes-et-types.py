nbr_tour = "8"

print("Bravo Thueban tu as effectué " + nbr_tour + " tours")

# Nombre de tours 
nbr_tour = 9

# Modifie nbr_tour en String
str_nbr_tour = str(nbr_tour)

# La Variable d'affichage
message = "Bravo Thueban tu as effectué " + str_nbr_tour + " tours"

# Affiche le message 
print(message)

# Les variables des jours précédents (d pour day jour en anglais)
nbr_tour_d1 = "14"
nbr_tour_d2 = "7"
nbr_tour_d3 = "6" 

# Utilise la méthode int() pour aider le robot à calculer
nbr_tour_week = int(nbr_tour_d1) + int(nbr_tour_d2) + int(nbr_tour_d3)

# Utilise la méthode str pour transformer nbr_tour_week
str_tour_week  = str(nbr_tour_week)

# Affiche le message
print("Cette semaine tu as effectué "+ str_tour_week + " tours")

# Jours precedents (1,2,3)
nbr_tour_week = "27"

# Jours suivants (4,5,6,7) 
nbr_tour_d4 = "10" 
nbr_tour_d5 = "9" 
nbr_tour_d6 = "13" 
nbr_tour_d7 = "10" 



# Utilise la méthode int() pour aider le robot a calculer
nbr_tour_week = int(nbr_tour_week) + int(nbr_tour_d4) + int(nbr_tour_d5) + int(nbr_tour_d6) + int(nbr_tour_d7)

# pour trouver la moyenne, on divise le total (nbr_tour_week) sur le nombre de jours (7)
nbr_tour_moy = nbr_tour_week /7

# Utilise la méthode str() pour transformer nbr_tour_moy
str_tour_moy  = str(nbr_tour_moy)

#Affiche la moyenne de cette semaine
print("Cette semaine tu as effectué en moyenne "+ str_tour_moy + " tours par jour")

nbr_tour_moy = "15.2"

nbr_tour_mois = float(nbr_tour_moy) * 30

str_tour_mois  = str(nbr_tour_mois)

#Affiche le nombre de tours du mois
print("Ce mois tu as effectué "+ str_tour_mois + " tours!")

