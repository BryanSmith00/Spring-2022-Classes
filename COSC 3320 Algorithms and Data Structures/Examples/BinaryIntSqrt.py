from cmath import sqrt
import math

def main():
    print(BinaryIntSqrt(274576))
    print(RecursiveSqrt(274576))


def BinaryIntSqrt(n):
    low = 1
    high = n

    while True:
        mid = math.floor((low + high) / 2)
        if mid**2 <= n and (mid+1)**2 > n:
            return mid
        elif mid**2 < n:
            low = mid
        else:
            high = mid

def RecursiveSqrt(n):
    print()

if __name__ == "__main__":
    main()