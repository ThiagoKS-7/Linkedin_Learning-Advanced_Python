# Demonstrate the use of function docstrings
# https://peps.python.org/pep-0257/

def myFunction(arg1, arg2=None) -> None:
    """myFunction(arg1, arg2=None) -> None:

    Docstring test function
    More info: https://peps.python.org/pep-0257/

    arg1: any;
    arg2: any, default to None;
    """

    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
