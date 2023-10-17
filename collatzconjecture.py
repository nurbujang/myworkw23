# The task is to verify, using Python, that the Collatz conjecture is true for the first 10000 positive integers.

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def verify_collatz_conjecture(limit):
    for n in range(1, limit + 1):
        sequence = collatz_sequence(n)
        if sequence[-1] != 1:
            print(f"Collatz conjecture is not true for n = {n}")
            return
    print("Collatz conjecture is true for all integers up to", limit)

verify_collatz_conjecture(10000)