from ctypes import sizeof


def main():
    s = [1,2,3,4,5]
    print(maxIterative(s))
    print(maxRecursive(s))


def maxIterative(s):
    max = s[0]
    for i in range(2, len(s)):
        if s[i] > max:
            max = s[i]
    return max

def maxRecursive(s):
    max = s[0]


if __name__ == "__main__":
    main()