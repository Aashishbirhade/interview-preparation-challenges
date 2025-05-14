age = []
for i in range(int(input("enter number of patients "))):
    a = int(input("enter age of patient "))
    if a > 0 and a < 120:
        age.append(a)
    else:
        print("invalid input")
        break
    
fare = 0
for i in age:
    if i <= 20:
        fare += 200
    elif i <= 40:
        fare += 400
    else:
        fare += 300
print("total fare is",fare)