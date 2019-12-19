def calltel(x,y):
	Ekb = 343
	Oms = 381
	Vor = 473
	Yar = 485
	if x == Ekb:
		return(y*15)
	elif x == Oms:
		return(y*18)
	elif x == Vor:
		return(y*13)
	elif x == Yar:
		return(y*11)
	else: 
		return('Вы позвонили не туда!')


ctcd  = int(input('Код города:'))
mins  = int(input('Время разговора:'))
calltel(ctcd,mins)