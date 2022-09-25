# Python program to demonstrate
# stack for strings implementation using list

class Stack:
    # initializing stack
    def __init__(self):
        self.stack = []


    # push() function to push element in the stack
    def push(self, value):
        self.stack.append(value)
        print("{} added to the stack".format(value))


    # pop() function to pop element from stack in LIFO order
    def pop(self):
        if (len(self.stack) == 0):
            print("Stack Underflow")
            return
        
        remove = self.stack.pop()
        print("{} removed from the stack".format(remove))
        return remove


    # top() function to view the element on the top of the stack
    # i.e. the last element in the last
    def top(self):
        if (len(self.stack) == 0):
            print("The stack is empty")
            return
        
        top = self.stack[-1]
        print("Top of the stack is {}".format(top))
        return top


    # get_size() function to return the size of the stack
    def get_size(self):
        size = len(self.stack)
        print("Size of the stack is {}".format(size))
        return size


    # is_empty() function to check if the stack has any elements
    def is_empty(self):
        if (len(self.stack) == 0):
            print("The stack is empty")
            return True
        
        print("The stack is not empty")
        return False


    # display() function to print all the elements in the stack
    def display(self):
        if (len(self.stack) == 0):
            print("The stack is empty")

        else:
            for element in self.stack:
                print(element)        


stack = Stack()
while True:
    print('1. push')
    print('2. pop')
    print('3. top')
    print('4. size')
    print('5. check if empty')
    print('6. display')
    print('7. exit')
    
    option = int(input('Enter the function to be executed from 1 to 7: '))
    
    if (option == 1):
        value = int(input('Enter the element to be pushed: '))
        stack.push(value)
        
    elif (option == 2):
        pop = stack.pop()
            
    elif (option == 3):
        top = stack.top() 
            
    elif (option == 4):
        size = stack.get_size()

    elif (option == 5):
        empty = stack.is_empty()
        
    elif (option == 6):
        stack.display()

    elif (option == 7):
        break
        
    else:
        print('Invalid option')

    print('\n')
    input('Press any key to continue')
        