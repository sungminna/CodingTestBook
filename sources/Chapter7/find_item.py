def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n = input()
data = list(map(int, input().split()))
data.sort()

m = input()
data_find = list(map(int, input().split()))

for i, item in enumerate(data_find):
    res = binary_search(data, item, 0, n-1)
    if(res == None):
        print('no ')
    else:
        print('yes ')