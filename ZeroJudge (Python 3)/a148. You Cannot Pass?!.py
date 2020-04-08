while True:
    try:
        nums = input().split()[1:]
        nums = list(map(int, nums))
        print("no" if (sum(nums) > 59*len(nums)) else "yes")
    except:
        break
