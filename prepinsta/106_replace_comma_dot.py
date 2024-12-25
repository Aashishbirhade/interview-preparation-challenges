a = "14,625,498.002"
# Output : 14.625.498, 002 
r = " "
for i in a:
    if i == ".":
        r += ","   
    elif i == ",":
       r +='.'
    else:
        r += i
print(r)