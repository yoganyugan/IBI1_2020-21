a=200102
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
#calculate the d and e
print('d=',d)
print('e=',e)
#compare
if d<e :
    print("d is smaller than e")
else :
    print("e is smaller than d")

X=True
Y=False
Z=(X and not Y) or (Y and not X)
W=("X!=Y")
print('Z=',Z)
print('W=Z',W)