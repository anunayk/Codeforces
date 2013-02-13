#!/usr/bin/python
 
import sys
import math
 
def prime_factorize(n):
    factors = []
    number = math.fabs(n)
 
    while number > 1:
        factor = get_next_prime_factor(number)
        factors.append(factor)
        number /= factor
 
    if n < -1: # If we'd check for < 0, -1 would give us trouble
        factors[0] = -factors[0]
 
    return tuple(factors)
 
def get_next_prime_factor(n):
    if n % 2 == 0:
        return 2
 
    # Not 'good' [also] checking non-prime numbers I guess?
    # But the alternative, creating a list of prime numbers,
    # wouldn't it be more demanding? Process of creating it.
    x = 3
    while (x < int(math.ceil(math.sqrt(n)) + 1)):
        if n % x == 0:
            return x
        x = x + 2
 
    return int(n)
 
def divisors(factors) :
    """
    Generates all divisors, unordered, from the prime factorization.
    """
    ps = sorted(set(factors))
    omega = len(ps)
 
    def rec_gen(n = 0) :
        if n == omega :
            yield 1
        else :
            pows = [1]
            j = 0
                
            while (j < factors.count(ps[n])) :
                pows += [pows[-1] * ps[n]]
                j += 1
            for q in rec_gen(n + 1) :
                for p in pows :
                    yield p * q
 
    for p in rec_gen() :
        yield p
 
def test(x, y):
        x = list(x)
        y = list(y)
        for e in x:
                if e in y:
                        return True
        return False
 
if __name__ == "__main__":
        N = int(raw_input())
        k = divisors(prime_factorize(N))
        temp = []
        for e in k:
                temp.append(e)
        k = temp
        ans = 0
 
        for e in k:
                if (test(str(e), str(N)) == True):
                        ans += 1
        print ans