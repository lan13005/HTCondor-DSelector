#!/usr/bin/env python

import os
import subprocess

fileLoc="list.txt"
outHistName="hist.root"
outTreeName="tree.root"
os.system("ls -d /d/grid15/ebarriga/Spring_2017_OmegaPi/tree_pi0pi0pippim__B4_03065* > "+fileLoc)

os.system("rm -rf condor")

with open(fileLoc,"r") as listOfFiles:
    totalLines=0
    for i, line in enumerate(listOfFiles):
        fileLoc=line.rstrip().lstrip()
        runTag=line.split("_")[6].split(".")[0]
        os.system("mkdir -p condor/run_"+runTag)
        os.system("cp codeThatDoesNothing.C condor/run_"+runTag)
        os.system("cp DSelector_ver20.C condor/run_"+runTag)
        os.system("mkdir condor/"+str(i))
        sedArgs=["sed","-i",'s@chain->Add(".*")@chain->Add("'+fileLoc+'")@',"condor/run_"+runTag+"/codeThatDoesNothing.C"]
        subprocess.Popen(sedArgs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
        sedArgs=["sed","-i",'s@outputHistFileName = .*@outputHistFileName = "'+outHistName+'"@',"condor/run_"+runTag+"/codeThatDoesNothing.C"]
        subprocess.Popen(sedArgs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
        sedArgs=["sed","-i",'s@outputTreeFileName = .*@outputTreeFileName = "'+outTreeName+'"@',"condor/run_"+runTag+"/codeThatDoesNothing.C"]
        subprocess.Popen(sedArgs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
        totalLines+=1

sedArgs=["sed","-i",'s@queue .*@queue '+str(totalLines)+'@', "submit.main"]
subprocess.Popen(sedArgs, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).wait()
