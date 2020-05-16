# Tinotenda Muzambi
# MZMTIN002

import sys


def FIFO(size, pages):
    print("FIFO")


def LRU(size, pages):
    print("FIFO")


def OPT(size, pages):
    print("FIFO")


def main():
    # ...TODO...
    size = int(sys.argv[1])
    print("FIFO", FIFO(size, pages), "page faults.")
    print("LRU", LRU(size, pages), "page faults.")
    print("OPT", OPT(size, pages), "page faults.")
