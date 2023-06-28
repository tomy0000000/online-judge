for each in range(int(input())):
    Test = input().replace("\r", "").split(" ")
    for each in range(len(Test)):
        Test[each] = int(Test[each])
    if Test[1]-Test[0] == Test[2]-Test[1]:
        for each in Test:
            print (each, end = " ")
        print (Test[3]*2 - Test[2])
    else:
        for each in Test:
            print (each, end = " ")
        if Test[2] == 0:
            print(0)
        else:
            print (Test[3]**2 // Test[2])