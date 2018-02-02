import numpy as np
import random
import sys
import os
from datetime import datetime
import string
import subprocess
from subproccess import call #Do you need this b/c you already imported subpr"""

Nm = int(sys.argv[1])   #size of matrix   #sysargv is a string, so the int forc$
Ns = int(sys.argv[2])   #size of sort
R = int(sys.argv[3])    #number of repetitions

#Correctness Tests
N = 10 #For correctness tests only
x = 0  #Phase count
M1 = np.random.rand(N, N)
M2 = np.random.rand(N, N)
Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]

w = open("MTResult-1.txt", "w")
w.close()

x = x + 1
Matrix = [[0 for i in range(N)] for j in range(N)]

for i in range(N):
    for k in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]

w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = os.popen("diff MTResult-1.txt MTResult-2.txt").read()
if len(out) != 0:
    print('Difference found in Phase ' + str(x)+"|"+out+"|")
else:
    print('No difference found in Phase ' + str(x))
    
#Phase 3
x = x + 1
Matrix = [[0 for i in range(N)] for j in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]

w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = os.popen("diff MTResult-1.txt MTResult-2.txt").read
if len(out) != 0:
    print('Difference found in Phase ' + str(x)+"|"+out+"|")
else:
    print('No difference found in Phase ' + str(x))

#Phase 4
x = x + 1
Matrix = [[0 for i in range(N)] for j in range(N)]
for k in range(N):
    for j in range(N):
        for i in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]

w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = os.poprn("diff MTResult-1.txt MTResult-2.txt").read
if len(out) != 0:
    print('Difference found in Phase ' + str(x)+"|"+out+"|")
else:
    print('No difference found in Phase ' + str(x))

#Phase 5
x = x + 1
Matrix = [[0 for i in range(N)] for j in range(N)]
for j in range(N):
    for i in range(N):
        for k in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]

w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = os.poprn("diff MTResult-1.txt MTResult-2.txt").read
if len(out) != 0:
    print('Difference found in Phase ' + str(x)+"|"+out+"|")
else:
    print('No difference found in Phase ' + str(x))

#Phase 6
x = x + 1
Matrix = [[0 for i in range(N)] for j in range(N)]
for j in range(N):
    for k in range(N):
        for i in range(N):
            Matrix[i][j] += M1[i][k] * M2[k][j]

w = open("MTResult-2.txt", "w")
w.write("{}".format(Matrix))
w.close()

out = os.poprn("diff MTResult-1.txt MTResult-2.txt").read
if len(out) != 0:
    print('Difference found in Phase ' + str(x)+"|"+out+"|")
else:
    print('No difference found in Phase ' + str(x))

#Matrix Performance Tests
#matrix.tmp.bak is the template file to generate different (ijk) orders

os. popen("rm *.txt")     #clean up all text files

#Do ijk
os.popen("cp matrix.tmp.back matrix.py")   #make a working copy
os.popen("chmod +x matrix.py")             #make matrix.py executable
cmd = "sed -i s/#1/i/q matrix.py"   #sed tells program to replace #1 with i glo$
os.popen(cmd)
cmd = "sed -i s/#2/j/g matrix.py"
os.popen(cmd)
cmd = "sed -i s/#3/k/g matrix.py"
os.popen(cmd)

for i in range(R):
    cmd = "matrix.py"+str(Nm)
    os.popen(cmd)              #run

#Do ikj
os.popen("cp matrix.tmp.back matrix.py")   #make a worki$
os.popen("chmod +x matrix.py")             #make matrix.$
cmd = "sed -i s/#1/i/q matrix.py"   #sed tells program t$
os.popen(cmd)
cmd = "sed -i s/#2/k/g matrix.py"
os.popen(cmd)
cmd = "sed -i s/#3/j/g matrix.py"
os.popen(cmd)

for i in range(R):
    cmd = "matrix.py"+str(Nm)
    os.popen(cmd)              #run

