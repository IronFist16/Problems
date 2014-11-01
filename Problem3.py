myNum = input('Please enter Value = ')
	
while (x*x < myNum):
    while(myNum % x == 0):
        myNum /= x 
    x+=1

print myNum
