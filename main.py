import os
from settings import *
import time
import subprocess


def parse(line,qargs):
    numberic_args = ['memory.free', 'memory.total', 'power.draw', 'power.limit']
    power_manage_enable=lambda v:(not 'Not Support' in v)
    to_numberic=lambda v:float(v.upper().strip().replace('MIB','').replace('W',''))
    process = lambda k,v:((int(to_numberic(v)) if power_manage_enable(v) else 1) if k in numberic_args else v.strip())
    return {k:process(k,v) for k,v in zip(qargs,line.strip().split(','))}

def query_gpu(qargs=[]):
    qargs =['memory.free', 'power.draw']+ qargs
    cmd = 'nvidia-smi --query-gpu={} --format=csv,noheader'.format(','.join(qargs))
    results = os.popen(cmd).readlines()
    return [parse(line,qargs) for line in results]

while True:
    gpustats = query_gpu()
    for index,gpu in enumerate(gpustats):
        if gpu["memory.free"] > limitmem and gpu["power.draw"]< limitpow:
            subprocess.check_call(command+["-cuda",str(index)])
            break
    time.sleep(interval)