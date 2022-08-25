def choice_sort(arr):
    min_idx = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i):
            if arr[min_idx+i] > arr[i+j]:
                arr[min_idx+i], arr[i+j] = arr[i+j], arr[min_idx+i]
        min_idx = 0
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


lst = list(map(int, input().split()))
print(*bubble_sort(lst))


#merge sort

def merge(left, right):
    temp = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    if i < len(left):
        temp.extend(left[i:])
    if j < len(right):
        temp.extend(right[j:])

    return temp


def merge_sort(s, a=[]):
    if len(s) < 2:
        return s
    else:
        L, R = s[:len(s)//2], s[len(s)//2:]
        L = merge_sort(L)
        R = merge_sort(R)
        return merge(L, R)


lst = list(map(int, input().split()))
print(*merge_sort(lst))

