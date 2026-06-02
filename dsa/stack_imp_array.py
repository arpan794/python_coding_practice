# stack implementation using array

class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def Pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def iter(self):
        if self.isEmpty():
            return None
        for i in range(len(self.stack)):
            print(self.stack[i])

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[-1]
        
    def Size(self):
        return len(self.stack)


    def isEmpty(self):
       return len(self.stack) == 0


stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)

stack1.iter()
print("is Empty: ",stack1.isEmpty())
print("peek: ",stack1.peek())
print("size: ",stack1.Size())
print("pop: ",stack1.Pop())
print("size: ",stack1.Size())
stack1.iter()
print("size: ",stack1.Size())