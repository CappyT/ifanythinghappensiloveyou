import secrets
import string
import numpy as np
from functools import partial
import argparse


def generate_key(file):
    randint = np.random.randint
    pick_char = partial(secrets.choice, string.ascii_uppercase + string.digits + string.ascii_lowercase)
    key = (''.join([pick_char() for _ in range(randint(24, 40))]))
    with open(str(file), 'a') as key_file:
        key_file.write(key)
        key_file.close()
    print(key)


def decode_key(file):
    try:
        with open(file, 'rb') as key_file:
            key = key_file.read().split(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x09\xff')[1].decode('utf-8')
        print(key)
    except Exception as e:
        print('Cannot decode file: ' + str(e))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='main.py')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--gen', help='Generate a key', action='store_true')
    group.add_argument('--decode', help='Decode file', action='store_true')
    parser.add_argument('file')
    args = parser.parse_args()
    if args.gen:
        generate_key(args.file)
    if args.decode:
        decode_key(args.file)
    else:
        print('No action specified. Use --help for usage.')
