# Tinotenda Muzambi
# MZMTIN002

import sys
from random import randint


def FIFO(size, pages):
    no_faults = 0
    memory = {}
    added = []
    for i in range(size):
        memory[i + 1] = "-"
    for i in pages:
        for j in range(1, size + 1):
            if memory[j] == i:
                break
            elif memory[j] == '-':
                memory[j] = i
                added.append(j)
                break
            if j == size:
                no_faults += 1
                memory[added[no_faults - 1]] = i
                added.append(added[no_faults - 1])

    print(memory)
    return no_faults


def LRU(size, pages):
    no_faults = 0
    return no_faults


def OPT(size, pages):
    no_faults = 0
    return no_faults


def main():
    size = int(sys.argv[1])
    pages = "85625354"
    # pages = ""
    # for i in range(8):
    #     pages += str(randint(0, 9))
    print(pages)
    print("FIFO", FIFO(size, pages), "page faults.")
    print("LRU", LRU(size, pages), "page faults.")
    print("OPT", OPT(size, pages), "page faults.")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
