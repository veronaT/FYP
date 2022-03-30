import os
import struct

"""Generates the urandom code based on size specified"""


def generate(size):
    result = os.urandom(size)
    print(result)
    return result


"""writes urandom results into new .dat file each time it's run"""


def write(result):
    file = "test/file.dat"
    with open(file, 'wb') as data_file:
        data_file.write(struct.pack('i' * len(result), *result))
    return "Successfully created urandom file"


size = input("Size of Urandom file: ")
size = int(size)
result = generate(size)
print(write(result))
