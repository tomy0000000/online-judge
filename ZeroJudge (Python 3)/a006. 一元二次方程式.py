a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
Exe = b**2 - 4*a*c
if Exe > 0:
    print ("")
    print("Two different roots x1=" + str(int(((-b)+Exe**0.5)/(2*a))) + " , x2=" + str(int(((-b) - Exe**0.5)/(2*a))))
elif Exe == 0:
    print ("Two same roots x=" + str(int((-b)/(2*a))))
else:
    print ("No real root")