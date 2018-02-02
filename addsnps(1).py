import sys
import random

bases =['A','C','G','T']

def addsnps(ss,bases,snprate):
    """
        make a new sequence from ss that has random bases replaced with different bases
    """
    withsnpcopy = ""
    numsnps = 0
    numbases = len(ss) - ss.upper().count('N')
    for b in ss:
        if b.upper() != 'N' and random.random() < snprate:
            numbases += 1
            newbase = b
            while newbase == b:
                newbase = random.choice(bases)
            withsnpcopy += newbase
            numsnps += 1
        else:
            withsnpcopy += b
    newss = "".join(withsnpcopy)
    return numsnps,numbases,newss

def dofastq(fn,fon,erate,bases):
    f = open(fn,"r")
    fo = open(fon,"w")
    numsnps = 0
    numbases = 0
    c = 0
    for line in f:
        if c == 0:
            fo.write("%s : bases changed at rate: %lf\n"%(line.strip(),erate))
        elif c == 1:
            n,nb,newline = addsnps(line.strip(),bases,erate)
            fo.write(newline + "\n")
            numsnps += n
            numbases += nb
        else:
            fo.write("%s\n"%line.strip())
        c += 1
        if c == 4:
            c = 0
    f.close()
    fo.close()
    return numsnps,numbases

def dofasta(fn,fon,erate,bases):
    f = open(fn,"r")
    fo = open(fon,"w")
    fo.write("%s  : bases changed at rate: %lf\n"%(f.readline().strip(),erate))
    numsnps = 0
    numbases = 0
    for line in f:
        n,nb,newline = addsnps(line.strip(),bases,erate)
        fo.write(newline + "\n")
        numsnps += n
        numbases += nb
    f.close()
    fo.close()
    return numsnps,numbases

def main(fn,fon,erate):
    if fn.lower().find(".fastq")>0 or fn.lower().find(".fq")>0:
        numsnps,numbases = dofastq(fn,fon,erate,bases)
    else:
        numsnps,numbases = dofasta(fn,fon,erate,bases)
    return numsnps,numbases



if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "usage: python addsnps.py <fasta or fastaq input file name> <output file name, same format as input> <change proportion, e.g. 0.01>"
        exit()
    numsnps,numbases = main(sys.argv[1],sys.argv[2],float(sys.argv[3]))
    print sys.argv[1],sys.argv[2],sys.argv[3]
    print "# of bases (not counting N's):",numbases,"  # of changes made:",numsnps


