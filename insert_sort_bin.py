import sys
sys.setrecursionlimit(10 ** 7)


def binary_search(arr, low, hig, ele):
    if low == hig:
        if arr[low] > ele:
            return low
        else:
            return low + 1
    elif low > hig:
        return low

    mid = (low + hig) // 2
    if arr[mid] < ele:
        return binary_search(arr, mid + 1, hig, ele)
    elif arr[mid] > ele:
        return binary_search(arr, low, mid - 1, ele)
    else:
        return mid


def insert_sort_bin(arr):
    for i in range(1, len(arr)):
        ele = arr[i]
        ind = binary_search(arr, 0, i - 1, ele)
        arr[:] = arr[:ind] + [ele] + arr[ind:i] + arr[i + 1:]
    return print(arr)


if __name__ == '__main__':
    item_list = ['Eddie', 'Bert', 'Mark', 'Aaron', 'Daniel',  'Gilbert', 'Hamilton', 'Carey', 'Jason', 'Louis']
    insert_sort_bin(item_list)
