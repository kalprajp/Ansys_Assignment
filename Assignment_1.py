a=[1,2,3]
b=[4,5,6]
def Merge(x,y):
    for i in y : 
        x.append(i)
    return(x)
ab = Merge(a,b)
print(ab)

