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
    curr_max = 0
    for i in range(size):
        memory[i + 1] = "-"
    for i in pages:
        for j in range(1, size + 1):
            if no_faults > 0 and memory[j] == i:
                curr_max += 1
                indexes[memory[j]] = curr_max
                break
            elif memory[j] == '-':
                curr_max += 1
                memory[j] = i
                no_faults += 1
                indexes[i] = curr_max
                break
            if j == size:
                min_el = 1000
                curr_key = -1
                for k in range(1, len(memory) + 1):
                    if indexes[memory[k]] < min_el:
                        min_el = indexes[memory[k]]
                        curr_key = k
                for k in range(1, len(memory) + 1):
                    if indexes[memory[k]] > curr_max:
                        curr_max = indexes[memory[k]]
                curr_max += 1
                indexes[i] = curr_max
                del indexes[memory[curr_key]]
                memory[curr_key] = i
                no_faults += 1

    print(memory)
    return no_faults


def OPT(size, pages):
    no_faults = 0
    memory = {}
    for i in range(size):
        memory[i + 1] = "-"
    for i in range(len(pages)):
        for j in range(1, size + 1):
            if no_faults > 0 and memory[j] == pages[i]:
                break
            elif memory[j] == '-':
                memory[j] = pages[i]
                no_faults += 1
                break
            if j == size:
                processed = []
                indexes = {}
                for k in range(len(memory), 0, -1):
                    indexes[memory[k]] = -1
                curr_key = -1
                for k in range(i + 1, len(pages)):
                    for m in range(1, len(memory) + 1):
                        if pages[k] == memory[m]:
                            if not pages[k] in processed:
                                curr_key += 1
                                indexes[pages[k]] = curr_key
                                processed.append(pages[k])
                curr_max = -1
                for k in range(1, len(indexes) + 1):
                    if indexes[memory[k]] == -1:
                        curr_max = k
                        break
                    elif indexes[memory[k]] > curr_max:
                        curr_max = k
                memory[curr_max] = pages[i]
                no_faults += 1

    print(memory)
    return no_faults


def main():
    size = int(sys.argv[1])
    # pages = "701203042303212017"
    # pages = "85625354"
    # pages = "23421375"
    pages = ""
    for i in range(8):
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
