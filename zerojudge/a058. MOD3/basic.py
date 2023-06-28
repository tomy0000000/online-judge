repeatNum = int(input())
A1 = A2 = A3 = 0
for each in range(repeatNum):
    Num = int(input())
    if Num % 3 == 0:
        A1 += 1
    elif Num % 3 == 1:
        A2 += 1
    elif Num % 3 == 2:
        A3 += 1
print (A1, A2, A3, sep = " ")