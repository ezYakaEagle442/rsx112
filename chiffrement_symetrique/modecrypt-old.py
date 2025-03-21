#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RC4, AES ECB/CBC/CTR implementation

Run with command-line argument "-h" to display the online help.
This program uses the now deprecated python3-crypto library from Daniel Litz
which used to be the default in Ubuntu 12.04 for example.

Nicolas Pioch, 31 Mar 2012
"""

import sys
import argparse

try:
    import Crypto.Cipher.ARC4
    import Crypto.Cipher.AES
    import Crypto.Util.Counter
except ModuleNotFoundError:
    sys.exit("Failed to load the Crypto modules: install the python3-crypto package.")


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
                        help='Initialization Vector file name (CBC only)',
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
        obj = Crypto.Cipher.ARC4.new(key)
    elif args.cipher == "aes-ecb":
        obj = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_ECB)
    elif args.cipher == "aes-cbc":
        if not args.iv:
            sys.stderr.write(
                """Error: an Initialization Vector is required for CBC mode.
Try --help for more information.\n""")
            sys.exit(1)
        obj = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC,
                                    args.iv.read())
    elif args.cipher == "aes-ctr":
        ctr = Crypto.Util.Counter.new(128)
        obj = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CTR,
                                    counter=ctr)
    else:
        assert False, "Unknown cipher selected: %s" % args.cipher

    if args.decrypt:
        res = obj.decrypt(buf)
    else:
        res = obj.encrypt(buf)

    args.outfile.write(res)
    args.outfile.close()

if __name__ == "__main__":
    main()
