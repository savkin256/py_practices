def print_result(element, index):
    if index == -1:
        print("Element", element, "is not in massive")
    else:
        print("Element", element, "has index", index)


def binsearch_recursive(massive, element, first_index, last_index):

    if last_index >= first_index:
        current_index = first_index + int((last_index - first_index) / 2)
        if massive[current_index] == element:
            return current_index
        elif massive[current_index] < element:
            return binsearch_recursive(massive, element, current_index + 1, last_index)
        else:
            return binsearch_recursive(massive, element, first_index, current_index - 1)
    else:
        return -1


def binsearch_iterative(massive, element, first_index, last_index):

    while first_index <= last_index:
        current_index = first_index + int((last_index - first_index) / 2)
        if massive[current_index] == element:
            return current_index
        elif massive[current_index] < element:
            first_index = current_index + 1
        else:
            last_index = current_index - 1
    return -1


def main():

    mass = [1, 3, 10, 27, 35, 45, 47, 97, 97, 98]
    to_find = 35
    print(mass)

    print()

    print("Searching by recursive function:")
    print_result(to_find, binsearch_recursive(mass, to_find, 0, len(mass)-1))

    print()

    print("Searching by iterative function:")
    print_result(to_find, binsearch_iterative(mass, to_find, 0, len(mass)-1))


if __name__ == '__main__':
    main()
