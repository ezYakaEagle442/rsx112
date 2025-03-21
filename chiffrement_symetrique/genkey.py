#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate random bytes in a file

Run with command-line argument "-h" to display the online help.

Nicolas Pioch, 4 Jan 2021
$Id$
"""

import argparse
import secrets

def main():
    parser = argparse.ArgumentParser(
        description='Generate random bytes in a file')
    parser.add_argument('-s', '--size',
                        help='Number of bytes to generate (default: 32, or 256 bits)',
                        type=int, default=32)
    parser.add_argument('-o', '--outfile',
                        help='Output file name',
                        required=True,
                        type=argparse.FileType('wb'))
    args = parser.parse_args()

    assert args.size >= 0, "Invalid number of bytes requested: %d" % args.size

    args.outfile.write(secrets.token_bytes(args.size))
    args.outfile.close()

if __name__ == "__main__":
    main()
