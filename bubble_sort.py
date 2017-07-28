# coding: utf-8


def bubble_sort(arr):
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return print(arr)

if __name__ == '__main__':
    item_list = ['Eddie', 'Bert', 'Mark', 'Aaron', 'Daniel',  'Gilbert', 'Hamilton', 'Carey', 'Jason', 'Louis']
    bubble_sort(item_list)
