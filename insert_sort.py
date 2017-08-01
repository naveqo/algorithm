# coding: utf-8


def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = ele
        return print(arr)


if __name__ == '__main__':
    item_list = ['Eddie', 'Bert', 'Mark', 'Aaron', 'Daniel',  'Gilbert', 'Hamilton', 'Carey', 'Jason', 'Louis']
    insert_sort(item_list)
