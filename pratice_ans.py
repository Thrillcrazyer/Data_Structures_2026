import ctypes
import time
from functools import wraps

def check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

def isPrimeNumber(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

@check
def getPrimeNumbers(n: int) -> ctypes.Array:
    primes = (ctypes.c_bool*(n+1))()
    for i in range(n+1):
        primes[i] = False
    for i in range(2, n+1):
        if isPrimeNumber(i):
            primes[i] = True
    return primes
    
@check
def sieveOfEratosthenes(n: int) -> ctypes.Array:
    primes = (ctypes.c_bool*(n+1))()
    
    for i in range(n+1):
        primes[i] = True
    primes[0] = primes[1] = False
        
    for k in range(2,n):
        inc=2
        temp = k*inc
        while temp <= n:
            primes[temp] = False
            inc += 1
            temp = k*inc
    return primes



if __name__ == "__main__":
    print("1. Check isPrimeNumber\n")
    
    for num in range(11,20):
        print(f"{num} is Prime Number" if isPrimeNumber(num) else f"{num} is not Prime Number")
    print("\n\n")
    
    print("2. Check sieveOfEratosthenes\n")
    
    A= sieveOfEratosthenes(100)
    for i in range(100):
        if A[i]:
            print(i, end=" ")
    print("\n\n")
    
    print("3. Compare getPrimeNumbers and sieveOfEratosthenes\n")
    n=10000
    list1=getPrimeNumbers(n)
    list2=sieveOfEratosthenes(n)
    
    def test(list1, list2, n):
        for i in range(n):
            if list1[i] != list2[i]:
                print(f"Error at index {i}")
        print("Correct!")
    
    test(list1, list2, n)