# CryptOfTheUndead

## FLAG: HTB{und01ng_th3_curs3_0f_und34th}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: All my important files have been zombified by the notorious Zombie Cybercrime Gang. Can you lay them to rest and bring my files back?

## NOTES

1. Unzip challenge files
   1. > unzip rev_crypt_of_the_undead.zip
      1. We are given two main files:
         1. crypt
         2. flag.txt.undead
2. MANUAL ENUMERATION
   1. FILE
      1. > file crypt
         1. crypt: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5ac213d86cdb95af5f911c357cdc45c66b6bffc1, for GNU/Linux 4.4.0, not stripped
      2. > file flag.txt.undead
         1. flag.txt.undead: data
   2. STRINGS
      1. > strings crypt
         1. We see some interesting strings

            ```text
                error reading file
                error renaming file
                error opening new file
                chacha.c
                0 != counter[1]
                error: that which is undead may not be encrypted
                BRAAAAAAAAAAAAAAAAAAAAAAAAAINS!!
                successfully zombified your file!
                chacha20_block_next
                expand 32-byte k
            ```

3. UNDERSTANDING / GAMEPLAN
   1. So based on what is given I am assuming that the undead flag (flag.txt.undead) is encoded / encrypted and we need to use the binary given to "undead" or decode / decrypt it
4. RUN
   1. So lets try running the binary
      1. > ./crypt
         1. ERROR: Usage: ./crypt file_to_encrypt
         2. So we need to provide a file to encrypt
