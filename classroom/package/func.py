def ajoute_un(v):
	return v + 1

def table_hamza(nb, max=10):

	i = 0

	while i < max:
		print (nb,"*",i , "=", nb * i)
		print ("hamza")
		i+= 1

if __name__ == "__main__":
	table_hamza(2)