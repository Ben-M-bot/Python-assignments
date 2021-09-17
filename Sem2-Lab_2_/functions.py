

# Script Name: functions.py
# Author: Ben Murphy    Student Number: 119394463


# Question 1

def power():
    """

    :return:
    """

    powers = [i*i for i in range(1,6) if i % 2 == 0]
    return powers



# Question 2

def F(s1, s2):
    """

    :param s1:
    :param s2:
    :return:
    """
    r = []
    c = 0
    while c < len(s1):
        s = 0
        while s < len(s2):
            if s1[c] == s2[s]:
                r.append(s1[c])
                break
            s += 1
        c += 1
    return r

# Question 3

def reducedFeeEntitlement(d):
    """

    :param d:Dictionary containing student ids as keys and a list of modules that they take
    :return: students who have two or less modules
    """
    reduced = []
    for key in d:
        if len(d[key]) <= 2:
            reduced.append(key)

    return reduced

#print(reducedFeeEntitlement(d = {"1145748": ["CS1103", "CS1111", "CS1117", "FR1107"], "1141234": ["FR1211", "FR1001", "FR1107"],
         #"1145801": ["CS1111", "CS1107", "CS1115", "CS1110"],
         #"1146571": ["DS2321", "DS4067"], "1149989": ["GR1231", "FR1107"]}))


def commonModules(d, s1, s2):
    """

    :param d: Dictionary containing student ids as keys and a list of modules that they take
    :param s1: A student id
    :param s2: A different student id
    :return:a list of modules that the two students have in common
    """
    common = []
    one = d[s1]
    two = d[s2]
    c = 0
    while c < len(one):
        s = 0
        while s < len(two):
            if one[c] == two[s]:
                common.append(one[c])
                break
            s += 1
        c += 1
    return common

# Question 4

def  iter_factorial(n):
    """

    :param n:
    :return:
    """
    f = n

    while n > 0:
        if n - 1 == 0:
            break
        f = f * (n - 1)

        n = n - 1

    return f

# Question 5

def fizz_buzz():
    """

    :return:
    """
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz")

        elif n % 3 == 0:
            print("Fizz")

        elif n % 5 == 0:
            print("Buzz")

        else:
            print(n)