5. GHIDRA
   1. Check the functions folder
      1. MAIN

            ```c
                undefined4 main(int param_1,char **param_2)

                {
                int iVar1;
                size_t sVar2;
                char *__dest;
                char *pcVar3;
                undefined4 uVar4;
                long in_FS_OFFSET;
                void *local_40;
                size_t local_38;
                long local_30;
                
                local_30 = *(long *)(in_FS_OFFSET + 0x28);
                if (param_1 < 2) {
                    pcVar3 = "crypt";
                    if (param_1 == 1) {
                    pcVar3 = *param_2;
                    }
                    uVar4 = 1;
                    printf("Usage: %s file_to_encrypt\n",pcVar3);
                }
                else {
                    pcVar3 = param_2[1];
                    iVar1 = ends_with(pcVar3,".undead");
                    if (iVar1 == 0) {
                    sVar2 = strlen(pcVar3);
                    __dest = (char *)malloc(sVar2 + 9);
                    strncpy(__dest,pcVar3,sVar2 + 9);
                    sVar2 = strlen(__dest);
                    *(undefined8 *)(__dest + sVar2) = 0x646165646e752e;
                    iVar1 = read_file(pcVar3,&local_38,&local_40);
                    if (iVar1 == 0) {
                        encrypt_buf(local_40,local_38,"BRAAAAAAAAAAAAAAAAAAAAAAAAAINS!!");
                        iVar1 = rename(pcVar3,__dest);
                        if (iVar1 == 0) {
                        iVar1 = open(__dest,0x201);
                        if (iVar1 < 0) {
                            uVar4 = 5;
                            perror("error opening new file");
                        }
                        else {
                            write(iVar1,local_40,local_38);
                            close(iVar1);
                            puts("successfully zombified your file!");
                            uVar4 = 0;
                        }
                        }
                        else {
                        uVar4 = 4;
                        perror("error renaming file");
                        }
                    }
                    else {
                        uVar4 = 3;
                        perror("error reading file");
                    }
                    }
                    else {
                    uVar4 = 2;
                    puts("error: that which is undead may not be encrypted");
                    }
                }
                if (local_30 == *(long *)(in_FS_OFFSET + 0x28)) {
                    return uVar4;
                }
                                    /* WARNING: Subroutine does not return */
                __stack_chk_fail()
                }
            ```

            1. So it look like this program checks params for if a file was specified when executed (if not then throw usage error)
            2. Else it checks for if the file ends with .undead
            3. Then does some string copying
            4. Then it runs a function called encrypt_buf()
               1. This also contains the string "BRAAAAAAAAAAAAAAAAAAAAAAAAAINS!!"
               2. Lets go checkout this encrypt_buf
      2. ENCRYPT_BUF

            ```c
                void encrypt_buf(undefined8 param_1,undefined8 param_2,undefined8 param_3)

                {
                long in_FS_OFFSET;
                undefined auStack_f8 [204];
                undefined8 local_2c;
                undefined4 local_24;
                long local_20;
                
                local_20 = *(long *)(in_FS_OFFSET + 0x28);
                local_2c = 0;
                local_24 = 0;
                chacha20_init_context(auStack_f8,param_3,&local_2c,0);
                chacha20_xor(auStack_f8,param_1,param_2);
                if (local_20 == *(long *)(in_FS_OFFSET + 0x28)) {
                    return;
                }
                                    /* WARNING: Subroutine does not return */
                __stack_chk_fail();
                }
            ```

            1. So it looks like our encrypt function is doing some form of XOR function
               1. It calls chacha20_init_context and chacha20_xor
      3. CHACHA20_XOR

            ```c
                void chacha20_xor(uint *param_1,byte *param_2,long param_3)

                {
                uint uVar1;
                uint uVar2;
                uint *puVar3;
                ulong uVar4;
                uint *puVar5;
                uint uVar6;
                uint uVar7;
                uint uVar8;
                uint uVar9;
                uint uVar10;
                uint uVar11;
                uint uVar12;
                uint uVar13;
                uint uVar14;
                uint uVar15;
                uint uVar16;
                uint uVar17;
                uint uVar18;
                uint uVar19;
                uint uVar20;
                uint uVar21;
                uint local_64;
                int local_5c;
                byte *local_58;
                
                if (param_3 == 0) {
                    return;
                }
                uVar4 = *(ulong *)(param_1 + 0x10);
                local_58 = param_2;
                do {
                    if (uVar4 < 0x40) {
                    puVar3 = (uint *)(uVar4 + (long)param_1);
                    }
                    else {
                    uVar20 = param_1[0x20];
                    local_5c = 10;
                    *param_1 = uVar20;
                    param_1[1] = param_1[0x21];
                    param_1[2] = param_1[0x22];
                    param_1[3] = param_1[0x23];
                    uVar18 = param_1[1];
                    uVar17 = param_1[2];
                    uVar10 = param_1[0x24];
                    uVar16 = param_1[3];
                    param_1[4] = uVar10;
                    param_1[5] = param_1[0x25];
                    param_1[6] = param_1[0x26];
                    param_1[7] = param_1[0x27];
                    uVar2 = param_1[5];
                    uVar13 = param_1[7];
                    uVar14 = param_1[0x28];
                    param_1[8] = uVar14;
                    param_1[9] = param_1[0x29];
                    param_1[10] = param_1[0x2a];
                    param_1[0xb] = param_1[0x2b];
                    local_64 = param_1[0xb];
                    uVar15 = param_1[9];
                    uVar1 = param_1[0x2c];
                    uVar19 = param_1[10];
                    param_1[0xc] = uVar1;
                    param_1[0xd] = param_1[0x2d];
                    param_1[0xe] = param_1[0x2e];
                    param_1[0xf] = param_1[0x2f];
                    uVar6 = param_1[0xd];
                    uVar21 = param_1[0xf];
                    uVar7 = param_1[6];
                    uVar8 = param_1[0xe];
                    do {
                        uVar1 = uVar1 ^ uVar20 + uVar10;
                        uVar6 = uVar6 ^ uVar18 + uVar2;
                        uVar8 = uVar8 ^ uVar17 + uVar7;
                        uVar1 = uVar1 << 0x10 | uVar1 >> 0x10;
                        uVar6 = uVar6 << 0x10 | uVar6 >> 0x10;
                        uVar14 = uVar14 + uVar1;
                        uVar15 = uVar15 + uVar6;
                        uVar8 = uVar8 << 0x10 | uVar8 >> 0x10;
                        uVar11 = uVar10 ^ uVar14;
                        uVar9 = uVar2 ^ uVar15;
                        uVar19 = uVar19 + uVar8;
                        uVar12 = uVar11 << 0xc | uVar11 >> 0x14;
                        uVar9 = uVar9 << 0xc | uVar9 >> 0x14;
                        uVar11 = uVar7 ^ uVar19;
                        uVar20 = uVar20 + uVar10 + uVar12;
                        uVar18 = uVar18 + uVar2 + uVar9;
                        uVar11 = uVar11 << 0xc | uVar11 >> 0x14;
                        uVar1 = uVar1 ^ uVar20;
                        uVar6 = uVar6 ^ uVar18;
                        uVar17 = uVar17 + uVar7 + uVar11;
                        uVar2 = uVar1 << 8 | uVar1 >> 0x18;
                        uVar7 = uVar6 << 8 | uVar6 >> 0x18;
                        uVar8 = uVar8 ^ uVar17;
                        uVar14 = uVar14 + uVar2;
                        uVar15 = uVar15 + uVar7;
                        uVar12 = uVar12 ^ uVar14;
                        uVar9 = uVar9 ^ uVar15;
                        uVar12 = uVar12 << 7 | uVar12 >> 0x19;
                        uVar10 = uVar9 << 7 | uVar9 >> 0x19;
                        uVar8 = uVar8 << 8 | uVar8 >> 0x18;
                        uVar20 = uVar20 + uVar10;
                        uVar21 = uVar21 ^ uVar16 + uVar13;
                        uVar19 = uVar19 + uVar8;
                        uVar11 = uVar11 ^ uVar19;
                        uVar21 = uVar21 << 0x10 | uVar21 >> 0x10;
                        uVar1 = uVar11 << 7 | uVar11 >> 0x19;
                        local_64 = local_64 + uVar21;
                        uVar18 = uVar18 + uVar1;
                        uVar6 = uVar13 ^ local_64;
                        uVar2 = uVar2 ^ uVar18;
                        uVar9 = uVar6 << 0xc | uVar6 >> 0x14;
                        uVar6 = uVar2 << 0x10 | uVar2 >> 0x10;
                        uVar16 = uVar16 + uVar13 + uVar9;
                        uVar21 = uVar21 ^ uVar16;
                        uVar2 = uVar21 << 8 | uVar21 >> 0x18;
                        local_64 = local_64 + uVar2;
                        uVar2 = uVar2 ^ uVar20;
                        uVar13 = uVar2 << 0x10 | uVar2 >> 0x10;
                        uVar9 = uVar9 ^ local_64;
                        local_64 = local_64 + uVar6;
                        uVar19 = uVar19 + uVar13;
                        uVar9 = uVar9 << 7 | uVar9 >> 0x19;
                        uVar10 = uVar10 ^ uVar19;
                        uVar2 = uVar10 << 0xc | uVar10 >> 0x14;
                        uVar20 = uVar20 + uVar2;
                        uVar13 = uVar13 ^ uVar20;
                        uVar21 = uVar13 << 8 | uVar13 >> 0x18;
                        uVar19 = uVar19 + uVar21;
                        uVar2 = uVar2 ^ uVar19;
                        uVar2 = uVar2 << 7 | uVar2 >> 0x19;
                        uVar1 = uVar1 ^ local_64;
                        uVar17 = uVar17 + uVar9;
                        uVar10 = uVar1 << 0xc | uVar1 >> 0x14;
                        uVar7 = uVar7 ^ uVar17;
                        uVar18 = uVar18 + uVar10;
                        uVar13 = uVar7 << 0x10 | uVar7 >> 0x10;
                        uVar6 = uVar6 ^ uVar18;
                        uVar1 = uVar6 << 8 | uVar6 >> 0x18;
                        local_64 = local_64 + uVar1;
                        uVar10 = uVar10 ^ local_64;
                        uVar14 = uVar14 + uVar13;
                        uVar7 = uVar10 << 7 | uVar10 >> 0x19;
                        uVar16 = uVar16 + uVar12;
                        uVar9 = uVar9 ^ uVar14;
                        uVar8 = uVar8 ^ uVar16;
                        uVar9 = uVar9 << 0xc | uVar9 >> 0x14;
                        uVar8 = uVar8 << 0x10 | uVar8 >> 0x10;
                        uVar17 = uVar17 + uVar9;
                        uVar15 = uVar15 + uVar8;
                        uVar13 = uVar13 ^ uVar17;
                        uVar12 = uVar12 ^ uVar15;
                        uVar6 = uVar13 << 8 | uVar13 >> 0x18;
                        uVar10 = uVar12 << 0xc | uVar12 >> 0x14;
                        uVar14 = uVar14 + uVar6;
                        uVar16 = uVar16 + uVar10;
                        uVar9 = uVar9 ^ uVar14;
                        uVar8 = uVar8 ^ uVar16;
                        uVar13 = uVar9 << 7 | uVar9 >> 0x19;
                        uVar8 = uVar8 << 8 | uVar8 >> 0x18;
                        uVar15 = uVar15 + uVar8;
                        uVar10 = uVar10 ^ uVar15;
                        uVar10 = uVar10 << 7 | uVar10 >> 0x19;
                        local_5c = local_5c + -1;
                    } while (local_5c != 0);
                    param_1[0xc] = uVar1;
                    *param_1 = uVar20;
                    param_1[0xb] = local_64;
                    param_1[0xf] = uVar21;
                    param_1[10] = uVar19;
                    param_1[5] = uVar2;
                    param_1[1] = uVar18;
                    param_1[6] = uVar7;
                    param_1[2] = uVar17;
                    param_1[8] = uVar14;
                    param_1[7] = uVar13;
                    param_1[3] = uVar16;
                    param_1[9] = uVar15;
                    param_1[4] = uVar10;
                    param_1[0xe] = uVar8;
                    param_1[0xd] = uVar6;
                    puVar3 = param_1;
                    do {
                        puVar5 = puVar3 + 4;
                        *puVar3 = puVar3[0x20] + *puVar3;
                        puVar3[1] = puVar3[0x21] + puVar3[1];
                        puVar3[2] = puVar3[0x22] + puVar3[2];
                        puVar3[3] = puVar3[0x23] + puVar3[3];
                        puVar3 = puVar5;
                    } while (param_1 + 0x10 != puVar5);
                    puVar3 = param_1 + 0x2c;
                    *puVar3 = *puVar3 + 1;
                    if (*puVar3 == 0) {
                        puVar3 = param_1 + 0x2d;
                        *puVar3 = *puVar3 + 1;
                        if (*puVar3 == 0) {
                                    /* WARNING: Subroutine does not return */
                        __assert_fail("0 != counter[1]","chacha.c",0x50,"chacha20_block_next");
                        }
                    }
                    *(undefined8 *)(param_1 + 0x10) = 0;
                    puVar3 = param_1;
                    }
                    *local_58 = *local_58 ^ *(byte *)puVar3;
                    local_58 = local_58 + 1;
                    uVar4 = *(long *)(param_1 + 0x10) + 1;
                    *(ulong *)(param_1 + 0x10) = uVar4;
                } while (local_58 != param_2 + param_3);
                return
            ```

6. GAMEPLAN
   1. So reading through the code, it looks like we need to "re-run" the undead encryption 
   2. STEPS
      1. Rename our flag.txt.undead to just flag.txt
      2. Run our crypt program on the flag
         1. > ./crypt flag.txt
            1. SUCCESS - it undead-ified our flag
            2. Check the flag
               1. > cat flag.txt.undead
                  1. "HTB{und01ng_th3_curs3_0f_und34th}"
