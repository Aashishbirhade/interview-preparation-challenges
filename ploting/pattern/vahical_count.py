vehical= 200 
wheels = 540 
# Wheels from four-wheelers = 4 * x
# Wheels from two-wheelers = 2 * (V - x)
x = (wheels - 2*vehical)//2
print("car count ",x)
print("two wheeler bikes", vehical-x)