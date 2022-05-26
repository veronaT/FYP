import os
import random
import struct

"""Generates the urandom code based on size specified"""


def generatePRNG(size, fileName):
    with open('test/' + fileName + '.dat', 'wb') as f:
        f.write(os.urandom(size))
    f.close()
    return "Successfully created urandom file"


def generateFRNG(size, amount):
    p = 0  # probability of the switch flipping
    urand = 0  # random var used to determine whether switch flips in conjunction with p
    value = 0  # a byte generated and potentially appended to the sequence
    fname = "tamperTestData"

    for a in range(0, amount):
        filename = 'test/'+fname + str(a)

        for i in range(1, amount):
            p = i / 100
            f = open(filename + "_" + ".bin", 'wb')
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


type = input("Specify what type of data: (1) Pseudo Random Data (2) tampered test sequence: ")
type = int(type)
size = input("Size of Urandom file: ")
size = int(size)
amount = input("Amount of files: ")
amount = int(amount)

if type == 1:
    fileName = input("Name of file: ")
    print(generatePRNG(size, fileName))
elif type == 2:
    print(generateFRNG(size, amount))
