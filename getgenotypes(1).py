
import math

def phredprob(Qchar):
    """
        calculate the probability of an error using the character code from the read data
        assumes that character coding is as follows:
            phredscore = (ASCII value of the character) minus 33
            use the ord() function to get ASCII value
    """
    phredscore = ord(Qchar)-33
    return pow(10,-float(phredscore)/10)



##for i in range(33,127):
##    print i,chr(i)

def getrefseq(fname):
    """
        return a string containing the first sequence in a fasta file
    """
    lines = open(fname).readlines()
    s = ""
    for l in lines[1:]:
        if l=='' or l[0] == '\n' or l[0]=='>':
            break
        else:
            s += l.strip()
    return s

def getreadinfo(fname):
    """
        pull info on the base position, sequence and quality from a set of reads taken form a bam file
        excludes those reads that have a CIGAR score that is not equal to the length of the sequence
        i.e. avoid reads spanning indels
    """
    f = open(fname)
    firstbases=[]
    seqs = []
    quals = []
    for line in f:
        v = line.split()
        seq = v[9]
        seqlen = len(seq)
        noindelstr = str(seqlen) + "M"
        if v[5] == noindelstr:
            firstbases.append(int(v[3]))
            seqs.append(seq)
            quals.append(v[10])
    return firstbases,seqs,quals


def matchreads(refseq,refbase1num,firstbases,seqs,quals):
    """
        make a list
            one item for each base in refseq in order
            each item is a list and contains, in order
                the base number
                the reference base
                a list of bases that occurred in reads
                a corresponding list of quality values that occured in reads
    """
    ## by python numbering the first base in refseq is at position 0
    ## need to renumber of firstbases[] values, so the base positions line up
    r = []
    numbases = len(refseq)
    for i in range(numbases):
        r.append([i,refseq[i],[],[]])
    numreads = len(firstbases)
    for j in range(numreads):
        k = firstbases[j]
        for ci,c in enumerate(seqs[j]):
            renum1 = (k+ci) - refbase1num
            if 0 <= renum1 < numbases:
                r[renum1][2].append(c)
                r[renum1][3].append(quals[j][ci])
    return r


refname = "hs37ds_22_40000001_40010000.fa"
samsampname = "samsample2.out"
refbase1num = 40000001
refseq = getrefseq(refname)
firstbases,seqs,quals = getreadinfo(samsampname)
readinfo = matchreads(refseq,refbase1num,firstbases,seqs,quals)
varrr = []
for rr in readinfo:
    isvariable = rr[2].count(rr[1]) != len(rr[2])
    if isvariable:
        varrr.append(rr)
##    print refbase1num+rr[0],rr[1],rr[2],rr[3],isvariable
print "positions with variable reads:"
for rr in varrr:
    errorprobs = []
    for e in rr[3]:
        errorprobs.append(phredprob(e))
    print refbase1num+rr[0],rr[1],rr[2],rr[3],errorprobs







