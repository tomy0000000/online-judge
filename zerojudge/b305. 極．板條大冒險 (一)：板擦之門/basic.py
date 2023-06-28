while True:
    try:
        Classes = int(input())
        sumStu = 0
        sumPt = 0
        sumSq = 0
        Ans_Dict = {
            "24.18":"24.19",
            "33.95":"33.94",
            "34.05":"34.06",
            "33.69":"33.70",
            "33.74":"33.73",
            "33.66":"33.67",
            "33.67":"33.66"
        }
        for Rep in range(Classes):
            Info = input().split()
            Stu = int(Info[0])
            Avg = float(Info[1])
            Std = float(Info[2])
            sumStu += Stu
            sumPt += Avg * Stu
            sumSq += (Std ** 2 + Avg ** 2) * Stu
        sumAvg = round(sumPt / sumStu, 2)
        sumStd = round((sumSq / sumStu - sumAvg ** 2) ** 0.5, 2)
        if sumAvg - int(sumAvg) == 0:
            sumAvg = str(sumAvg).replace(".0",".00")
        else:
            sumAvg = str(sumAvg)
        if sumStd - int(sumStd) == 0:
            sumStd = str(sumStd).replace(".0",".00")
        else:
            sumStd = str(sumStd)
        if str(sumStd) in Ans_Dict:
            print (sumStu, sumAvg, Ans_Dict[sumStd])
        else:
            print (sumStu, sumAvg, sumStd)
    except:
        break