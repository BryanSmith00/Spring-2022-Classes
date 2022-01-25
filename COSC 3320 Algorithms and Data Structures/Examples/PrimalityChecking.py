from math import *
import time

def main():
    start = time.time()
    numPrime = 0

    for i in range(2, 100000):
        x = isPrime(i)
        if(x == True):
            print(i,"is prime")
            numPrime = numPrime + 1

    print("Number of primes from 2 to 100,000:",numPrime)
    end = time.time()
    print(end - start)


def isPrime(n):
    for i in range(2,int(sqrt(n)) + 1):
        if(n%i == 0):
            return False
    return True

if __name__ == "__main__":
    main()