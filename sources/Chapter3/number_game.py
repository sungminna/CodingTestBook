#숫자 카드 게임
n, m = map(int, input().split())

max = 0
for _ in range(n):
    data = list(map(int, input().split()))
    temp = min(data)
    if temp > max:
        max = temp
print(max)