import subprocess, os

for i in range(1000,1,-1) :
    filename = "%s.tar" % str(i)
    command = "tar -xvf %s" % filename
    subprocess.run(command, shell=True)
    fillername = "filler%s.txt" % str(i)
    os.rename("filler.txt", fillername)
