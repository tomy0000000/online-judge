T = input()
Act = 0
Prev = 0
for each in range(len(T)//3):
    Pos = T.find("y", Prev)
    Prev = Pos+1
    Act += abs(each*3 - Pos)
print (Act)