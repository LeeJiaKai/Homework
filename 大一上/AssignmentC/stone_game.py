def game(a, b):
    global hand
    if a >= 2*b or a == b:
        return
    else:
        hand += 1
        game(b, a-b)
        return

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    a1, b1 = max(a,b), min(a,b)
    hand = 0
    game(a1,b1)
    if hand % 2 == 0:
        print("win")
    else:
        print("lose")