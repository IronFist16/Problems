import time

count = input('Enter max number = ')

s = time.time()

myTry = 2
mySum = 0

while(myTry <= count):
	dv = 2
	prime = 1
	while(dv*dv <= myTry):
		if(myTry % dv == 0):
			prime = 0
			break
		dv += 1
	if prime:
		#print myTry
		mySum += myTry
		#count -= 1
	myTry += 1

print ('Calculation time = '), time.time() - s
print ('Sum = '), mySum
