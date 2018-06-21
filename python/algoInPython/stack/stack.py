class Stack:

    def __init__(self):
        self.top = -1
        self.maxsize = 100
        self.stk = [None] * self.maxsize

    def push(self, data):
        if(self.top != self.maxsize-1):           #Checking stack overflow.
            self.top += 1
            self.stk[self.top] = data

    def printStack(self):
        print('PRINTING STACK.................')
        if(self.top == -1):
            print('Stack is Empty.')
        else:
            for index in range(self.top+1):
                print self.stk[index]

    def pop(self):
        if(self.top == -1):
            print('Stack is Empty.')
        else:
            self.stk[self.top]=None
            self.top-=1


if __name__=='__main__':
    s = Stack()
    s.push(1)
    s.push(5)
    s.push(2)
    s.push(6)
    s.push(8)
    s.push(3)
    s.printStack()
    s.pop()
    s.pop()
    s.pop()
    s.printStack()
    s.push(8)
    s.push(3)
    s.push(6)
    s.printStack()
