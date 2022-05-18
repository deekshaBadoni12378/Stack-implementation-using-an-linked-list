

class Node:
	
	
	def __init__(self,x):
		self.x = x
		self.next = None
	
class Stack:
	
	
	def __init__(self):
		self.top = None
	
	
	def isempty(self):
		if self.top == None:
			return True
		else:
			return False
	
	
	def push(self,x):
		
		if self.top == None:
			self.top=Node(x)
			
		else:
			newnode = Node(x)
			newnode.next = self.top
			self.top = newnode
	
	
	def pop(self):
		
		if self.isempty():
			return None
			
		else:
			
			poppednode = self.top
			self.top = self.top.next
			poppednode.next = None
			return poppednode.x
	
	
	def peek(self):
		
		if self.isempty():
			return None
			
		else:
			return self.top.x
		
	def display(self):
		
		iternode = self.top
		if self.isempty():
			print(" Underflow")
		
		else:
			
			while(iternode != None):
			
				print(iternode.x,"->",end = " ")
				iternode = iternode.next
			return
		
Stacklist = Stack()

Stacklist.push(12)
Stacklist.push(26)
Stacklist.push(37)
Stacklist.push(49)


Stacklist.display()


print("\nTop element is ",Stacklist.peek())


Stacklist.pop()
Stacklist.pop()


Stacklist.display()


print("\nTop element is ", Stacklist.peek())


