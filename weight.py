def imc(poids,taille):
    result = float(poids) / float(taille)**2
    return result

poids = input("Combien pèses-tu ? ")
taille = input("Combien mesures-tu ? ")

if imc(poids,taille) > 26:
    message = "Va faire du sport !"
    print(message)

