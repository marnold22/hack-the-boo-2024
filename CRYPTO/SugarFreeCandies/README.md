# SugarFreeCandies

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: For years, strange signals pulsed through the air on the eve of October 31st. Some said it was the voice of an ancient witch, others believed it was a message from something far darker. A cryptic message, scattered in three parts, was intercepted by a daring group of villagers. Legend spoke of a deal made between the witch and a shadowy figure, but the true intent of their secret could only be revealed by those brave enough to decipher it before midnight, when the veil between worlds would thin.

## NOTES

1. Unzip challenge files
   1. > unzip crypto_sugar_free_candies.zip
      1. output.txt, source.py
2. OUTPUT.TXT
   1. Looking at this file we see:
      1. v1 = 4196604293528562019178729176959696479940189487937638820300425092623669070870963842968690664766177268414970591786532318240478088400508536
      2. v2 = 11553755018372917030893247277947844502733193007054515695939193023629350385471097895533448484666684220755712537476486600303519342608532236
      3. v3 = 14943875659428467087081841480998474044007665197104764079769879270204055794811591927815227928936527971132575961879124968229204795457570030
      4. v4 = 6336816260107995932250378492551290960420748628
3. SOURCE.PY
   1. Lets look at the code

        ```py
            from Crypto.Util.number import bytes_to_long

            FLAG = open("flag.txt", "rb").read()

            step = len(FLAG) // 3
            candies = [bytes_to_long(FLAG[i:i+step]) for i in range(0, len(FLAG), step)]

            cnd1, cnd2, cnd3 = candies

            with open('output.txt', 'w') as f:
                f.write(f'v1 = {cnd1**3 + cnd3**2 + cnd2}\n')
                f.write(f'v2 = {cnd2**3 + cnd1**2 + cnd3}\n')
                f.write(f'v3 = {cnd3**3 + cnd2**2 + cnd1}\n')
                f.write(f'v4 = {cnd1 + cnd2 + cnd3}\n')
        ```

        1. So lets piece together this code
4. CODE BREAKDOWN
   1. import libraries
   2. Open a flag.txt file as rb and save it to variable "FLAG"
   3. Set the "step" variable = the length of the flag divided by 3 (BUT TAKE THE FLOOR VALUE ie. round down)
      1. EXAMPLE: a // b    -> is equivilant to ->  floordiv(a, b)
   4. LOOP
      1. Loop through FLAG variable from i to lenth of flag in step increments
      2. Convert the values from bytes to long at i to i+step
   5. Output values in form of cnd1, cnd2, cnd3 and write to output.txt
