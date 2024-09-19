year = int(input())
if year % 100 == 0 and year %400 != 0:
    print("N")
elif year % 4 == 0:
    print("Y")
else:
    print("N")
