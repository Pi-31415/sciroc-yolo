#!/usr/bin/env python3

"""
This script performs object detection
"""

import sys

def main():
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == '-input':
        print("The input is "+args[1])

if __name__ == '__main__':
    main()
