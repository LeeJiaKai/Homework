n, k = map(int, input().split())
t = list(map(int, input().split()))
t.sort()
total_time = sum(t)
average_time = total_time/k
while True:
    if t[-1] > average_time: #if the longest chick last longer than avg_time
        total_time -= t.pop() #put it in one slot for the whole time
        k -= 1
        average_time = total_time/k #calculate the remaining chick
    else: #when none of the chick last longer than avg_time
        print(f'{average_time:.3f}') #达到最优解
        break