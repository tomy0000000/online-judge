import sys
for input in sys.stdin:
    Text = list(input)
    Text.reverse()
    while Text[0] == "0" and len(Text) > 1:
        Text.pop(0)
    print("".join(Text))