def getArrayPos(anyArray,number):
	arrayreturn = []
	for i,line in enumerate(anyArray):
		for j,val in enumerate(line):
			if val == number:
				arrayreturn.append([i*90,j*90])
	return arrayreturn