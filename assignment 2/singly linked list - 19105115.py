# Python program to perform insertion of an element
# after a specified value in a singly linked list

class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class SinglyLinkedList:
    def __init__(self, value):
        self.head = Node(value)


    def insert(self, value, after):
        current = self.head

        while current.next is not None and current.next.value != after:
            current = current.next

        if current.next is None:
            current.next = Node(value)

        else:
            current = current.next
            new = Node(value)
            new.next = current.next
            current.next = new


    def display(self):
        current = self.head
        while current is not None:
            if current.value is not None:
                print(current.value, end = ' ')
            current = current.next
        print()


singlylinkedlist = SinglyLinkedList(None)

while True:
    print('1. insert')
    print('2. display')
    print('3. exit')
    
    option = int(input('Enter the function to be executed from 1 to 3: '))
    
    if (option == 1):
        value = int(input('Enter the element to be inserted: '))
        after = int(input('Enter the element after which it should be inserted (If the element is not present or if the list is empty, element will be added at the end): '))
        singlylinkedlist.insert(value, after)
        
    elif (option == 2):
        singlylinkedlist.display()
            
    elif (option == 3):
        break
    
    else:
        print('Invalid option')

    print('\n')
    input('Press any key to continue')
