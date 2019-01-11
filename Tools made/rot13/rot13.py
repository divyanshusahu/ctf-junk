#!/usr/bin/env python

import argparse
import string
import sys

def shift(s ,n) :
    cipher = ''
    for c in s :
        if c in string.ascii_lowercase :
            x = ord(c)
            x = x - 97
            x = (x + n)%26
            x = x + 97
            cipher += chr(x)
        elif c in string.ascii_uppercase :
            x = ord(c) - 65
            x = (x + n)%26
            x = x + 65
            cipher += chr(x)
        else :
            cipher += c
            
    return cipher

def main() :
    parser = argparse.ArgumentParser(prog=sys.argv[0])
    parser.add_argument("-s", help="Message string")
    parser.add_argument("-n", help="Number to shift")
    args = parser.parse_args()
    
    if not args.s :
        parser.print_usage()
        sys.exit()
    
    if not args.n :
        print shift(args.s, 13)
        sys.exit()

    if args.n :
        
        for check in args.n :
            if check not in string.digits+"-" :
                parser.print_help()
                sys.exit()
        
        try :
            if '-' in args.n :
                r = args.n.split("-")
                n, m = int(r[0]), int(r[1])
                for num in range(n,m+1) :
                    print num, shift(args.s, num)
                sys.exit()
            else :
                print shift(args.s, int(args.n))
        except :
            #parser.print_help()
            sys.exit()

if __name__ == "__main__":
    main()
