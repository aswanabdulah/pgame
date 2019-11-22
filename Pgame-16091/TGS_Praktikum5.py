a= 80
b= 65
c= 50
nilai = int (input(" Masukan Nilai :"))
if nilai >= a:
	print ("Sangat Baik")
	print ("*"*45)
elif nilai >= b and nilai <=a:
	print ("cukup baik")
	print ("*"*45)
elif nilai >= c and nilai <=b:
	print ("baik")
	print ("*"*45)
else :
	print ("kurang baik")
	print ("*"*45)

