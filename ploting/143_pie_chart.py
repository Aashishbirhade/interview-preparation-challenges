import matplotlib.pyplot as plt
a = ["a","b","c","d","e"]
c = ['red','pink','green','black','blue']
b = [1,2,3,4,2]
e = [0.05]*len(b)
print(plt.pie(b,labels=a,colors=c,explode=e))
print(plt.show())