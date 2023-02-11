
def show_utils(list: list, value=None) -> any:
    # TODO: any() return True if any of the sequence values are True
    # TODO: all() return True if all of the sequence values are True
    # TODO: any() return True if any of the sequence values are True
    # TODO: sum() return the sum of all sequence values
    utils = [
        any(list),
        all(list),
        min(list),
        max(list),
        sum(list)
    ]
    for util in utils:
        print(util)


def main():
    list1 = [1, 2, 3, 0, 5, 6]

    show_utils(list1)


if __name__ == '__main__':
    main()
