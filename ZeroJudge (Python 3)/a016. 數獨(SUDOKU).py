Raw_data = []
while True:
    try:
        Raw_data.append(input().split())
    except:
        break
        
for each in range((len(Raw_data)+1)//10):
    data = []
    for each_2 in range(9):
        data.append(Raw_data[each*10+each_2])
    
    Valid = True

    #Check Row
    for Row in data:
        if Valid == False:
            break

        for each in range(1, 10):
            if str(each) not in Row:
                Valid = False
                break
    
    #Check Column
    for Col in range(9):
        if Valid == False:
            break

        TempL = []
        for each in data:
            TempL.append(each[Col])
        for each in range(1, 10):
            if str(each) not in TempL:
                Valid = False
                break

    #Check small Square
    for each in range(0, 9, 3):
        if Valid == False:
            break
        for each_2 in range(0, 9, 3):
            if Valid == False:
                break

            TempL = []
            for each_3 in range(3):
                for each_4 in range(3):
                    TempL.append(data[each+each_3][each_2+each_4])

            for each_3 in range(1, 10):
                if str(each_3) not in TempL:
                    Valid = False
                    break

    if Valid == True:
        print("yes")
    else:
        print("no")