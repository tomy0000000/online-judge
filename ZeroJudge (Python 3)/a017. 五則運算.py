import sys
for input in sys.stdin:
    input = input.replace("/", "//")
    print(int(eval(input)))