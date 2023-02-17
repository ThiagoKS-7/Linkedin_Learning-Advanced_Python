# Demonstrate how to use list comprehensions


def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # TODO: Perform a mapping and filter function on a list
    evenSqrd = list(
        map(lambda x: x**2, filter(lambda x: x > 4 and x < 16, evens)))
    print(evenSqrd)
    # TODO: Derive a new list of numbers frm a given list
    evenSqrd = [x ** 2 for x in evens]
    print(evenSqrd)

    # TODO: Limit the items operated on with a predicate condition
    oddsSqrd = [x ** 2 for x in odds if x > 4 and x < 16]
    print(oddsSqrd)


if __name__ == "__main__":
    main()
