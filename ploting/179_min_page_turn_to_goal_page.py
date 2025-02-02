def page_turn(n,p):
    front = p//2
    back = (n//2)-(p//2)
    return (min(front,back))


n = 6 #1|(2,3)|(4,5)|6 (left,right)
p  = 2
print(page_turn(n,p))