import sys
for input in sys.stdin:
    a,b = input.split()
    a = int(a)
    b = int(b)
    while b != 0:
        a, b = b,a%b
    print (a)