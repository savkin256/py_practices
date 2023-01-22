from random import randint
import copy


def generate_massive(count):
    return[randint(0, 99) for i in range(count)]


def bubble_sort(unsorted_massive):
    a = copy.deepcopy(unsorted_massive)
    n = len(a)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def merge_sort(unsorted_massive):
    a = copy.deepcopy(unsorted_massive)
    if len(a) < 2:
        return a
    else:
        median = int(len(a) / 2)
        left = merge_sort(a[:median])
        right = merge_sort(a[median:])
        return merge(left, right)


def merge(left_side, right_side):
    res = []
    i = 0
    j = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] < right_side[j]:
            res.append(left_side[i])
            i += 1
        else:
            res.append(right_side[j])
            j += 1
    while i < len(left_side):
        res.append(left_side[i])
        i += 1
    while j < len(right_side):
        res.append(right_side[j])
        j += 1
    return res


def insert_sort(unsorted_massive):
    a = copy.deepcopy(unsorted_massive)
    for j in range(2, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


def main():
    mass = generate_massive(10)

    print(mass)
    print(bubble_sort(mass), "\n")

    print(mass)
    print(merge_sort(mass), "\n")

    print(mass)
    print(insert_sort(mass), "\n")


if __name__ == '__main__':
    main()
