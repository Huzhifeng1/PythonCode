#!/usr/bin/env python
# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os

def splitfile(filename,sizelimit,forline=True):
    size=0
    i=1
    out=open("%s.%04d"%(filename,i),'w')
    for line in open(filename):
        size=size+1 if  forline else size+len(line)
        if(size>sizelimit):
            size=1 if forline else len(line)
            out.close()
            i+=1
            out=open("%s.%04d"%(filename,i),'w')
        out.write(line)
    out.close()

if __name__=='__main__':
    splitfile(filename,500000000,0)
    
