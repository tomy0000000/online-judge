cnt = int(input())
for t in range(cnt):
    nums = list(input())
    final = 1
    for each in nums:
        final *= int(each) if each != "\r" else 1
    print(final)
