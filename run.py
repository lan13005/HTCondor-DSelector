#!/usr/bin/env python

import os
import sys
import glob

cwd="/d/grid13/ln16/jasonTest/condorVersion/"

if __name__ == "__main__":
    if len(sys.argv)-1 == 1:
        fileIndex = sys.argv[1]
    else:
        print("exiting... invalid number of arguments")
        exit()
    fileList = glob.glob(cwd+"condor/run_*")
    os.chdir(cwd+"condor")
    os.chdir(fileList[int(fileIndex)])
    print("moved to: "+os.getcwd())
    os.system("root -l -b -q codeThatDoesNothing.C")



