import os
import random
import struct

"""Generates the urandom code based on size specified"""


def generatePRNG(size, fileName):
    with open('test/' + fileName + '.dat', 'wb') as f:
        f.write(os.urandom(size))
    return "Successfully created urandom file"


def generateFRNG(size, period, fileName):
    sequence = []
    key = []
    random.seed(key)
    c = 0
    for i in range(0, int(size / period)):
        for j in range(0, period):
            temp = random.randint(0, 255)
            if temp == key[c]:
                while temp == key[c]:
                    temp = random.randint(0, 255)
            sequence.append(temp)
    if c >= len(key) - 1:
        c = 0
    else:
        c += 1
    with open('test/' + fileName + '.dat', 'wb') as f:
        f.write(sequence)
    return "Successfully created tampered test sequence file"


type = input("Specify what type of data: (1) Pseudo Random Data (2) tampered test sequence: ")
type = int(type)
size = input("Size of Urandom file: ")
size = int(size)
fileName = input("Name of file: ")
if type == 1:
    print(generatePRNG(size, fileName))
elif type == 2:
    period = input("Enter period")
    print(generateFRNG(size, period, fileName))
