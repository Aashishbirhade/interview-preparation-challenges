class Encapsulation:
    def __init__(self):
        self.name = 'veer'
        self._naav = 'protected'
        self.__pro = 'private'
    def privatetopublic(self):
        return self.__pro
  
        
c = Encapsulation()
print(c.name)
print(c._naav)
# print(c.__pro)
print(c.privatetopublic())