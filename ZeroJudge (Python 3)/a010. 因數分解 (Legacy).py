Num = int(input())

#Fetch Prime Numbers (2 ~ 5000)
Primes = []
for each in range (2,5001):
    NonPrime = False
    for test in range (2, each):
        if each % test == 0:
            NonPrime = True
            break
        else:
            continue
    if NonPrime == False:
        Primes.append(each)

#Check if Input is Prime Number
if Primes.count(Num) != 0:
    print (Num)

#If not, list all Prime Factors and count the repetition
else:
    Divisor = []
    Results = "-"
    for each in Primes:
        if Num % each == 0:
            Divisor.append(each)
    for each in Divisor:
        Dimen = 1
        Current = each
        while Num % Current ==0:
            Dimen += 1
            Current = each ** Dimen
        if Dimen == 2:
            Results = Results + " * " + str(each)
        else:
            Results = Results + " * " + str(each) + "^" + str(Dimen-1)
    print (Results.replace("- * ", ""))