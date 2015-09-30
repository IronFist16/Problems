def fct(size):
	d={}
	for i in range(size+1):
		for j in range(size+1):
			d[(i,j)] = 0
			if i == 0 or j == 0:
				d[(i,j)] = 1
			else:
				d[(i,j)] = d[(i-1),j] + d[(i,j-1)]
	return d[(size-1,size-1)]
	
print fct(20)
