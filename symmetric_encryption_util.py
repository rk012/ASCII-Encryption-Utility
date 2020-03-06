from primes import PRIMES
import random

GENERATOR=3
MODULUS=PRIMES[356]
PRIVATE_KEY=random.randint(1, 1000)

PUBLIC_KEY=(GENERATOR**PRIVATE_KEY)%MODULUS

def key_gen(public_key):
    global PRIVATE_KEY, MODULUS
    return (int(public_key)**PRIVATE_KEY)%MODULUS
