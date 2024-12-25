def remove(s):
    if s == "":
        return "str is empty "
    else:
        return remove(s[1:])
a = "Aashish"
print(remove(a))