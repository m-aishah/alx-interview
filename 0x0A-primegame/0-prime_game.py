#!/usr/bin/python3
"""
Prime Game module.
"""


def isWinner(x, nums):
    """
    Determines the winner of a prime game session.

    Args:
        x (int): The number of rounds.
        nums (list): Array of max limits.

    Returns: 'Maria' if Maria will win the game, otherwise 'Ben'.
    """

    # Check that x is a valid number.
    if x < 1 or not nums:
        return None

    # Init Maria & Ben's wins.
    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    n = max(nums)

    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False

    # Filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Return None if they both have the same number of wins.
    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
