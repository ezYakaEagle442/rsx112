#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RC4, AES ECB/CBC/CTR implementation

Run with command-line argument "-h" to display the online help.
This program uses the python3 cryptography library
which is now installed by default on Ubuntu 22.04 for example.

Nicolas Pioch, 23 Oct 2022
"""

import sys
import argparse

try:
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
except ModuleNotFoundError:
    sys.exit("Failed to load the cryptography module: install the python3-cryptography package.")


def main():
    parser = argparse.ArgumentParser(
        description='Encrypt or decrypt a file')
    parser.add_argument('-d', '--debug',
                        help='Enable debug diagnostics',
                        action='store_true')
    parser.add_argument('-s', '--skipbytes',
                        help='Number of bytes to copy unmodified (default: 0)',
                        type=int, default=0)
    parser.add_argument('-c', '--cipher',
                        help='Cipher to use',
                        required=True,
                        choices=['rc4', 'aes-ecb', 'aes-cbc', 'aes-ctr'])
    parser.add_argument('--decrypt',
                        help='Decrypt (default is to encrypt instead)',
                        action='store_true')
    parser.add_argument('-k', '--keyfile',
                        help='Key file name',
                        required=True,
                        type=argparse.FileType('rb'))
    parser.add_argument('--iv',
                        help='Initialization Vector file name (CBC) or nonce (CTR)',
                        required=False,
                        type=argparse.FileType('rb'))
    parser.add_argument('-i', '--infile',
                        help='Input file name',
                        required=True,
                        type=argparse.FileType('rb'))
    parser.add_argument('-o', '--outfile',
                        help='Output file name',
                        required=True,
                        type=argparse.FileType('wb'))
    args = parser.parse_args()

    # Read the key
    key = args.keyfile.read()
    args.keyfile.close()

    if args.debug:
        print("main():", len(key),"bytes key read from file: ", key)
        
    # Process data

    # Skip first bytes if required
    if args.skipbytes > 0:
        buf = args.infile.read(args.skipbytes)
        args.outfile.write(buf)

    buf = args.infile.read()

    args.infile.close()

    if args.cipher == "rc4":
        obj = Cipher(algorithms.ARC4(key), mode=None)
    elif args.cipher == "aes-ecb":
        obj = Cipher(algorithms.AES(key), modes.ECB())
    elif args.cipher == "aes-cbc":
        if not args.iv:
            sys.stderr.write(
                """Error: an Initialization Vector is required for CBC mode.
Try --help for more information.\n""")
            sys.exit(1)
        obj = Cipher(algorithms.AES(key), modes.CBC(args.iv.read()))
    elif args.cipher == "aes-ctr":
        if not args.iv:
            sys.stderr.write(
                """Error: a nonce is required for CTR mode.
Try --help for more information.\n""")
            sys.exit(1)
        obj = Cipher(algorithms.AES(key), modes.CTR(args.iv.read()))
    else:
        assert False, "Unknown cipher selected: %s" % args.cipher

    if args.decrypt:
        res = obj.decryptor()
    else:
        res = obj.encryptor()

    args.outfile.write(res.update(buf) + res.finalize())
    args.outfile.close()

if __name__ == "__main__":
    main()
