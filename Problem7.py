import time

class Node:
	__slots__ = ('data', 'next',)
	
	def __init__(self,data=None,next=None):
		self.data = data
		self.next = next
		
		def __str__(self):
			return str(self.data)
			
class LinkedList:	
	__slots__ = ('length', 'head', 'cur', 'tail', )
	
	def __init__(self):
		self.head   = Node(2)
		self.cur = self.head
		self.curPrime = self.cur
		self.tail = self.cur
		self.length = 1
		
	def add_node(self,data):
		new_node = Node(data,None)
		self.cur.next = new_node
		self.cur = new_node
		self.length += 1
		
	def list_print(self):
		node = self.head
		while node:
			print node.data, ('-')
			node = node.next
			
	#def printBack(self):
	#	if self == None: return
	#	list_print(self.next)
	#	print self
		
count = input('Enter a number of prime = ')

s = time.time()

myTry = 3

primeList = LinkedList()

while(primeList.length <= count):
	primeList.curPrime = primeList.head
	prime = 1
	while(primeList.curPrime.data * primeList.curPrime.data <= myTry):
		if(myTry % primeList.curPrime.data == 0):
			prime = 0
			break
		primeList.curPrime = primeList.curPrime.next
	if (prime):
		 primeList.add_node(myTry)
	if(primeList.length == count):
		primeList.tail = primeList.cur
	myTry += 1

delta_time = time.time() - s
#primeList.list_print()
print 'Calculation time =', delta_time
#print ('Length = '), primeList.length 
#print ('Head = '), primeList.head.data
#print ('Tail = '), primeList.tail.data
print 'The ' + repr(count) + 'st prime = ' + repr(primeList.tail.data)
