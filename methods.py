import requests
import timeit
import random
import secrets
import os
import numpy


# DIFFERENT METHODS OF OBTAINING RANDOM or "RANDOM" NUMBERS

# Method 1 - uses REAL randomness that comes from atmospheric noise, is VERY slow (uses api).
def real_random_number():
    real_num = []
    for i in range(10):
        response = requests.get("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new") # Generates a truly random number
        real_num.append(int(response.text.strip())) # Appends the random number
    print(real_num)
# Method 2 - using 'random' package, pseudorandom, very fast
def pseudo_random_number():
    pseudo_num = []
    for i in range(10):
        pseudo_num.append(random.randint(1, 100)) # Generates & appends a pseudo-random number
    print(pseudo_num)
# Method 3 - cryptographically secured pseudo-randomness,
def encrypted_random_number():
    encrypted_num = []
    for i in range(10):
        encrypted_num.append(secrets.randbelow(100)) # Generates a cryptographically secure number
    print(encrypted_num)
# Method 4 - system level generated pseudo-randomness, very close to true randomness as it utilizes the unpredictable system data.
def system_random_number():
    system_num = []
    for i in range(10):
        random_bytes = os.urandom(4)
        random_int = int.from_bytes(random_bytes, "big")
        system_num.append(random_int % 100)
    print(system_num)
# Method 5 - using a precomputed pool, almost instant
RANDOM_POOL = [random.randint(1, 100) for i in range(1000)]
def precomputed_random_number():
    precomputed_num = []
    for i in range(10):
        precomputed_num.append(RANDOM_POOL[-1])
        RANDOM_POOL.pop()
    print(precomputed_num)
# Method 6 - using numpy, much faster than the traditional 'random' package
def numpy_random_number():
    numpy_num = [numpy.random.randint(1, 101, size=10)]
    print(numpy_num)

real_gen, pseudo_gen, encrypted_gen, system_gen, precomputed_gen, numpy_gen = timeit.timeit(real_random_number, number=1), timeit.timeit(pseudo_random_number, number=1), timeit.timeit(encrypted_random_number, number=1), timeit.timeit(system_random_number, number=1), timeit.timeit(precomputed_random_number, number=1), timeit.timeit(numpy_random_number, number=1)
print(f'\nPERFORMANCE:\nReal random number gen: {real_gen}s \nPseudo random number gen: {pseudo_gen}s\nEncrypted pseudo-random gen: {encrypted_gen}s\nSystem pseudo-random gne: {system_gen}s\nPrecomputed pseudo-random gen: {precomputed_gen}s\nNumpy pseudo-random gen: {numpy_gen}s')
