import random

def generate_starting_list(n, min_val, max_val):
    lst = [random.randint(min_val, max_val) for _ in range(n)]
    return lst
