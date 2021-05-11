#1이 될 때까지
n, k = map(int, input().split())

i = 0
while(n!=1):
    if (n % k == 0):
        n //= k
    else:
        n -= 1
    i+=1

print(i)