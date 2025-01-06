class Queue:
    def __init__(self):
        self.front = 0
        self.rare = -1
        self.queue = []
        self.cap = 10
    def isFull(self):
        if self.rare == self.cap-1:
            return True
        else:
            False
    def isEmpty(self):
        if self.rare == -1:
            return True
        else:
            return False
    def Enqueue(self,data):
        if self.isFull():
            print("queue is full")
        else:
            self.queue.append(data)
            self.rare += 1
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            data = self.queue[self.front]
            del self.queue[self.front]
            # self.front += 1
            return data
    def Print(self):
        print(self.queue)

c = Queue()
while True:
    print("Enter Any key")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Print")
    ch = int(input("enter any option "))
    if ch == 1:
        d = int(input("enter data : "))
        c.Enqueue(d)
    elif ch == 2:
        d = c.Dequeue()
        print(f"delete ele is {d}")
    elif ch == 3:
        c.Print()

