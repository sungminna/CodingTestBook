data = input()
row = int(data[1])
column = int(ord(data[0]))-int(ord('a'))+1

case = 0
step = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
for item in step:
    next_row = row + item[0]
    next_column = column + item[1]

    if (next_row > 0) & (next_column > 0) & (next_row < 9) & (next_column < 9):
        case +=1

print(case)