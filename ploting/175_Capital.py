def capital(a):
    for i in a:
        if i.islower():
            return False
    return True

a ="USA"
print(capital(a))