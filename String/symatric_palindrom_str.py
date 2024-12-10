a = 'amaama'
h = len(a)//2
sub = a[h:]
rev = sub[::-1]
f = True
f1 = True
for i in range(h):
    if a[i] != sub[i]:
        f = False
    if  a[i] != rev[i]:
        f1 = False

if f == True:
    print("Given Str is symatrical")
else:
    print("NOT Symatric")
if f1 == True:
    print("Given Str is Palindro")
else:
    print("NOT Palindrom")

