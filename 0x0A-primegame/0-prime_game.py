#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """
    Function to check game winner
    """
    prayer = {"Maria": 0, "Ben": 0}
    # print(x)
    for i in range(0, x):
        # print(i)
        arr_prime = generate_prime_array(nums[i])
        # print(arr_prime)
        if (len(arr_prime) == 0):
            prayer["Ben"] += 1
        else:
            if (len(arr_prime) % 2 == 0):
                prayer["Ben"] += 1
            else:
                prayer["Maria"] += 1

    if (prayer["Maria"] > prayer["Ben"]):
        return "Maria"
    elif (prayer["Ben"] > prayer["Maria"]):
        return "Ben"
    else:
        return None


def generate_prime_array(n):
    """To generate sequence n of prime numbers
    """

    prime_arr = []
    for i in range(1, n + 1):
        if (is_prime(i)):
            prime_arr.append(i)

    return prime_arr


def is_prime(number):
    """check if a number is prime
    """

    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
