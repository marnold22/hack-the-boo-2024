# SekurJulius

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: Hidden deep in the forest was an ancient scroll, rumored to grant immense power to anyone who could read its shifting symbols. On Halloween, a curious traveler found the scroll, its letters strangely out of order. As they deciphered the message, the words slowly rearranged themselves, revealing a dark spell. But with the final shift, the traveler felt a cold presence behind them, whispering, 'You were never meant to understand.' The forest grew silent, but the spell was already cast.

## NOTES

1. Unzip challenge files
   1. > unzip crypto_sekur_julius.zip
      1. outptu.txt, source.py
2. OUTPUT.TXT
3. SOURCE.PY
   1. Lets take a look at the source code

        ```py
            from random import choices

            def julius_encrypt(msg, shift):
                ct = ''
                for p in msg:
                    if p == ' ':
                        ct += '0'
                    elif not ord('A') <= ord(p) <= ord('Z'):
                        ct += p
                    else:
                        o = ord(p) - 65
                        ct += chr(65 + (o + shift) % 26)
                return ct

            def encrypt(msg, key):
                for shift in key:
                    msg = julius_encrypt(msg, shift)
                return msg

            msg = open('secret.txt').read().upper()
            secure_key = os.urandom(1337)

            with open('output.txt', 'w') as f:
                f.write(encrypt(msg, secure_key))
        ```

4. CODE BREAKDOWN
   1. import library
   2. Define the julius_encrypt() function -> **NOTE: Julius might be a hint at Julius Ceaser or rather a Ceaser Cipher**
      1. The function takes in 2 variables:
         1. message and shift
      2. set ct = empty string (cipher text)
      3. LOOP
         1. for some variable p in msg (I am assuming p is place or position)
            1. IF p == a space ' ' 
               1. THEN append 0 to our ct (cipher text)
            2. ELSEIF NOT ordinal value of 'A' lessthan or equal to ordinal value of p lessthan or equal to oridnal value of 'Z'
               1. THEN append p to our ct (cipher text)
            3. ELSE
               1. set o = to ordinal value of p -65
               2. append the character value of (65+ (o+shift) %26)
                  1. The mod 26 is becuase of 26 characters in the alphabet
            4. RETURN
               1. return our ciphertext
   3. Define encrypt() function
      1. The function takes in 2 variables:
         1. message and key
      2. LOOP
         1. For 'shift' in key (which chould act like posision in key)
            1. message = julius_encrypt(msg, shift)
         2. RETURN
            1. return our message (msg)
   4. open up out secret.txt file and set it equal to our message (msg) variable
   5. generate secure_key by getting a random string of 1337 bytes from os.urandom(1337)
   6. open up output.txt
      1. write the encrypted value of our message