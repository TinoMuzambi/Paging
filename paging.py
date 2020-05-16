# Tinotenda Muzambi
# MZMTIN002

import sys
from random import randint


def FIFO(size, pages):
    print("FIFO")
    no_faults = 0
    return no_faults


def LRU(size, pages):
    print("LRU")
    no_faults = 0
    return no_faults


def OPT(size, pages):
    print("OPT")
    no_faults = 0
    return no_faults


def main():
    size = int(sys.argv[1])
    pages = ""
    for i in range(7):
        pages += str(randint(0, 9))
    print(pages)
    print("FIFO", FIFO(size, pages), "page faults.")
    print("LRU", LRU(size, pages), "page faults.")
    print("OPT", OPT(size, pages), "page faults.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
