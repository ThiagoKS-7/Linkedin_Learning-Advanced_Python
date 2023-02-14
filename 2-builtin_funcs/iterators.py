def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
    print(days, daysFr)
    # TODO: use iter to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))

    # TODO: iterate using a function and a sentinel (iter's second parameter)
    with open('2-builtin_funcs/testfile.txt', 'r') as f:
        for line in iter(f.readline, ''):
            print(line)

    # TODO: use regular interation over the days
    for m in days:
        print(m)
    # TODO: using enumerate reduces code and provides a counter
    for i, m in enumerate(days):
        print(f"{i} - {m}")
    # TODO: use zip to combine sequences
    for m in zip(days, daysFr):
        print(m)

    for i, m in enumerate(zip(days, daysFr), start=1):
        print(f"{i} - {m[0]}, {m[1]}")


if __name__ == '__main__':
    main()
