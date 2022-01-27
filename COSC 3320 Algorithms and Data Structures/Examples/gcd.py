def main():
    a = 1002395010
    b = 2405030405
    print(gcd(a,b))

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


if __name__ == "__main__":
    main()