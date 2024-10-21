#!/usr/bin/python3
from pwn import *
import warnings
import os
warnings.filterwarnings('ignore')
context.arch = 'amd64'
context.log_level = 'critical'

fname = './que_onda' 

LOCAL = False # Change this to "True" to run the solver locally

os.system('clear')

if LOCAL:
  print('Running solver locally..\n')
  r = process(fname)
else:
  IP   = str(sys.argv[1]) if len(sys.argv) >= 2 else '0.0.0.0'
  PORT = int(sys.argv[2]) if len(sys.argv) >= 3 else 1337
  r    = remote(IP, PORT)
  print(f'Running solver remotely at {IP} {PORT}\n')

sla = lambda x,y : r.sendlineafter(x,y)

# Send the statement "flag" to complete challenge
sla('$ ', 'flag')   # CHANGE THIS

response = r.recvall().decode()
print(response)

# print(f'Flag --> {r.recvline_contains(b"HTB").strip().decode()}\n')
