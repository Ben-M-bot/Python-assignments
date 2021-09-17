# Script Name: functions.py
# Author: Ben Murphy  Student Number: 119394463

# Question 1
def fractions(DNA):
    """

    :param: String
    :return:the fraction of how many times C G T A appear in that order
    """
    c = 0
    t = 0
    g = 0
    a = 0
    if type(DNA) is str:
        # this loop goes through the string,if it matches with one of the if statements will add 1 to different counters
        for f in DNA:
            if f == "C":
                c += 1
            elif f == "T":
                t += 1
            elif f == "G":
                g += 1
            elif f == "A":
                a += 1
        # Used to get the fraction of how many times the particular string appears
        max_Dna = a + c + t + g
        # if it equals 0 then the characters didn't appear in the string and get returned in a tuple
        if max_Dna != 0:
            # the amount of times the character appears divided by the total characters gives the fraction
            result = (c/max_Dna, g/max_Dna, t/max_Dna, a/max_Dna)
        else:
            result = (float(c), float(g), float(t), float(a))
        return result
    else:
        return "input must be a string character"


# Question 2

def F(S1, S2):
    R = []
    for e1 in S1:
        for e2 in S2:
            if e1 == e2:
                R += [e1]
                break
    return R


def F_while(S1, S2):
    """

    :param S1: either string or a list
    :param S2: either string or a list
    :return: a list of the common occurrences
    """
    R = []
    x = 0
    while x < len(S1):
        y = 0
        while y < len(S2):
            if S1[x] == S2[y]:
                R += [S1[x]]
                break
            y += 1
        x += 1
    return R



def F_list_comp(S1, S2):
    """

    :param S1: either string or a list
    :param S2: either string or a list
    :return:a list of the common occurrences
    """
    R = [e1 for e1 in S1 for e2 in S2 if e1 == e2]
    return R



def F_lambda(S1, S2):
    """

    :param S1: either string or a list
    :param S2: either string or a list
    :return:a list of the common occurrences
    """
    d = []
    R = []
    for e1 in S1:
        for e2 in S2:
            # the result of the lamda will get added to the empty list
            d += list(map(lambda a, b: a if a == b else False, [e1], [e2]))
    # Goes through the list d, it will be either a False or answer to be appended, the if will check if is False or not
    for y in d:
        if y:
            R += [y]
    return R


def F_error(S1, S2):
    """

    :param S1:As long as its not a dictionary it might/should work
    :param S2:As long as its not a dictionary it might/should work
    :return: a list of the common occurrences
    """

    R = []

    S3 = list(str(S1))
    S4 = list(str(S2))
    for e1 in S3:
        for e2 in S4:
            if e1 == e2:
                if type(S1) == int and type(S2) == int:
                    R += [int(e1)]
                elif type(S1) == int and type(S2) == str or type(S1) == str and type(S2):
                    R += e1
                break
    return R


# Question 3
def frequencies(s):
    """

    :param s:the input as string
    :return:
    """
    diction = {}
    for k in s:
        # If k isn't in the keys in the dictionary it will create a key with the value of 1 and skip the rest
        if k not in diction.keys():
            diction[k] = 1
            continue
        # if k is in the keys of the dictionary then it will increase the value of it by 1 to get the frequency
        if k in diction.keys():
            diction[k] += 1
    return diction


# Question 4

def firsts(s):
    """

    :param s: your input
    :return: what you inputted but it will remove the repeated values
    """
    result = ""
    s = str(s)
    for l in s:
        # the first time it goes through it will concatenate l since it has to be the first occurrence
        if result == "":
            result += l
        # this stops it from repeating the same character in the result
        if l in result:
            continue
        else:
            result += l
    return result


# Question 5
text = "gather around yearly"
def extract(text, n, m):
    """

    :param text: the passage you are trying to extract the message
    :param n: the letter in each word to be extracted
    :param m: the mth word that the letters will be extracted from
    :return:the word that the letters spell out
    """
    code = ""
    space = 0
    c = 0
    for letter in text:
        # the first time i have deal with a specific circumstance so the if is there
        if code == "":
            # this if and counter are used to tell how many words have been passed
            if letter == " ":
                space += 1
            # the first time will have 1 less space than the others as the first word will not start after a space
            if space == m-1:
                x = 0
                # used for the slicing to take the mth word out for the error message
                start = c
                while c < len(text):
                    if x == n:
                        # if the index c is an space character then the word is too short and causes an error
                        if text[c] == " ":
                            # word is the word that there is not enough characters in
                            word = text[start:c]
                            return "there is no character " + str(n) + " in " + word
                        # adds the charter to the code and breaks out of the loop
                        code += text[c]
                        break
                    # standard counters for while loops
                    x += 1
                    c += 1
                    # this checks if the word ends before the character is added to the code
                    if text[c] == " ":
                        word = text[start:c]
                        return "there is no character " + str(n) + " in " + word
                #  resets the counter for the words to 0 and c back to what it was before the while loop
                space = 0
                c -= x
            c += 1
        else:
            # every other time the code will go through the else that effectively looks the same with only 1 difference
            if letter == " ":
                space += 1
            # if space if equal to m instead of m - 1 as it is not the start of the passage
            if space == m:
                x = 0
                start = c
                while c < len(text):
                    if x == n:
                        if text[c] == " ":
                            word = text[start:c]
                            return "there is no character " + str(n) + " in " + word
                        code += text[c]
                        break
                    x += 1
                    c += 1
                    if text[c] == " ":
                        word = text[start:c]
                        return "there is no character " + str(n) + " in " + word
                space = 0
                c -= x
            c += 1
    return code

print(extract(text , 1, 1))