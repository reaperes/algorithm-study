"""
ref: https://leetcode.com/problems/perfect-number/description/

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:

Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""
from math import sqrt


def check_perfect_number_brute_force(n):
    dividers = []
    for i in range(1, n):
        if n % i is 0:
            dividers.append(i)

    n_clone = n
    for divider in dividers:
        n_clone -= divider

    return n_clone == 0


def check_perfect_number(n):
    if n <= 0:
        return False

    sum_of_dividers = 0
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            sum_of_dividers += i
            if i * i != n:
                sum_of_dividers += n // i

    return sum_of_dividers - n == n


result = check_perfect_number(4)
print(result)