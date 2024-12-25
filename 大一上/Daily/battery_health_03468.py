while True:
    try:
        n = int(input())
        battery = list(map(float, input().split()))
        battery.sort()
        time = 0
        total_time = sum(battery)
        average_time = total_time / 2
        while True:
            if battery[-1] > average_time:
                battery.pop()
                print(round(sum(battery), 1))
                break
            else:
                print(round(average_time, 1))
                break
    except EOFError:
        break