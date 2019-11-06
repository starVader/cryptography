def calculate_xor(buffer1, buffer2):
    buffer1 = bytes.fromhex(buffer1)
    buffer2 = bytes.fromhex(buffer2)
    return bytes([b1 ^ b2 for b1, b2 in zip(buffer1, buffer2)])


if __name__ == '__main__':
    input_str = "1c0111001f010100061a024b53535009181c"
    print(calculate_xor(input_str, "686974207468652062756c6c277320657965"))
