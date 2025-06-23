# 0x0A. Prime Game

## Description

This project involves designing an algorithm to determine the winner of a competitive game based on prime numbers. Two players take turns selecting prime numbers from a list of consecutive integers and removing the chosen prime along with all of its multiples. The player unable to make a move loses. The winner is determined based on optimal play using principles of number theory and game theory.

The objective is to determine the overall winner after playing multiple rounds of the game.

---

## Learning Objectives

- Understand prime numbers and how to efficiently compute them using the Sieve of Eratosthenes.
- Apply game theory to predict outcomes of competitive turn-based games.
- Optimize algorithms using memoization and precomputation.
- Use Python for implementing and analyzing algorithmic challenges.

---

## Function Prototype

```python
def isWinner(x, nums):
    """
    Determines the winner of a series of Prime Games.

    Parameters:
    - x (int): Number of rounds.
    - nums (list of int): List of integers representing the upper limit of numbers for each round.

    Returns:
    - str: "Maria" if Maria wins more rounds, "Ben" if Ben wins more rounds, or None for a tie.
    """

Rules of the Game
A list of numbers from 1 to n is created.

Players take turns choosing a prime number p from the list and remove all multiples of p.

The first player is "Maria", the second is "Ben".

The player who cannot make a move loses the round.

The winner is the one who wins the most rounds out of x.

Example
python

isWinner(3, [4, 5, 1])
Round 1 (n=4): Maria wins

Round 2 (n=5): Ben wins

Round 3 (n=1): Ben wins

=> Output: "Ben"

Requirements
All code files are interpreted using Python 3.4.3

All code follows PEP 8 style (version 1.7.x)

All scripts start with #!/usr/bin/python3

All files must be executable

No global variables

Must handle edge cases and invalid inputs gracefully

Files
0-prime_game.py: Contains the core algorithm for determining the game winner.

main.py: Sample test cases to verify implementation.

README.md: Project documentation.

Compilation & Execution
Make scripts executable:

bash

chmod +x 0-prime_game.py main.py
Run test file:

bash

./main.py
Author
Duncan Korir