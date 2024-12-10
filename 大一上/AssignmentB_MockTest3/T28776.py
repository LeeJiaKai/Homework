n=int(input())
a0,b0=map(int,input().split())
numbers=[]
for _ in range(n):
    a,b=map(int,input().split())
    numbers.append((a,b))
numbers.sort(key=lambda x:(x[0]*x[1]))
result=0
for i in range(n):
    result=max(result,a0//numbers[i][1])
    a0*=numbers[i][0]
print(result)
