import math
import time
from random import randint
import sys
from package.fonction import *

print("Bonjour et Bienvenue au Casino de Limay\n")
entree = input ("Il s'agit de la du jeu de la roulette, voulez vous jouer (Y/N)?\n")

if entree == 'y':
	print("C'est parti ! Commencons !")
else:
	sys.exit(0)
while 1:
	num		= input ("Merci de renseigner un numero de roulette compris entre 0 et 49 : \n")
	if num >= 0 and num <= 49:
		break
	else:
		print ("le numero doit etre compris entre 0 et 49\n")


mise	= input ("Combien voulez vous miser ? : \n")

chance	= randint(0, 49);

print ("--------------------- 3 ---------------------")
time.sleep( 1 )
print ("--------------------- 2 ---------------------")
time.sleep( 1 )
print ("--------------------- 1 ---------------------")
time.sleep( 1 )

print("La bille s'arrete sur le numero ", chance)
if num == chance:

	gain = 3 * mise
elif ((num % 2 == 0 and chance % 2 == 0) or (num % 2 != 0 and chance % 2 != 0)):
	gain = mise / 2
else:
	gain = 0
time.sleep( 1 )
print ("Vos gains s'eleve a un montant de : " , gain)


