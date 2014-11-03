
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
		self.length = 0
		self.head   = None
		self.cur = None
		self.tail = None
		
	def add_node(self,data):
		new_node = Node()
		new_node.data = data
		new_node.next = self.cur
		self.cur = new_node
		if (not self.length):
			self.head = new_node
		self.length += 1
		
	def list_print(self):
		node = self.cur
		while node:
			print node.data, ('-')
			node = node.next
			
	#def printBack(self):
	#	if self == None: return
	#	list_print(self.next)
	#	print self
		
count = input('Enter a number of prime = ')

myTry = 2

primeList = LinkedList()

while(primeList.length <= count):
	dv = 2
	prime = 1
	while(dv*dv <= myTry):
		if(myTry % dv == 0):
			prime = 0
			break
		dv += 1
	if (prime):
		 primeList.add_node(myTry)
	if(primeList.length == count):
		primeList.tail = primeList.cur
	myTry += 1



primeList.list_print()
print ('Length = '), primeList.length - 1
print ('Head = '), primeList.head.data
print ('Tail = '), primeList.tail.data
