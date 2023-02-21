"""
Challenge Nº3 by MoureDev - IS PRIME?
"""

#Prime numbers are numbers that have only 2 factors: 1 and themselves.
#For example, the first 5 prime numbers are 2, 3, 5, 7, and 11.
#By contrast, numbers with more than 2 factors are call composite numbers.

def is_prime():
    for i in range(1, 101):

        if i >= 2:

            is_divisible = False

            for j in range(2, i):
                if i % j == 0:
                    is_divisible = True
                    break
            
            if not is_divisible:
                print(i)

is_prime()
