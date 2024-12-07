x,y = map(int,input("Enter x and y value: ").split())
if x >0 and y>0:
    print(f"{x} and {y} lie in first quadrant")
elif x <0 and y> 0:
    print(f"{x} and {y} lie in second quadrant")
elif x <0 and y < 0:
    print(f"{x} and {y} lie in Third quadrant")
elif x >0 and y < 0:
    print(f"{x} and {y} lie in Fourth quadrant")
elif x == 0 and y == 0:
    print(f"{x} and {y} lie on the origin ")
elif x == 0 and y != 0:
    print(f"{x} and {y} lie on y- axis")
elif x!=0 and y == 0:
    print(f"{x} and {y} lie on x-axis")