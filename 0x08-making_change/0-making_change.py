#!/usr/bin/python3
"""" Script to calculate the fewest number of coins needed
for a given amount using a set of coin denominations.
"""


def makeChange(coins, total):
    """
    Calculate the number of coins needed to make change.
    Args:
        coins (list): List of coin denominations.
        total (int): The total amount to make change from
                     using the given denominations.

    Returns:
        int: The number of ways to make change for the total amount.
    """
    # Check if the total is less than or equal to zero
    if total <= 0:
        return 0
    # Initialize a list to store the minimum number of coins.
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make change for 0 amount
    for i in range(1, total + 1):
        # Iterate through each coin denomination
        for coin in coins:
            if i - coin >= 0:  # Check if the coin can be used
                # Update the dp array with the minimum coins needed
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # End of the loop through coins
    return dp[total] if dp[total] != float('inf') else -1
