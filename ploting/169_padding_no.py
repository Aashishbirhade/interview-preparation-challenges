a = [6,20,10,140,302]
for i in a:
    p =""
    for j in range(5):
        p += '0' 
    print(str(i).rjust(5,'0')) #add zero at first
print("_______________________________")
for i in a:
    p =""
    for j in range(5):
        p += '0' 
    print(str(i).ljust(5,'0')) #add zero at first
