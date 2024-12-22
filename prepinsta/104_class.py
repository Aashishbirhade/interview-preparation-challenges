class Sum:
    def __init__(self,n):
        self.n = n
    def  squre(self):
        return self.n**2
class Area(Sum):
    def area(self):
       return self.n*3.14

a = 10
c = Area(a)
print(c.area())
print(c.squre())
