import os

i = 0

n = int(input('Instance count:  '))

import sys
import subprocess

procs = []
for i in range(n):
    proc = subprocess.Popen([sys.executable, 'spaceshot.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)

for proc in procs:
    proc.wait()
