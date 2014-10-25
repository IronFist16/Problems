

i = 0
l = 0

while (i<1000):
	if ((i % 3) == 0 or (i % 5) == 0) :
		l = l + i
		print 'i = ' + str(i) + '\n'
		print 'Sum = ' + str(l) + '\n'
	i = i+1
		
print 'Total of 3 and 5 multipes is = ' + str(l)
	
