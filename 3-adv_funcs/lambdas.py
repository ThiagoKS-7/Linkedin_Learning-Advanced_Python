# Use lambdas as in-place functions
# lambda (parameters) : expression

def CelsisusToFahrenheit(temp):
    return (temp * 9/5) + 32


def FahrenheitToCelsisus(temp):
    return (temp-32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]
    # É uma lista, a função é pra cada item
    # logo, precisa criar uma lista nova, usando essa func pra cada item
    # Ou seja, tu usa o map pra criar a instancia e o list pra conseguir ler
    # ao inves de fazer um for com append numa lista vazia

    # TODO: Use regular functions to convert temps
    print(list(map(CelsisusToFahrenheit, ctemps)))
    print(list(map(FahrenheitToCelsisus, ftemps)))

    # TODO: Use lambdas to accomplish the same thing
    print(list(map(lambda x: (x * 9/5) + 32, ctemps)))
    print(list(map(lambda x: (x-32) * 5/9, ftemps)))


if __name__ == "__main__":
    main()
