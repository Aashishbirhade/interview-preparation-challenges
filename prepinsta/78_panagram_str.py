a = "The quick brown fox jumps over the lazy dog"
c = "abcdefghijklmnopqrstuvwxyz"
a = a.lower()
v =False
for i in c:
    if i  in a:
       v = True
if v:
    print("given str is panagram")
else:
    print("Not")