def tambah_1(a,b):
	c = a + b
	print(c)

def tambah_2(a,b):
	c = a + b
	print (c)

def tambah_2(a,b):
	c = a + b 
	return c

tambah_1(12,8)
print (tambah_2(22,8))

a=24
b=26
tambah_1(a,b)
print (tambah_2(a,b))
x = 100

def fungsi_1():
	x=10

def fungsi_2():
	global x
	x=200

fungsi_1()
print(x)
fungsi_2()
print(x)