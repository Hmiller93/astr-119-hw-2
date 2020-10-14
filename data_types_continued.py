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