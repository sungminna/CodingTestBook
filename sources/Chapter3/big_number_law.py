#큰수의 법칙
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

print((m // (k+1)) * (data[-1] * k + data[-2]) + (m % (k+1)) * data[-1])
