from cmath import sqrt
import math

def main():
    print(BinaryIntSqrt(274576))
    print(RecursiveSqrt(1, 274576, 274576))


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

def RecursiveSqrt(low, high, n):
    mid = math.floor((low + high) / 2)
    if mid ** 2 <= n and (mid ** 2) + 1 > n:
        return mid
    elif mid ** 2 <= n:
        return RecursiveSqrt(mid, high, n) 
    else:
        return RecursiveSqrt(low, mid, n)


if __name__ == "__main__":
    main()