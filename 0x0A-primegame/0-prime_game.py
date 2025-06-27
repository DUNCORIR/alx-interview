#!/usr/bin/python3
""" The script simulates Prime Game
Maria and Ben play a game over x rounds. In each round,
they pick primes ≤ n and remove them and their multiples.
The player who cannot make a move loses.
"""


def sieve_with_count(limit):
    """
    Generates a list where index i stores the number of prime numbers ≤ i.
    Uses the Sieve of Eratosthenes to precompute prime numbers efficiently.
    Args:
        limit (int): The maximum number to compute primes up to.
    Returns:
        List[int]: List of prime counts up to each index.
    """
    # Initialize is_prime list:
    # Set index 0 and 1 as not prime, others start as potentially prime
    is_prime = [False, False] + [True] * (limit - 1)
    prime_count = [0] * (limit + 1)
    count = 0

    # Initialize list to store prime counts and a counter
    for i in range(2, limit + 1):
        if is_prime[i]:
            count += 1
            # Mark all multiples of i as not prime
            for j in range(i * 2, limit + 1, i):
                is_prime[j] = False
        # Store the current count of primes up to index i
        prime_count[i] = count

    return prime_count


def isWinner(x, nums):
    """
    Determines the winner of each round of Prime Game.
    Args:
        x: number of rounds
        nums: list of integers, where each is the upper limit of the round
    Returns:
        Name of the player with the most wins ("Maria" or "Ben"), or None
    """
    if not nums or x < 1:
        return None

    # Find the maximum n to precompute primes only once
    max_n = max(nums)
    prime_count = sieve_with_count(max_n)

    # Initialize win counters
    maria_wins = 0
    ben_wins = 0

    # Evaluate each round
    for n in nums:

        # If number of primes ≤ n is odd, Maria wins (she plays first)
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    # Determine who won more rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
