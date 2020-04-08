import sys
for input in sys.stdin:
    Text = list(input.replace("\r","").replace("\n",""))
    TestCount = len(Text)//2
    Printing = True
    for each in range(TestCount):
        if Text[each] != Text[len(Text)-each-1]:
            Printing = False
            break
    if Printing == True:
        print ("yes")
    else:
        print ("no")