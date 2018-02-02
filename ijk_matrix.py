import time
import numpy as np
import random
import sys
import os
from datetime import datetime
import string
import subprocess
from subprocess import call

Nm = int(sys.argv[1])   #Matrix size
#Ns = int(sys.argv[2])   #size of sort
R = int(sys.argv[2])     #run time

M1 = np.random.rand(Nm, Nm)
M2 = np.random.rand(Nm, Nm)

a = 0
start_time_1 = time.time()
Matrix = [[0 for i in range(Nm)] for j in range(Nm)]

for d1 in range(Nm):
    for d2 in range(Nm):
        M1[d1][d2] = d1 * d2
for d3 in range(Nm):
    for d4 in range(Nm):
        M2[d3][d4] = d3 * d4

for i in range(len(M1)):
    for j in range(len(M2[0])):
        for k in range(len(M2)):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            end_time_1 = time.time()
            time_taken_1 = end_time_1 - start_time_1
            #print('time taken in writing is %s seconds'%(time_taken_1))
            file_name = "matrix1.txt"
            file_name1 = "run_matrix1.txt"
            f = open(file_name, "w")
            f1 = open(file_name1, "w")
            f.write("%s" %(Matrix))
            f1.write("%s" %(time_taken_1))
f.close()
f1.close()

a = a + 1
start_time_2 = time.time()
Matrix = [[0 for i in range(Nm)] for j in range(Nm)]

for d1 in range(Nm):
    for d2 in range(Nm):
        M1[d1][d2] = d1 * d2
for d3 in range(Nm):
    for d4 in range(Nm):
        M2[d3][d4] = d3 * d4

for i in range(len(M1)):
    for k in range(len(M2[0])):
        for j in range(len(M2)):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            end_time_2 = time.time()
            time_taken_2 = end_time_2 - start_time_2
            file_name = "matrix2.txt"
            file_name1 = "run_matrix2.txt"
            f = open(file_name, "w")
            f1 = open(file_name1, "w")
            f.write("%s" %(Matrix))
            f1.write("%s" %(time_taken_2))
f.close()
f1.close()

o_p = os.popen("diff matrix1.txt matrix2.txt").read()
if len(o_p) != 0:
    print('Identical Matrix ijk and ikj' + str(a)+"|"+o_p+"|")
else:
    print('Not indentical matrix ijk and ikj' + str(a))


a = a + 1
start_time_3 = time.time()
Matrix = [[0 for i in range(Nm)] for j in range(Nm)]

for d1 in range(Nm):
    for d2 in range(Nm):
        M1[d1][d2] = d1 * d2
for d3 in range(Nm):
    for d4 in range(Nm):
        M2[d3][d4] = d3 * d4

for j in range(len(M1)):
    for i in range(len(M2[0])):
        for k in range(len(M2)):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            end_time_3 = time.time()
            time_taken_3 = end_time_3 - start_time_3
            file_name = "matrix3.txt"
            file_name1 = "run_matrix3.txt"
            f = open(file_name, "w")
            f1 = open(file_name1, "w")
            f.write("%s" %(Matrix))
            f1.write("%s" %(time_taken_3))
f.close()
f1.close()

o_p = os.popen("diff matrix1.txt matrix3.txt").read()
if len(o_p) != 0:
    print('Identical Matrix ijk and jik' + str(a)+"|"+o_p+"|")
else:
    print('Identical Matrix ijk and jik' + str(a))


o_p = os.popen("diff matrix2.txt matrix3.txt").read()
if len(o_p) != 0:
    print('identical Matrix ikj and jik ' + str(a)+"|"+o_p+"|")
else:
    print('not identical Matrix ikj and jik ' + str(a))


a = a + 1
start_time_4 = time.time()
Matrix = [[0 for i in range(Nm)] for j in range(Nm)]

for d1 in range(Nm):
    for d2 in range(Nm):
        M1[d1][d2] = d1 * d2
for d3 in range(Nm):
    for d4 in range(Nm):
        M2[d3][d4] = d3 * d4

for j in range(len(M1)):
    for k in range(len(M2[0])):
        for i in range(len(M2)):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            end_time_4 = time.time()
            time_taken_4 = end_time_4 - start_time_4
            file_name = "matrix4.txt"
            file_name1 = "run_matrix4.txt"
            f = open(file_name, "w")
            f1 = open(file_name1, "w")
            f.write("%s" %(Matrix))
            f1.write("%s" %(time_taken_4))
f.close()
f1.close()


o_p = os.popen("diff matrix1.txt matrix4.txt").read()
if len(o_p) != 0:
    print('identical Matrix ijk and jki' + str(a)+"|"+o_p+"|")
