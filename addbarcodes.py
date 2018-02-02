
import random

barcodes = ['ATGAGATCTT', 'AGCTCATTTC', 'TGAAAATCTT', 'TATCCAGCCA', 'AGGCAGGCAG', 'CTTGTTACTA', 'AAGGCACAAG', 'TGCTCGCTGA', 'GTACCGCCGT', 'CCTCACCAGC']


fqf = "week3_seqs.fq"
fqo = "week3_seqs_bc.fq"


fi = open(fqf,"r")
fo = open(fqo,"w")

while True:
    line = fi.readline()
    if len(line) ==0:
        break
    fo.write(line)
    sline = fi.readline()
    newsline = random.choice(barcodes) + sline[10:]
    fo.write(newsline)
    fo.write(fi.readline())
    fo.write(fi.readline())

fi.close()
fo.close()



