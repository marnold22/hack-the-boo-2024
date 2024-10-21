# QueOnda

## FLAG: HTB{w3lc0m3_2_pwn_f35t1v4l_206455a1e1ec082b0f3ab0544396554c}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Que onda! Welcome to the festival of Pwn! This is a small guide to help you continue your journey, follow the instructions in README.txt

## NOTES

1. Spawn Docker
   1. IP: 83.136.255.10
   2. PORT: 49677
2. Unzip challenge files
   1. > unzip pwn_que_onda.zip 
      1. Notes.txt, challenge->que_onda, challenge -> glibc
3. NOTES
   1. It looks like this particular challenge is based around being familiar with:
      1. GDB
      2. GEF
      3. PWN TOOLS
   2. So we can run the tools.sh script to install these
4. RUN
   1. Lets connect to this with nc and test to see what it's asking
      1. > nc 83.136.255.10 49677

        ```text
            ▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧
            ▧  Hola mi Amigos! Send me the string "flag"
            ▧  and I will give you uno grande prize!!
            ▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧▧
        ```

        1. INPUT: flag
        2. RESPONSE: `HTB{w3lc0m3_2_pwn_f35t1v4l_206455a1e1ec082b0f3ab0544396554c}`
        3. Wellllll that was quick.... so lets actually run through the local install like what the challenge was intended to do!

## LOCAL & INSTRUCTIONS

1. TOOLS
   1. Lets first install the tools with the tools.sh
      1. > ./tools.sh
         1. **I allready have these installed so no need to repeat**
2. SOLVER
   1. Lets go make our own SOLVER.PY modeled from the previous challenge

        ```py
            #!/usr/bin/python3
            from pwn import *
            import warnings
            import os
            warnings.filterwarnings('ignore')
            context.arch = 'amd64'
            context.log_level = 'critical'

            fname = './que_onda' 

            LOCAL = True # Change this to "True" to run the solver locally

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
        ```

        1. After a tad bit of debugging I got rid of the original "print(f'Flag --> {r.recvline_contains(b"HTB").strip().decode()}\n')" statement and chose to just create a response variable and recieve ALL
        2. We also needed to change the sla('> ', '1') to sla('$ ', 'flag') that way we knew what the correct character was to start our recieve and send
3. RUN (locally)
   1. ./solver.py
      1. Running solver locally...
      2. HTB{f4ke_fl4g_4_t35t1ng}
   2. SUCCESS!
4. RUN (server)
   1. First change LOCAL = False (so it will look to the server not local)
      1. > ./solver 83.136.255.10 496777
         1. Running solver remotely at 83.136.255.10 496777
            1. HTB{w3lc0m3_2_pwn_f35t1v4l_1f2d1a3788cd630009104d154bfaeb46}
