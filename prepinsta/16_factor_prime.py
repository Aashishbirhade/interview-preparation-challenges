def primeFactor(i):
            f = False
            for j in range(2,i):
                if i%j==0:
                    f = True
                    return f
            return f
n = 100
li =[]
for i in range(1,n):
        if n%i == 0 :
            li.append(i)
            v = primeFactor(i)
            if v == False:
                print(i,end = " ")
print("\n All factor",li)

