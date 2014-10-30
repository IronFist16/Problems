prime = [2,3,5,7]

myNum = input('Please enter Value = ')
	
x = 1
while (x < myNum):
	if(all((x % y) != 0 for y in prime) and (myNum % x) == 0):
		print x
	x = x+1