else:
    print('identical Matrix ijk and jki ' + str(a))


o_p = os.popen("diff matrix2.txt matrix4.txt").read()
if len(o_p) != 0:
    print('identical Matrix ikj and jki ' + str(a)+"|"+o_p+"|")
else:
    print('identical Matrix ikj and jki ' + str(a))

o_p = os.popen("diff matrix3.txt matrix4.txt").read()
if len(o_p) != 0:
    print('identical Matrix jik and jki ' + str(a)+"|"+o_p+"|")
else:
    print('identical Matrix jik and jki ' + str(a))


a = a + 1
start_time_5 = time.time()
Matrix = [[0 for i in range(Nm)] for j in range(Nm)]

for d1 in range(Nm):
    for d2 in range(Nm):
        M1[d1][d2] = d1 * d2
for d3 in range(Nm):
    for d4 in range(Nm):
        M2[d3][d4] = d3 * d4

for k in range(len(M1)):
    for i in range(len(M2[0])):
        for j in range(len(M2)):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            end_time_5 = time.time()
            time_taken_5 = end_time_5 - start_time_5
            file_name = "matrix5.txt"
            file_name1 = "run_matrix5.txt"
            f = open(file_name, "w")
            f1 = open(file_name1, "w")
            f.write("%s" %(Matrix))
            f1.write("%s" %(time_taken_5))
f.close()
f1.close()



o_p = os.popen("diff matrix1.txt matrix5.txt").read()
if len(o_p) != 0:
    print('Identical Matrix ijk and kij' + str(a)+"|"+o_p+"|")
else:
    print('Identical Matrix ijk and kij' + str(a))


o_p = os.popen("diff matrix2.txt matrix5.txt").read()
if len(o_p) != 0:
    print('identical Matrix ikj and kij ' + str(a)+"|"+o_p+"|")
else:
    print('not identical Matrix ikj and kij ' + str(a))


o_p = os.popen("diff matrix3.txt matrix5.txt").read()
if len(o_p) != 0:
    print('Identical Matrix jik and kij' + str(a)+"|"+o_p+"|")
else:
    print('Identical Matrix jik and kij' + str(a))


o_p = os.popen("diff matrix4.txt matrix5.txt").read()
if len(o_p) != 0:
    print('identical Matrix jki and jik ' + str(a)+"|"+o_p+"|")
else:
    print('not identical Matrix jki and jik ' + str(a))



a = a + 1
start_time_6 = time.time()
Matrix = [[0 for i in range(Nm)] for j in range(Nm)]

for d1 in range(Nm):
    for d2 in range(Nm):
        M1[d1][d2] = d1 * d2
for d3 in range(Nm):
    for d4 in range(Nm):
        M2[d3][d4] = d3 * d4

for k in range(len(M1)):
    for j in range(len(M2[0])):
        for i in range(len(M2)):
            Matrix[i][j] += M1[i][k] * M2[k][j]
            end_time_6 = time.time()
            time_taken_6 = end_time_6 - start_time_6
            file_name = "matrix6.txt"
            file_name1 = "run_matrix6.txt"
            f = open(file_name, "w")
            f1 = open(file_name1, "w")
            f.write("%s" %(Matrix))
            f1.write("%s" %(time_taken_6))
f.close()
f1.close()



o_p = os.popen("diff matrix1.txt matrix6.txt").read()
if len(o_p) != 0:
    print('Identical Matrix ijk and kji' + str(a)+"|"+o_p+"|")
else:
    print('Identical Matrix ijk and kji' + str(a))


o_p = os.popen("diff matrix2.txt matrix6.txt").read()
if len(o_p) != 0:
    print('identical Matrix ikj and kji ' + str(a)+"|"+o_p+"|")
else:
    print('not identical Matrix ikj and kji ' + str(a))


o_p = os.popen("diff matrix3.txt matrix6.txt").read()
if len(o_p) != 0:
    print('Identical Matrix jik and kji' + str(a)+"|"+o_p+"|")
else:
    print('Identical Matrix jik and kji' + str(a))


o_p = os.popen("diff matrix4.txt matrix6.txt").read()
if len(o_p) != 0:
    print('identical Matrix jki and kji ' + str(a)+"|"+o_p+"|")
else:
    print('not identical Matrix jki and kji ' + str(a))

o_p = os.popen("diff matrix5.txt matrix6.txt").read()
if len(o_p) != 0:
    print('identical Matrix kij and kji ' + str(a)+"|"+o_p+"|")
else:
    print('not identical Matrix kij and kji ' + str(a))






