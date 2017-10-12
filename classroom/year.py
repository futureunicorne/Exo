#def fonction_multi(nb):
from package.func import table_hamza
import os

annee = input ("Saisissez votre annee: ")
annee = int(annee)

if (annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0)):
	print ("C est une annee bissextile")
else:
	print ("Ce n est pas une annee bissextile")


chaine =  "le maroc est qualifie"

for lettre in chaine:
	print (lettre)

table_hamza(3);

while 1:
	  lettre = input ("taper Q pour quitter : ")
	  if lettre == 'Q':
	  	print ("fin de boucle")
		break
