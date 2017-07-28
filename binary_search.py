# coding: utf-8


def binary_search(card_list, card):
    low = 0
    high = len(card_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = card_list[mid]
        if guess == card:
            print("{0}番目に{1}はあります".format(mid, card))
            return
        elif guess < card:
            low = mid + 1
        else:
            high = mid - 1
    return


if __name__ == '__main__':
    item_list = ['Aaron', 'Bert', 'Carey', 'Daniel', 'Eddie', 'Gilbert', 'Hamilton', 'Jason', 'Louis', 'Mark']
    item = 'Hamilton'
    binary_search(item_list, item)

