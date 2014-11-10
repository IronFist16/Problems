#a**2 + b**2 = c**2
#a + b + c = 1000
#
#sqrt(a**2 + b**2) = 1000 - (a + b)
#
#a**2 + b**2 = 1000000 - 2000a - 2000b + a**2 + b**2 + 2*a*b
#
#2000(a+b) - 2*a*b = 1000000
#
#1000(a+b) - a*b = 500000
#
#b = (500000 - 1000*a)/(1000 - a) 

a,b,c=0,0,0
for a in range (333):
	b = (500 - float(a))/(1 - float(a)/1000)
	if b.is_integer():
		c = 1000 - (a+b)
		if c**2 == a**2 + b**2 and a < b < c:
			print a,b,c
