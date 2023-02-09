from decimal import Decimal
from fractions import Fraction


def leitura_arquivo(name=str):
    f = open(name, "r")
    if f.mode == 'r':
        return f.read()
    f.close()


class MyClass:
    def __bool__(self):
        return False

    def __len__(self):
        return 0


def main():
    print("TRUTH VALUES\n")
    mc = MyClass()
    data = {
        "bool_vl": [False, bool(None)],
        "num_vals": [bool(0), bool(0.0), bool(0j)],
        "dec_frac": [bool(Decimal(0)), bool(Fraction(0, 1))],
        "empty_seq/coll": [bool(()), bool([]), bool({})],
        "empty_sets/ranges": [bool(set()), bool(range(0))],
        "class_params": [bool(mc), len(mc)],
    }
    for key in data.keys():
        print(f"{key} - {data[key]}")


if __name__ == '__main__':
    main()
