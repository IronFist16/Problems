
i = 1
seq = [1,2]

while ((seq[i] + seq[i-1]) <= 4000000):
	seq.append(seq[i] + seq[i-1])
	i = i + 1
	
print('Value of i = '), i	
print ('Fib. Series(100) = '), seq
for k in range(i+1):
	if (seq[k] % 2 == 0):
		print('Even value = '), seq[k] 
print ('Sum of Fib. Series(100) of Even numbers = '), sum(seq[j] for j in range(i+1) if (seq[j] % 2 == 0))
