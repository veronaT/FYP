import os
import random
import struct

"""Generates the urandom code based on size specified"""


def generatePRNG(size, fileName, amount):
    for i in range(amount):
        with open('data/prng/' + fileName + str(i) + '.dat', 'wb') as f:
            f.write(os.urandom(size))
        f.close()
    return "Successfully created urandom file"


def generateFRNG(size, fileName, amount):
    p = 0  # probability of the switch flipping
    urand = 0  # random var used to determine whether switch flips in conjunction with p
    value = 0  # a byte generated and potentially appended to the sequence
    fname = "tamperTestData"

    for a in range(0, amount):

        for i in range(1, amount):
            p = i / 100
            f = open('data/frng/' + fileName + str(i) + '.dat', 'wb')
            for j in range(0, size):
                urand = random.uniform(0.00, 1.00)

                if (urand <= p):
                    temp = int.from_bytes(os.urandom(1), byteorder='little')
                    while temp == 255:
                        temp = int.from_bytes(os.urandom(1), byteorder='little')
                    value = temp
                else:
                    value = int.from_bytes(os.urandom(1), byteorder='little')

                f.write(bytes([value]))
            f.close()
    return "Successfully created tampered test sequence file"

def generateNRNG(size, fileName, amount):
    size = int(size / 1000) #amount divided up is set for large files
    for i in range(amount):
        with open('data/nrng/' + fileName + str(i) + '.dat', 'wb') as f:
            first = os.urandom(size)
            second = os.urandom(size)
            for i in range (500):
                f.write(first)
                f.write(second)
        f.close()
    return "Successfully created non-random file"


type = input("Specify what type of data: (1) Pseudo Random Data (2) tampered test sequence (3) non-random data: ")
type = int(type)
size = input("Size of file: ")
size = int(size)
amount = input("Amount of files: ")
amount = int(amount)
fileName = input("Name of file: ")

if type == 1:
    print(generatePRNG(size, fileName, amount))
elif type == 2:
    print(generateFRNG(size, fileName, amount))
elif type ==3:
    print(generateNRNG(size, fileName, amount))
