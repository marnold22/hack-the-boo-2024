# SpookyPass

## FLAG: HTB{un0bfu5c4t3d_5tr1ng5}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: All the coolest ghosts in town are going to a Haunted Houseparty - can you prove you deserve to get in?

## NOTES

1. Unzip challenge files
   1. > unzip rev_spookypass.zip
      1. This gives us just a "pass" file
2. MANUAL ENUMERATION
   1. FILE
      1. > file ./pass
         1. pass: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3008217772cc2426c643d69b80a96c715490dd91, for GNU/Linux 4.4.0, not stripped
   2. STRINGS
      1. > strings ./pass
         1. Ooo! We see some potentially useful strings

            ```text
                Before we let you in, you'll need to give us the password: 
                s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5
                Welcome inside!
                You're not a real ghost; clear off!
            ```

            1. So lets go run this to test
3. RUN
   1. > ./pass
      1. We are met with a prompt

        ```text
            Welcome to the SPOOKIEST party of the year.
            Before we let you in, you'll need to give us the password:
        ```

        1. Lets try using that password we saw from strings
   2. INPUT:
      1. s3cr3t_p455_f0r_gh05t5_4nd_gh0ul5
   3. OUTPUT
      1. Welcome in!
      2. HTB{un0bfu5c4t3d_5tr1ng5}
