def afficher(sep=' ', end='\n', *param):


	param = list(param)
	cup = ['pommme', 'fraise', 'framboise']
	print param
	for i, para in enumerate(param):
		param[i] = str(para)
		print (para)
	print param

	chaine = sep.join(param) + end

	print(chaine)

#if __name__ == "__main__":
#(a, b, c, d) = (1, 3, "hamza", [['pommme', 'fraise', 'framboise'], ['pommme', 'fraise', 'framboise']])
#	afficher(' ', '\n', ())