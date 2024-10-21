# Graverobber

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: We're breaking into the catacombs to find a rumoured great treasure - I hope there's no vengeful spirits down there...

## NOTES

1. Unzip challenge fiels
   1. > unzip rev_graverobber.zip
2. MANUAL ENUMERATION
   1. FILE
      1. > file robber
         1. robber: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=972b4d1424b8cd4916e26b94ebb6257f970e4cbb, for GNU/Linux 4.4.0, not stripped
   2. STRINGS
      1. > strings robber
         1. We see the normal GLIBC, but we also see the text: 
            1. We took a wrong turning!
            2. We found the treasure! (I hope it's not cursed)
3. GHIDRA
   1. Lets open this in ghidra and see the code
   2. Check the functions
      1. MAIN

            ```c
                undefined8 main(void)

                {
                int iVar1;
                undefined8 uVar2;
                long in_FS_OFFSET;
                uint local_ec;
                stat local_e8;
                undefined8 local_58;
                undefined8 local_50;
                undefined8 local_48;
                undefined8 local_40;
                undefined8 local_38;
                undefined8 local_30;
                undefined8 local_28;
                undefined8 local_20;
                undefined4 local_18;
                long local_10;

                local_10 = * (long * )(in_FS_OFFSET + 0x28);
                local_58 = 0;
                local_50 = 0;
                local_48 = 0;
                local_40 = 0;
                local_38 = 0;
                local_30 = 0;
                local_28 = 0;
                local_20 = 0;
                local_18 = 0;
                local_ec = 0;
                do {
                    if (0x1f < local_ec) {
                    puts("We found the treasure! (I hope it\'s not cursed)");
                    uVar2 = 0;
                    LAB_00101256:
                        if (local_10 != * (long * )(in_FS_OFFSET + 0x28)) {
                        /* WARNING: Subroutine does not return */
                        __stack_chk_fail();
                        }
                    return uVar2;
                    }
                    *(char * )((long) & local_58 + (long)(int)(local_ec * 2)) = (char) * (undefined4 * )(parts + (long)(int) local_ec * 4);
                    *(undefined * )((long) & local_58 + (long)(int)(local_ec * 2 + 1)) = 0x2f;
                    
                    iVar1 = stat((char * ) & local_58, & local_e8);
                    if (iVar1 != 0) {
                    puts("We took a wrong turning!");
                    uVar2 = 1;
                    goto LAB_00101256;
                    }
                    local_ec = local_ec + 1;
                } while (true);
                }
            ```

            1. So it looks like we need the 0x1f to be less than "local_ec" to pass the check the "Find the treasure"
            2. 0x1f = 31 in decimal
            3. It also looks like if iVar1 DOES NOT = 0 then it outputs "We took a wrong turning"
4. RUN
   1. Lets run the binary now to explore
      1. > ./robber
         1. We took a wrong turning!
         2. So we run the program and  immediately get the "We took a wrong turning"
      2. > ./robber 
