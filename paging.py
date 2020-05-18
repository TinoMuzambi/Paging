# Tinotenda Muzambi
# MZMTIN002

import sys
from random import randint


def FIFO(size, pages):
    no_faults_counter = 0
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
                no_faults += 1
                break
            if j == size:
                no_faults_counter += 1
                no_faults += 1
                memory[added[no_faults_counter - 1]] = i
                added.append(added[no_faults_counter - 1])

    print(memory)
    return no_faults


def LRU(size, pages):
    no_faults = 0
    memory = {}
    indexes = {}
    for i in range(size):
        memory[i + 1] = "-"
    for i in pages:
        for j in range(1, size + 1):
            if memory[j] == i:
                break
            elif memory[j] == '-':
                memory[j] = i
                no_faults += 1
                indexes[i] = j
                break
            if j == size:
                min_el = 1000
                curr_key = -1
                for k in range(1, len(memory) + 1):
                    if indexes[memory[k]] < min_el:
                        min_el = indexes[memory[k]]
                        curr_key = k
                indexes[i] = indexes[memory[curr_key]] + 1
                del indexes[memory[curr_key]]
                memory[curr_key] = i

    print(memory)
    return no_faults


def OPT(size, pages):
    no_faults = 0
    return no_faults


def main():
    size = int(sys.argv[1])
    pages = "701203042303120"
    # pages = "85625354"
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
