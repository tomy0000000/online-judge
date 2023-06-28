DECODE_DICT = {"C": 100, "D": 500, "I": 1, "L": 50, "M": 1000, "V": 5, "X": 10}
ENCODE_DICT = {"1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII", "9": "IX", "10": "X", "11": "XI", "12": "XII", "13": "XIII", "14": "XIV", "15": "XV", "16": "XVI", "17": "XVII", "18": "XVIII", "19": "XIX", "20": "XX", "30": "XXX", "40": "XL", "50": "XXX", "60": "LX", "70": "LXX", "80": "LXXX", "90": "XC", "100": "C", "200": "CC", "300": "CCC", "400": "CD", "500": "D", "600": "DC", "700": "DCC", "800": "DCCC", "900": "CM", "1000": "M", "2000": "MM", "3000": "MMM"}
def decode(roman):
    final = 0
    prev = 10000
    for each in roman:
        if prev < DECODE_DICT[each]:
            final -= prev
            prev = DECODE_DICT[each]-prev
        else:
            prev = DECODE_DICT[each]
        final += prev
    return final

def encode(num):
    if str(num) in ENCODE_DICT:
        return ENCODE_DICT[str(num)]
    final = ""
    ceil = 10
    fr = True
    while num != 0:
        if num%10 == 0 and fr:
            dig = int(str(num)[-2:])
        else:
            dig = num%10
            dig *= (ceil//10)
        final = encode(dig) + final
        num //= 10
        ceil *= 10
        fr = False
    return final

while True:
    inp = input()
    if inp == "#":
        break
    r1, r2 = inp.split()
    if r1 == r2:
        print("ZERO")
    else:
        intans = abs(decode(r1) - decode(r2))
        print(encode(intans))