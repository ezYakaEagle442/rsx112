#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""RC4 implementation

Run with command-line argument "-h" to display the online help.

Nicolas Pioch, 31 Mar 2012
$Id$
"""

import argparse

def hexdump_str(string):
    hexparts = []
    for c in string:
        hexparts.append("%02x" % ord(c))
    return " ".join(hexparts)

def hexdump_bytearray(ba):
    hexparts = []
    for i in range(len(ba)):
        hexparts.append("%02x" % ba[i])
    return " ".join(hexparts)

def rc4_stream_generator(key):
    S = bytearray()
    K = bytearray()

    assert key, "Empty key!"

    key_length = len(key)

    if debug:
        print("rc4 init: %d-bit key: %s" % ((8 * key_length), hexdump_bytearray(key)))

    if key_length > 256:
        print("Warning: key is", key_length, "bytes long: only the first 256 bytes will be used.")

    # Initialization of state array S
    for i in range(256):
        S.append(i)
        K.append(key[i % key_length])

    if debug:
        print("rc4 init: K[] =", hexdump_bytearray(K))

    j = 0
    for i in range(256):
        j = (j + S[i] + K[i]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0

    if debug:
        print("rc4 init: state S[] =", hexdump_bytearray(S))

    # Generation of pseudo-random stream
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        yield S[(S[i] + S[j]) % 256]

def main():
    global debug

    parser = argparse.ArgumentParser(
        description='Encrypt/decrypt a file using the RC4 cipher.')
    parser.add_argument('-d', '--debug',
                        help='Enable debug diagnostics',
                        action='store_true')
    parser.add_argument('-s', '--skipbytes',
                        help='Number of bytes to copy unmodified (default: 0)',
                        type=int, default=0)
    parser.add_argument('-k', '--keyfile',
                        help='Key file name',
                        required=True,
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

    debug = args.debug

    # Read the key
    key = args.keyfile.read()
    args.keyfile.close()

    if debug:
        print("main():", len(key), "byte key read from file:", hexdump_bytearray(key))

    rc4stream = rc4_stream_generator(key)

    # Process data

    # Skip first bytes if required
    if args.skipbytes > 0:
        buf = args.infile.read(args.skipbytes)
        args.outfile.write(buf)

    while True:
        c = args.infile.read(1)
        if not c:
            break
        args.outfile.write(bytes([(ord(c) ^ next(rc4stream))]))

    args.infile.close()
    args.outfile.close()

if __name__ == "__main__":
    main()
