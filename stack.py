class Stack:
    def __init__(self, size):
        self.max_size = size
        self.stack_array = []
    
    def push(self, value):
        if len(self.stack_array) == self.max_size:
            print("Stack is full. Cannot push element", value)
        else:
            self.stack_array.append(value)
    
    def pop(self):
        if len(self.stack_array) == 0:
            print("Stack is empty.")
            return -1
        else:
            return self.stack_array.pop()
    
    def peek(self):
        if len(self.stack_array) == 0:
            print("Stack is empty.")
            return -1
        else:
            return self.stack_array[-1]
    
    def is_full(self):
        return len(self.stack_array) == self.max_size
    
    def is_empty(self):
        return len(self.stack_array) == 0
    
    def display_elements(self):
        print("Elements:")
        for element in reversed(self.stack_array):
            print(element)


# Main program
stack = Stack(5)

stack.push(9)
stack.push(3)
stack.push(6)
stack.push(7)

print("Element at top of the stack:", stack.peek())
stack.display_elements()

print("Stack full:", stack.is_full())
print("Stack empty:", stack.is_empty())

stack.pop()

print("Element at top of the stack:", stack.peek())
stack.display_elements()