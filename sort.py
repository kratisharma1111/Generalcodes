import numpy as np
import random
import sys
import os
from datetime import datetime
import string
import subprocess
from subprocess import call
import time
import numpy as np

Ns = int(sys.argv[1])

def create_big_random_number_file(number_of_values):
    start_time_1 = time.time()
    file_name = 'big_input_file.txt'
    random_numbers = random.sample(range(200000), number_of_values)
    f = open(file_name, 'w')
    f.write('\n'.join(map(str, random_numbers)))
    f.close()
    end_time_1 = time.time()
    time_taken_1 = end_time_1 - start_time_1
    print('time taken in writing %s random numbers to %s is %s seconds'%(number_of_values, file_name, time_taken_1))

if __name__ == '__main__':
    # lets generate file having 2000 random numbers
     create_big_random_number_file(Ns)


def create_Bubble_sort(f):
        start_time_2 = time.time()
        length = len(f)-1
        exchanges = True
        while length > 0 and exchanges:
                exchanges = False
                for i in range(length):
                        if f[i] > f[i+1]:
                                exchanges = True
                                tmp = f[i]
                                f[i] = f[i+1]
                                f[i+1] = tmp
                length = length - 1
        file_nameSort = 'SortedBigNum.txt'
        fout = open(file_nameSort, 'w')
        fout.write('\n'.join(map(str, f)))
        fout.close()
        end_time_2 = time.time()
        time_taken_2 = end_time_2 - start_time_2
        print('time taken in sorting %s is %s seconds'% (f, time_taken_2))


if __name__ == '__main__':
        f = open('big_input_file.txt')
        f = f.readlines()
        f = np.int32(f)
        create_Bubble_sort(f)
