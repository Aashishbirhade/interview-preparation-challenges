a = "((a+b)*[c-d])//{a-c}"
for i in a:
    if ord(i) == 41 or ord(i) == 40 or ord(i) == 91 or ord(i) == 93 or ord(i) == 123 or ord(i) == 125:
        pass
    else:
        print(i,end="")