s= 'aashish birhade'
result= " "
for i in s.split():
    result =result + i[0].upper()+ i[1:-1] + i[-1].upper() +" "
print(result)