#!/usr/bin/env python

import os
import subprocess

fileLoc="list.txt"

with open(fileLoc,"r") as listOfFiles:
    for i, line in enumerate(listOfFiles):
        fileLoc=line.rstrip().lstrip()
        runTag=line.split("_")[6].split(".")[0]
        moveCmd = "mv condor/"+str(i)+"/* condor/run_"+runTag
        print(moveCmd)
        os.system(moveCmd)
        os.system("rm -r condor/"+str(i))
