# Script Name: functions.py
# Author: Ben Murphy    Student Number: 119394463

# Question 1
def chooseLargest (a, b):
    """

    :param a:a list containing integers
    :param b:a list containing integers
    :return:a list that contains the highest number for each index
    """
    result = []
    #lambda gets the range of the length of the first list for the for loop
    for i in lambda c: range(len(c)), a:
        # this gets the zip of the two lists then map uses the max function on the zip to map it to the list which is then appended to the empty list
        result.append(list(map(max, zip(a, b))))
    return result[1]

    # List comprehension version
    # result = [list(map(max, zip(a, b))) for i in (lambda c: range(len(c)), a)]
    # return result[1]

# Question 2
def read_draw():
    """

    :return:
    """
    lotterydraws = []
    draws = []
    infile = open("lotteryNumbers.txt", "r")
    info = infile.readlines()
    for i in info:
        i = i.strip("\n")
        # appends the data to a list where each draw is at a certain index
        draws.append(i)
    x = 0
    # while loop is for converting the draws to their own list and to make the string into separate integers
    while x < len(draws):
        r = []
        # This loop goes in threes to avoid the empty space and the appends the integer of the 2 numbers that appear
        for i in range(0, len(draws[x]), 3):
            numbers = draws[x][i:i+2]
            r.append(int(numbers))
        # this list is then appended to the final list in order to create each draw in a separate list
        lotterydraws.append(r)
        x += 1
    infile.close()
    return lotterydraws



# Question 3


def del_1000(courierData):
    """

    :param courierData:A matrix containing the data of how many deliveries each driver made each day
    :return:the number of weekdays the employees collectively walked more than 100000
    """
    num_of_days = 0
    y = 0
    while y < len(courierData[0]):
        x = 0
        deliveries = 0
        # the y is which column and x is which row, This causes it to go through all the rows at a particular column
        while x < len(courierData):
            # This will add the number of deliveries on a particular day together
            deliveries += courierData[x][y]

            x += 1
        # if there ae more or equal to 1000 deliveries on a particular day it will add 1 to the counter for the days
        if deliveries >= 1000:
            num_of_days += 1

        y += 1

    return num_of_days


def most_del(courierData):
    """

    :param courierData: A matrix containing the data of how many deliveries each driver made each day
    :return:
    """
    x = 0
    while x < len(courierData):
        y = 0
        deliveries = 0
        # this loop causes it to go through all the columns in a row and add them together
        while y < len(courierData[x]):
            deliveries += courierData[x][y]

            y += 1
        # if it is the first driver there deliveries will be the most as it is the first time it goes through
        if x == 0:
            driver = x
            driver_deliveries = deliveries
            x += 1
            continue
        # compares the next driver to the driver with the previous most deliveries and if the had more they get stored
        if driver_deliveries < deliveries:
            driver = x
            driver_deliveries = deliveries

        x += 1

    return driver


# Question 4


def append_list():
    list1 = [1, 2, 3]
    list2 = [10, 20, 30]
    totals = []
    for tup in zip(list1, list2):
        totals += (list(map(lambda a, b: int(a) + int(b), [tup[0]], [tup[1]])))

    return totals

# Question 5
def check_match(d,name):
    """

    :param d: the dictionary containing the clients
    :param name: the name of the clien you are looking for the matches of
    :return: a list of matches for the client
    """
    match = []
    look = d[name.lower()][2:5]
    for first in d.keys():
        if name.lower() == first:
            continue
        elif look[0] == d[first][0]:
            if look[1] <= d[first][1] <= look[2]:
                match.append(first)
    return match


def client_matcher():
    """

    :return:
    """
    clients = {}
    file = open("clients.txt", "r")
    info = file.readlines()
    for i in info:
        i = i.strip("\n").split(",")
        print(i)
        clients[i[0].lower()] = i[1:]
        print(clients)

    file.close()
    return check_match(clients, "Peter Jackson")


print(client_matcher())
