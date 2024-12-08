def permutation(a):
    fact = 1
    for i in range(1,a+1):
        fact *= i
    return fact
n,r = map(int,input("Enter no of person and cheir : ").split())
print(f"permutation:{permutation(n)//permutation(n-r)}")