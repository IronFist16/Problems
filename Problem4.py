def palindrome(x,y):
	while (x > 0):
		z = y
		while(z > 900):
			if (str(x*z) == str(x*z)[::-1]):
				print x*z
				return
			z -= 1	
		x -= 1	

palindrome(999,999)
