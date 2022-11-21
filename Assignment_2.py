Pi=3.141592
print(" Function to find Area of Circle ")
def Area(a):
    sa=Pi*a*a
    return(sa)
R = round(float(input(" Enter Radius of Circle : ")),4)
SA = round(Area(R),4)
print(" Given Radius = {} And Circle Area = {} ".format(R,SA))
