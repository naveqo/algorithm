# coding: utf-8


def select_sort(arr):
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        print(min_ind)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return print(arr)


if __name__ == '__main__':
    item_list = ['Eddie', 'Bert', 'Mark', 'Aaron', 'Daniel',  'Gilbert', 'Hamilton', 'Carey', 'Jason', 'Louis']
    select_sort(item_list)
