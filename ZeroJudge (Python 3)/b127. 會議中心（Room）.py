n = int(input())
init = [1, 2]
Target = 3
if n == 1:
    print ("1")
elif n == 2:
    print ("2")
elif n == 3:
    print ("3")
else:
    while Target != n+1:
        init.append(init[Target-3]+init[Target-2])
        Target += 1
    print (init[n-1])