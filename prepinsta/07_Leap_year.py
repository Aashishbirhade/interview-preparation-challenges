st = int(input("enter start year"))
end = int(input("enter last year"))
for i in range(st,end+1):

    if (i%4==0) or (i%100!=0 and i%400==0):
        print(i)
   
