days = int(input().replace("\n", ""))
listing = input().replace("\n","")
listing = listing.split(" ")
Stat = 0
for each in range(len(listing)):
    Stat += (each+1)*int(listing[each])
print (Stat)