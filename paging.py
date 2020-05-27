# Tinotenda Muzambi
# MZMTIN002

import sys
from random import randint


def FIFO(size, pages):
    no_faults_counter = 0
    no_faults = 0   # Number of faults.
    memory = {}     # Representation of page frames in memory.
    added = []
    for i in range(size):   # Initialise memory values.
        memory[i + 1] = "-"
    for i in pages:     # For each value in the pages requested.
        for j in range(1, size + 1):
            if memory[j] == i:  # If page is already in memory, do nothing.
                break
            elif memory[j] == '-':  # If page frame is empty, add page and increment no faults.
                memory[j] = i
                added.append(j)
                no_faults += 1
                break
            if j == size:   # If no free page frames, replace one using FIFO.
                no_faults_counter += 1
                no_faults += 1
                memory[added[no_faults_counter - 1]] = i
                added.append(added[no_faults_counter - 1])

    return no_faults


def LRU(size, pages):
    no_faults = 0   # Number of faults.
    memory = {}     # Representation of page frames in memory.
    indexes = {}    # Stores pages and their least recent access time.
    curr_max = 0    # Stores max recent access time.
    for i in range(size):   # # Initialise memory values.
        memory[i + 1] = "-"
    for i in pages:   # For each value in the pages requested.
        for j in range(1, size + 1):
            if no_faults > 0 and memory[j] == i:    # If page is already in memory, update access time.
                curr_max += 1
                indexes[memory[j]] = curr_max
                break
            elif memory[j] == '-':  # If page frame is empty, add page and increment no faults.
                curr_max += 1
                memory[j] = i
                no_faults += 1
                indexes[i] = curr_max
                break
            if j == size:   # If no free page frames, replace one using LRU.
                min_el = 1000
                curr_key = -1   # Stores least recent access time.
                for k in range(1, len(memory) + 1):
                    if indexes[memory[k]] < min_el:     # If current access time < minimum, update access time.
                        min_el = indexes[memory[k]]
                        curr_key = k
                for k in range(1, len(memory) + 1):
                    if indexes[memory[k]] > curr_max:   # Identify least recent access time.
                        curr_max = indexes[memory[k]]
                curr_max += 1
                indexes[i] = curr_max           # Add new page to indexes.
                del indexes[memory[curr_key]]   # Delete old page from index.
                memory[curr_key] = i    # Replace page in memory with current requested page.
                no_faults += 1          # Increment number of faults.

    return no_faults


def OPT(size, pages):
    no_faults = 0   # Number of faults.
    memory = {}     # Representation of page frames in memory.
    for i in range(size):   # Initialise memory values.
        memory[i + 1] = "-"
    for i in range(len(pages)):     # For each value in the pages requested.
        for j in range(1, size + 1):
            if no_faults > 0 and memory[j] == pages[i]:     # If page is already in memory, do nothing.
                break
            elif memory[j] == '-':      # If page frame is empty, add page and increment no faults.
                memory[j] = pages[i]
                no_faults += 1
                break
            if j == size:   # If no free page frames, replace one using OPT.
                processed = []  # values already processed.
                indexes = {}    # stores pages and their furthest access time.
                for k in range(len(memory), 0, -1):     # initialise access time to -1.
                    indexes[memory[k]] = -1
                curr_key = -1   # stores furthest access time across all pages.
                for k in range(i + 1, len(pages)):
                    for m in range(1, len(memory) + 1):
                        if pages[k] == memory[m]:           # If page occurs after current page requested and
                            if not pages[k] in processed:   # page hasn't already been processed
                                curr_key += 1               # update furthest access time for that page.
                                indexes[pages[k]] = curr_key
                                processed.append(pages[k])
                curr_max = -1       # stores page with the highest (furthest) access time.
                for k in range(1, len(indexes) + 1):
                    if indexes[memory[k]] == -1:    # If page access time is still -1, it doesn't
                        # occur after initial request and it'll be the one to be replaced.
                        curr_max = k
                        break
                    elif indexes[memory[k]] > curr_max:     # Update current max page access time.
                        curr_max = k
                memory[curr_max] = pages[i]     # Replace page in memory with current requested page.
                no_faults += 1      # Increment number of faults.

    return no_faults


def main():
    size = int(sys.argv[1])
    pages = ""
    try:
        page_length = eval(sys.argv[2])
    except IndexError:
        page_length = 8
    for i in range(page_length):      # Randomly generate pages to be requested.
        pages += str(randint(0, 9))
    print(pages)
    print("FIFO", FIFO(size, pages), "page faults.")
    print("LRU", LRU(size, pages), "page faults.")
    print("OPT", OPT(size, pages), "page faults.")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python paging.py [number of pages]")
    else:
        main()
