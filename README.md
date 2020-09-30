What this code is trying to achieve
- Need to replace codeThatDoesNothing.C string in setupFolders.py and run.py to your runDSelector file name
   You should also change the /d/grid15/ebarriga/Spring_2017_OmegaPi/tree_pi0pi0pippim__B4_03065 text in setupFolders.py to the location of your root tree. A list.txt file is made to store the absolute path
   to the file so that we can input that into the appropriate runDSelectors
- setupFolders.py would setup a file structure so that DSelectors and runDSelectors are all copied. This is to ensure that modifcations from one job does not affect another.
   condor has a cluster id and a process id for each job. We will use process id as our identifier and put the logs/errors/output into there and move everything over later. Probably could have set up a map
   from the process id to the root file.
- run.py would run one of the modified runDSelector codes in the condor/run_XXXXX folder. This is the executable that condor would use which is found in the submit.main script
- clean.py would move all the condor output files to the appropriate condor/run_XXXXX file and delete the dummy folder


they way you should run things
./setupFolders.py
condor_submit submit.main
./clean.py
