for Rep in range(int(input())):
    St = int(input()) ** 0.5
    if St - int(St) != 0:
        St = int(round(St, 1)) + 1
    En = int(input()) ** 0.5
    if En - int(En) != 0:
        En = int(round(En, 1))
    Sum = 0
    for each in range(int(St), int(En+1)):
        Sum += each ** 2
    print ("Case " + str(Rep+1) + ": " + str(Sum))