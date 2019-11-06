import codecs


def convert_hex_to_base64(hex_data):
    bytes_data = codecs.decode(hex_data, 'hex')
    print(type(bytes_data))
    print(codecs.encode(bytes_data, 'base64').decode())


if __name__ == '__main__':
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    # Output base64_str = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    convert_hex_to_base64(hex_str)
