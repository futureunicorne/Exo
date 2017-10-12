from package.func import table_hamza
import os


chaine = str()

while chaine.lower() != 'q':
	chaine = input("Taper q pour quitter\n")

print("Merci")

inventaire = [
	("pommes", 22),
	("melons", 4),
	("poires", 18),
	("fraises", 76),
	("prunes", 51),
]


inventaire_inverse = [(qtt, nom_fruit) for nom_fruit,qtt in inventaire]

inventaire = [(nom_fruit, qtt) for qtt,nom_fruit in sorted(inventaire_inverse, \
reverse=True)]

for elt in enumerate(inventaire):
	print(elt)

chaine2 = "la nuit est tomber"
list1	=  ["le", "jour", "s est", "lever"]

coupe = chaine2.split(" ")
coupe2 =  ".".join(list1)

print(coupe)
print(coupe2)
