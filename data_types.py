import numpy as np

#integers
i = 10 
print(type(i))

a_i = np.zeros(i,dtype=int)	#declares an array of integers
print(type(a_i))			#returns ndarray
print(type(a_i[0]))         #returns int64

#floats
x = 119.0
print(type(x))	#prints data type of x

y = 1.19e2	    #float 119 in scientific notation
print(type(y))

z = np.zeros(i,dtype=float)	#declares an array of floats
print(type(z))
print(type(z[0]))

#string
s = "I am a string."
print(type(s))

#boolean
yes = True
print(type(yes))

no = False
print(type(no))

#list
alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

#tuple
alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"
except TypeError:
	print("We can't add elements to tuples!")
print(alpha_tuple)