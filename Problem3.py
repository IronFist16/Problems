prime = [2,3,5,7]

myNum = input('Please enter Value = ')
	
while (x*x < myNum):
    while(myNum % x == 0):
        myNum /= x 
    x+=1

print myNum
