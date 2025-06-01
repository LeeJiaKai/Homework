for T in range(int(input())):
    ans = True
    n =  int(input())
    phone = list(input() for _ in range(n))
    phone.sort(key=lambda x:len(x))
    for i in range(n-1):
        m = len(phone[i])
        for j in range(i+1,n):
            if phone[i] == phone[j][:m]:
                ans = False
    if ans:
        print("YES")
    else:
        print("NO")
