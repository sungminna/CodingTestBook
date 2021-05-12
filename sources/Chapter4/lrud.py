#상하좌우 예제 4-1
n = int(input())
x, y = 1, 1
data = input().split()

for item in data:
    if item == 'L':
        if y != 1:
            y-=1
    if item == 'R':
        if y != n:
            y+=1
    if item == 'U':
        if x != 1:
            x-=1
    if item == 'D':
        if x != n:
            x+=1

print(x, y)