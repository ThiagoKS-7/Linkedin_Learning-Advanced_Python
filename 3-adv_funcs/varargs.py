def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result


def main():
    print(add(2, 6, 8, 12))
    print(add(7567, 8, 678))
    list = [1, 2, 344, 56]
    print(add(*list))


if __name__ == '__main__':
    main()
