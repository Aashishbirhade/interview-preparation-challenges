class A:
    def __init__(self,num):
        self.n = num
    def sum(self):
        return self.n + 10
class B(A):
    def __init__(self,num):
        self.n = num
    def squre(self):
        return self.n**2

b = B(10)
print(b.squre())
print(b.sum())
