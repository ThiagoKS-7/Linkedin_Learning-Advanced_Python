# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(arg1, arg2, *, supressWarnings=False):
    print(arg1 + arg2)


def main():
    # try to call the function without the keyword
    # myFunction(1, 2, True) # -> throws an exception

    myFunction(1, 2, supressWarnings=True)  # -> throws an exception


if __name__ == "__main__":
    main()
