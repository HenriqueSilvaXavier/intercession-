def intercession(x, y):
	xlista=[]
	ylista=[]
	for k in x:
		xlista.append(k)
	for k in y:
		ylista.append(k)
	zlista=[]
	for k in xlista:
		if k in ylista:
			zlista.append(k)
			ylista.remove(k)
	if type(x)==list and type(y)==list:
		return zlista
	if type(x)==str and type(y)==str:
		z=""
		for k in zlista:
			z=z+k
		return z