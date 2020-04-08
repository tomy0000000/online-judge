Num = int(input())

#Fetch all Prime Factors and save into Dictionary
D = {}
while Num != 1:
    init = 2
    while Num % init != 0:
        init += 1
    if init in D.keys():
        D.update({init:D[init]+1})
    else:
        D[init] = 1
    Num = Num // init

#Build a new sorted list of Prime Factors
Keys = list(D.keys())
Keys.sort()

#Print results with order
for each in range(len(Keys)-1):
    if D[Keys[each]] == 1:
        print (Keys[each], end = " * ")
    else:
        print(str(Keys[each]) + "^" + str(D[Keys[each]]), end = " * ")
if D[Keys[len(Keys)-1]] == 1:
    print (Keys[len(Keys)-1])
else:
    print(str(Keys[len(Keys)-1]) + "^" + str(D[Keys[len(Keys)-1]]))