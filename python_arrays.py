x = [0.0, 3.0, 5.0, 2.5, 3.7]	#defines an array
print(type(x))

#removes third element
x.pop(2)
print(x)

#removes the element equal to 2.5
x.remove(2.5)
print(x)

#adds an element to the end
x.append(1.2)
print(x)

#gets a copy
y = x.copy()
print(y)

#prints how many elements are 0
print(y.count(0.0))

#prints the index with value 3.7
print(y.index(3.7))

#sorts the list
y.sort()
print(y)

#reverse sort
y.reverse()
print(y)

#removes all elements
y.clear()
print(y)