# Script Name: functions.py
# Author: Ben Murphy    Student Number: 119394463


# Question 1



def removeVowels(sentence):
    vowels = "aeiou"
    filtered_list = [l for l in sentence if l not in vowels]
    return filtered_list


# Question 2

def hailStone(n):
    """

    :param n: a positive integer
    :return: the hailstone sequence of the integer
    """
    x = 0
    while x >= 0:
        if x == 0:
            print(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = int(n/2)
            print(n)
            x += 1
            continue
        if n % 2 != 0:
            n = int((3*n) + 1)
            print(n)
        x += 1


def hexToBinary(hex, d):
    """

    :param hex: hex as a string
    :param d: dictionary
    :return: the binary of the hex according to the dictionary
    """
    binary = ""
    for x in hex:
        binary = binary + d[x]

    return binary

def proteins(RNA):
    """

    :param RNA: Rna as string
    :return: the protein that would be created formthe rna
    """
    codon_map = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
                 'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine', 'UCA': 'Serine',
                 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine', 'UGU': 'Cysteine', 'UGC':
                     'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'stop', 'UAG': 'stop', 'UGA': 'stop'}
    protein = []
    hope = []
    for i in range(0, len(RNA), 3):
        codon = RNA[i:i + 3]
        print(codon)
        hope.append(codon)
        if codon_map[codon] == "stop":
            break
        protein. append(codon_map[codon])

    return hope, protein