#Do jik
os.popen("cp matrix.tmp.back matrix.py")   #make a worki$
os.popen("chmod +x matrix.py")             #make matrix.$
cmd = "sed -i s/#1/j/q matrix.py"   #sed tells program t$
os.popen(cmd)
cmd = "sed -i s/#2/i/g matrix.py"
os.popen(cmd)
cmd = "sed -i s/#3/k/g matrix.py"
os.popen(cmd)

for i in range(R):
    cmd = "matrix.py"+str(Nm)
    os.popen(cmd)              #run

#Do jki
os.popen("cp matrix.tmp.back matrix.py")   #make a worki$
os.popen("chmod +x matrix.py")             #make matrix.$
cmd = "sed -i s/#1/j/q matrix.py"   #sed tells program t$
os.popen(cmd)
cmd = "sed -i s/#2/k/g matrix.py"
os.popen(cmd)
cmd = "sed -i s/#3/i/g matrix.py"
os.popen(cmd)

for i in range(R):
    cmd = "matrix.py"+str(Nm)
    os.popen(cmd)              #run

#Do kij
os.popen("cp matrix.tmp.back matrix.py")   #make a worki$
os.popen("chmod +x matrix.py")             #make matrix.$
cmd = "sed -i s/#1/k/q matrix.py"   #sed tells program t$
os.popen(cmd)
cmd = "sed -i s/#2/i/g matrix.py"
os.popen(cmd)
cmd = "sed -i s/#3/j/g matrix.py"
os.popen(cmd)

for i in range(R):
    cmd = "matrix.py"+str(Nm)
    os.popen(cmd)              #run

#Do kji
os.popen("cp matrix.tmp.back matrix.py")   #make a worki$
os.popen("chmod +x matrix.py")             #make matrix.$
cmd = "sed -i s/#1/k/q matrix.py"   #sed tells program t$
os.popen(cmd)
cmd = "sed -i s/#2/j/g matrix.py"
os.popen(cmd)
cmd = "sed -i s/#3/i/g matrix.py"
os.popen(cmd)

for i in range(R):
    cmd = "matrix.py"+str(Nm)
    os.popen(cmd)              #run
    
#Extra Credit: numpy (apple to apple comparison)
M1 = np.random.rand(Nm, Nm)
M2 = np.random.rand(Nm, Nm)
Te = datetime.now()
Result = np.dot(M1, M2)
Te = datetime.now() - Te
TotalUs = Te.seconds * 1000000 + Te.microseconds
Mflops = pow(Nm, 3)/float(TotalUs)
w = open("MTime.txt", "a")
w.write("numpy Results:/n {N} {T} {M} /n".format(N=Nm, T=TotalUs, M=Mflops)

#BubbleSort1: No split
Input = np.random.rand(Ns)
Itmp = list(Input)
def sort(numbers):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                sorted = False
                numbers[i + 1], numbers[i] = numbers[i], numbers[i + 1]

for i in range(R):     #Run R-times
    Itmp = list(Input) #Get fresh input
    print Itmp         #see if moved?
    Te = datetime.now()
    sort(Itmp)         #This is in place sort. Input will be altered.
    Te = datetime.now() - Te
    TotalUs = Te.seconds * 1000000 + Te.microseconds
    w.write("Full Bubblesort Results:/n {N} {T} /n".format(N=Ns, T=TotalUs))
#BubbleSort2: Split input in half. Sort, then merge.
def merge(list1, list2)
    output = []
    i = j = k = 0
    while k<(Ns//2):
#       print("{} {} {}/n".format(k, (Ns//2), i, j)
        if list1[i] < list2[j]:
            output.append(list1[i])
            i = i + 1
        else:
            output.append(list2[j])
            j = j + 1
        k = k + 1
    return(output)

for i in range(R):
    Te = datetime.now()
    Itmp = list(Input)  #Use the same input
    List1 = Itmp[0:(Ns//2)]
    List2 = Itmp[(Ns//2):]
    sort(List1)
    sort(List2)
    Output = merge(List1, List2)
    Te = datetime.now() - Te
    TotalUs = Te.seconds * 1000000 + Te.microseconds
    w.write("Split Bubblesort Result\n".format(N=Ns, T=TotalUs))
w.close()

print("All done!")



