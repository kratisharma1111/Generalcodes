
import sys


def sumcharcount(chars,counts):
    sumc = 0
    for c in chars:
        if c in counts:
            sumc += counts[c]
    return sumc

def makedic0(s):
    """
        s is a string of characters
        make a dictionary with each characters as a key and 0 as the value
        covert all chars to uppercase
    """
    tempdic={}
    for c in s:
        tempdic[c.upper()] = 0
    return tempdic


def updatecounts(d,s):
    for c in s:
        try:
            d[c] += 1
        except:
            pass
    return d

def sumdiccount(d):
    sum = 0
    for dv in d.keys():
        sum += d[dv]
    return sum


def main(fname):
    bases = "ACGT"
    twobase = "MRWSYK"
    threebase = "VHDB"
    noinfochar = "XN-"

    basedic = makedic0(bases)
    twodic = makedic0(twobase)
    threedic = makedic0(threebase)
    noinfodic = makedic0(noinfochar)
    f = open(fname,"r")
    f.readline()  # read first line
    for line in f:
        basedic = updatecounts(basedic,line)
        twodic = updatecounts(twodic,line)
        threedic = updatecounts(threedic,line)
        noinfodic = updatecounts(noinfodic,line)
    basecount = sumdiccount(basedic)
    twocount = sumdiccount(twodic)
    threecount = sumdiccount(threedic)
    noinfocount = sumdiccount(noinfodic)

    print "base counts:"
    for cv in basedic.keys():
        print cv,basedic[cv]
    for cv in twodic.keys():
        print cv,twodic[cv]
    for cv in threedic.keys():
        print cv,threedic[cv]
    somebasecount = basecount+twocount+threecount
    print "total number of base characters:",somebasecount
    print "total number of unambiguous bases:",basecount
    print "two base ambiguous count:", twocount
    print "three base ambigous count:",threecount
    if somebasecount > 1:
        print "unambiguous base proportion:",basecount/float(somebasecount)
        print "GC content:", (basedic['C'] + basedic['G'])/float(basecount)
    print "N count",noinfodic['N'] + noinfodic['X']
    print "indel count:",noinfodic['-']
    return



if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
    exit()
