# strings = unicode
# byte são valores 8-bit

def main():
    b = bytes([0x41, 0x42, 0x43, 0x44])
    print(b)

    s = "String example"
    print(s)

    # TODO: Combine them
    print(s + " " + str(b))

    # TODO: Encode/Decode before working on them together
    s2 = b.decode("utf-8")
    print(s + " " + s2)

    b2 = s.encode("utf-8")
    print(b + b2)
    # TODO: Encode the string as UTF-32
    b3 = s.encode("utf-32")
    print(b3)


if __name__ == '__main__':
    main()
