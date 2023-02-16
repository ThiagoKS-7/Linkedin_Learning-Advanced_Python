# deque objects are like double-ended queues

from collections import deque
import string


def main():

    # TODO: initialize a deque with lowercase letters
    d = deque(string.ascii_lowercase)
    # TODO: deques support the len() function
    print("item count", str(len(d)))
    # TODO: deques can be iterated over
    for i in d:
        print(i, end=",")
    print()
    # TODO: manipulate items from either end
    d.pop()
    d.append(2)
    d.popleft()
    d.appendleft(1)
    for i in d:
        print(i, end=",")
    print()
    # TODO: rotate the deque
    print(d)
    d.rotate(10)
    print(d)


if __name__ == "__main__":
    main()
