# coding: utf-8


import bisect


def insert_sort_bin_with_bisect(arr):
    for i in range(1, len(arr)):
        bisect.insort(arr, arr.pop(i), 0, i)
    return print(arr)


if __name__ == '__main__':
    item_list = ['Eddie', 'Bert', 'Mark', 'Aaron', 'Daniel',  'Gilbert', 'Hamilton', 'Carey', 'Jason', 'Louis']
    insert_sort_bin_with_bisect(item_list)
