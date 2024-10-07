n = int(input())
notes = [100, 20, 10, 5, 1]
bills = 0
for i in notes:
    bills += n // i
    n -= n//i * i
print(bills)