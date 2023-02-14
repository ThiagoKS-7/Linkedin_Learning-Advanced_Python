# advanced iteration functions in the itertools package
import itertools


def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    # islice turns cycle into a sequence, given a batch size
    print(list(itertools.islice(cycle1, 5)))

    # TODO: use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(list(itertools.islice(count1, 5)))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    acc = itertools.accumulate(vals)
    print(list(acc))

    # TODO: use chain to connect sequences together
    x = itertools.chain("ABC", "1234")
    print(list(x))

    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    # OBS: Bom pra dividir coisas
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))


if __name__ == "__main__":
    main()
