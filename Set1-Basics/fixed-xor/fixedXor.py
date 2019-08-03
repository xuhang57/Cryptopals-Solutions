"""
A function that takes two equal-length buffers and produces their XOR
combination.
Inputs are in hex format, output is the hex format
"""

from binascii import hexlify, unhexlify
from Crypto.Util.strxor import strxor


def fixed_xor(num1, num2):
    """
        Convert two equal-length buffers to XOR combination

        : param num1: a hex number in string format
        : param num2: a hex number in string format
        : return: a hex number in string format
        """
    return hexlify(strxor(unhexlify(num1), unhexlify(num2))).decode()


if __name__ == "__main__":
    input_str1 = str(input("Give a hex number: "))
    input_str2 = str(input("Give another hex number: "))
    print(fixed_xor(input_str1, input_str2))
