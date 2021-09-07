def mysqrt(x):
    m = 1
    if x == 0:
        return 0
    while m <= x:
        if m * m == x:
            return m
        if m * m >= x:
            return m - 1
        else:
            m = m + 1


def main():
    print(mysqrt(4))
    print(mysqrt(8))
    print(mysqrt(0))
    print(mysqrt(1))
    print(mysqrt(17))


if __name__ == "__main__":
    main()
