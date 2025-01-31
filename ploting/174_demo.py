a = 15
for i in range(1,a+1):
    if i%3 == 0 and i%5 == 0:
        print("FIZZABUZZ",end=" , ")
    elif i%3== 0:
        print("FIZZA",end=" , ")
    elif i%5 == 0:
        print("BUZZU",end=" , ")
    else:
        print(i,end=" , ")