import random


def random_float(low, high, digits=1):
    return round(random.uniform(low, high), digits)


def random_int(low, high):
    return random.randint(low, high)