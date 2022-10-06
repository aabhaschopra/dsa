# Python program to perform deletion of an element
# in a doubly linked list

class Node: 
	def __init__(self, value):
		self.value = value
		self.next = None 
		self.prev = None


class DoublyLinkedList: 
	def __init__(self): 
		self.head = None
		self.tail = None


	def insert(self, val): 
		new_node = Node(val)

		# If no head, set new node as head
		if self.head == None: 
			self.head = new_node
			self.tail = new_node

		else: 
			current_node = self.head
			
			while current_node.next != None: 
				current_node = current_node.next
			
			current_node.next = new_node
			new_node.prev = current_node
			self.tail = new_node


	def delete(self, value): 
		if self.head != None: 
			current_node = self.head 

			# If val is the head 
			if self.head.value == value: 
				self.head.next.prev = None
				self.head = self.head.next

			# If val is the tail
			elif self.tail.value == value: 
				self.tail.prev.next = None
				self.tail = self.tail.prev

			else: 
				while current_node.next.value != value: 
					current_node = current_node.next 
					
                    # If val is not in list 
					if current_node.next is None or current_node.next.value != value: 
						print("Value not in list")
						return False

				current_node.next.next.prev = current_node 
				current_node.next = current_node.next.next


	def display(self):
		value_list = []

		if self.head != None: 
			current_node = self.head 

			# Start at head and check if next is not tail
			while current_node.next != None:
				value_list.append(current_node.value)
				current_node = current_node.next 

			value_list.append(current_node.value)
			print(value_list)

		else: 
			print("No nodes")
			return False


doublylinkedlist = DoublyLinkedList()

while True:
    print('1. insert')
    print('2. delete')
    print('3. display')
    print('4. exit')
    
    option = int(input('Enter the function to be executed from 1 to 4: '))
    
    if (option == 1):
        value = int(input('Enter the element to be inserted: '))
        doublylinkedlist.insert(value)
    
    elif (option == 2):
        value = int(input('Enter the element to be deleted: '))
        doublylinkedlist.delete(value)

    elif (option == 3):
        doublylinkedlist.display()
            
    elif (option == 4):
        break
    
    else:
        print('Invalid option')

    print('\n')
    input('Press any key to continue')
