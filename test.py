import argparse

import torch

parser = argparse.ArgumentParser(description='')
parser.add_argument("-cuda", type=int, default=-1, help="use GPU")

args = parser.parse_args()

device = torch.device("cpu" if args.cuda<0 else "cuda:"+str(args.cuda))

t = torch.randn(10000).to(device)
import time
time.sleep(15)

print("end of test")

