import psutil
import sys
import os

PROCNAME = "UV4.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()

print(sys.argv)
print(sys.argv[1])
os.startfile(sys.argv[1])
