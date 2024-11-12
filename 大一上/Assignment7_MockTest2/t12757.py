eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
eng_weishu = ["hundred", "thousand", "million"]
arab = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40, 50, 60, 70, 80, 90]
arab_weishu = [100, 1000, 1000000]

s = list(input().split())

def translate(s):
    ans = 0
    tmp = 0
    for i in s:
        if i in eng_weishu:
            k = eng_weishu.index(i)
            if i == "hundred":
                tmp *= 100
            else:
                ans += tmp*arab_weishu[k]
                tmp = 0
        elif i in eng:
            tmp += arab[eng.index(i)]
    return ans + tmp

if s[0] == "negative":
    ans = -1 * translate(s[1:])
else:
    ans = translate(s)
print(ans)