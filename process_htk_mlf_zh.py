#!/usr/bin/env python
#
# This script reads in a HTK MLF format label file and converts the 
# encoded contents to GBK encoding.
#

import string, codecs
fin=open('vom_utt_wlab.mlf')
fout=codecs.open('vom_utt_wlab.gbk.mlf', encoding='gbk', mode='w')
while True:
    sr=fin.readline()
    if sr=='':break
    sr=sr.strip()
    if sr.endswith('.lab"'):
        print >>fout, sr
        while True:
            sr=(fin.readline()).strip()
            if sr=='.':break
            if sr.startswith('\\'):
                lst=(sr.strip('\\')).split('\\') # get the list of octal representation of each byte
                bins=bytearray()
                for itm in lst:
                    val=0
                    for ii in range(3): # each octal number will have exactly 3 numbers, i.e. of the form \nnn
                        val=val*8
                        val=val+int(itm[ii])
                    bins.append(val)
                print >>fout, bins.decode('gbk')
            else:
                print >>fout, sr
        print >>fout, '.'
    else:
        print >>fout, sr
fin.close()
fout.close()
