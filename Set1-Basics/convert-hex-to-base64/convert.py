"""
Convert a hex number to a base64 number
Crytopal Rule: Always operate on raw bytes, never on encoded strings.
Only use hex and base64 for pretty-printing.
"""

import base64


def convert_hex_to_base64(hex_str):
    """
        Convert a hex number in string format to base64.

        :param hex_str: a hex number in string format.
        :return: a base64 number in string format.
        """
    # first, convert hex number to raw bytes, and from raw bytes,
    # we convert it to a base64 format number in string format
    return base64.b64encode(bytes.fromhex(hex_str)).decode("utf-8")


if __name__ == "__main__":
    input_str = str(input("Give a hex number: "))
    print(convert_hex_to_base64(input_str))
