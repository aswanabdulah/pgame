myvar=input ("Masukan Numerik Atau String :")
if myvar.isnumeric():
	print("C1: Ya, Variable myvar Numerik :", myvar)
else:
	pass

 if not myvar.isnumeric():
 	print("C2: Variable myvar BUKAN Numerik !")
 elif myvar.isnumeric():
 	print("C2: myvar : %s, adalah Numerik", % myvar)