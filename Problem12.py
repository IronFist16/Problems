import time

strt = time.time()

mySum = 0
primes = []
i = 0
pwrSum = 1
lastNb = 2
dv = 2

while (pwrSum < 500):
	i += 1
	mySum += i
	print "mysum = ", mySum
	myTry = lastNb
	pwrSum = 1
	
	#Primes Searching in range of (lastNumber, mySum)
	dv = 2
	while(myTry <= mySum):
		j = 0
		dv = 2
		prime = 1
		while(dv*dv <= myTry):
			if(myTry % dv == 0):
				prime = 0
				break
			j += 1
			dv = primes[j]
		if prime:
			#print "Prime = ",myTry
			primes.append(myTry)
		myTry += 1
	
	#Power of Prime Factors
	
	for elem in primes:
		pwr = 1
		while not mySum % (elem ** pwr):
			#print "Current Pwr = ",pwr
			pwr += 1
		if pwr > 1: 
			pwrSum = pwrSum*pwr	
			#print elem
	
	lastNb = mySum + 1
	#print "Last Number = ", lastNb
	#print "Primes = ",primes
	#for elem in primes:
	#	print elem
	#print "Nb of Divisors = ", pwrSum
	#print"*******"
	#nxt = input("Enter 1 :")

#print primes
print "Calc. Time = ", time.time() - strt
print "Triangle Nb = ", mySum
print "Divisors total of = ", pwrSum
