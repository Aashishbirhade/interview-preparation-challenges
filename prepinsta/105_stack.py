class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
        self.capacity = 5
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False
    def isfull(self):
        if self.top == self.capacity-1:
            return True
        else:
            return False
    def push(self,d):
        if self.isfull():
            print("stack is full")
        else:
            self.top += 1
            self.stack.append(d)
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            d = self.stack.pop()
            self.top -= 1
            return d

    def print(self):
        print(self.stack)
s = Stack()
while True:
    print("Menu Card :")
    print("1.Push")
    print("2.Pop")
    print("3.Print")
    n = int(input("Enter any choice"))
    if n == 1:
        d = int(input("Enter data"))
        s.push(d)
    if n== 2:
        print("deleted element is ",s.pop())
    if n==3:
        s.print()