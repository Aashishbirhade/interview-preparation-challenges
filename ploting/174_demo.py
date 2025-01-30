a = 15
for i in range(1,a+1):
    if i%3 == 0 and i%5 == 0:
        print("FIZZABUZZ")
    elif i%3== 0:
        print("FIZZA")
    elif i%5 == 0:
        print("BUZZU")
    else:
        print(i)