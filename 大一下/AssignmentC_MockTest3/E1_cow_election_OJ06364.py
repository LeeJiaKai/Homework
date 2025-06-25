n, k = map(int, input().split())
cow = []
for i in range(n):
    cow.append(list(map(int, input().split())) + [i+1])
cow.sort(reverse=True ,key=lambda x: x[0])
second_cow = cow[:k]
second_cow.sort(reverse=True ,key=lambda x: x[1])
print(second_cow[0][2])
