try:
	print(a)	#throws an exception since a is not defined
except:
	print("a is not defined!")

try:
	print(a)
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong.")

#this will break the program
#since a is not defined
print(a)