def main():

	i = 0 
	x = 119.0

	for i in range(120):	#loops i from 0 to 119
		if((i%2)==0):
			x += 3	#add 3 to x if i is even
		else:
			x -= 5	#subtract 5 from x if i is odd

	s = "%3.2e" % x	#creates a string containing x 
					#in csi. notation to 2 decimal places
	print(s)

if __name__ == '__main__':
	main()