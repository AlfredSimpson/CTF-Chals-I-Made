# Breaking JerseyCTF_2023 - For Nikola

For Nikola was used as a medium difficulty challenge at JerseyCTF. This received only 2 solutions throughout the course of the CTF, so I'm breaking down how to solve this here.

![image](https://github.com/AlfredSimpson/CTF-Chals-I-Made/assets/73041922/cb172524-10c0-4526-a16f-28b0bd74baaf)


# Step One - Examine the evidence

Examine the evidence! This provided multiple files: doodles.txt, encrypt.py, and mlist.csv.

- Doodles.txt
  - Doodles.txt contained the same phrase over and over and over again.
    ![image](https://github.com/AlfredSimpson/CTF-Chals-I-Made/assets/73041922/1b37e43d-8fdb-406e-9d13-a96eca058cab)
  - It's clear that this is just a simple cipher. If it wasn't clear, using cyberchef or dcode.fr/en would prove this!
  -   ![image](https://github.com/AlfredSimpson/CTF-Chals-I-Made/assets/73041922/979911d8-dd19-49ed-9b5e-17aa8e219e88)
  -   ![image](https://github.com/AlfredSimpson/CTF-Chals-I-Made/assets/73041922/0b996c54-59ef-481c-be23-9bb24e5142be)
  -   So now we know that the phrase repeated was TesalsRevenge.
# Step Two - Examine the Encryption
- Encrypt.py
  - Now we can look at encrypt.py and see what's happening there.
  - ![image](https://github.com/AlfredSimpson/CTF-Chals-I-Made/assets/73041922/f2ee6558-3c4d-4411-9102-1873e7cc37bc)
  - Line by line, this is what is happening:
  - r = ord('J'): ASCII value of 'J'(74) stored in 'r'.
    - **r = 74**
  - b = ord('O'): ASCII value of 'O'(48) stored in 'b'.
    - **b = 48**
  - d = r * b % 26: Modulo operation on 74 x 48 stored in 'd'.
    - This is 74 * 48 % 26.
    - **d = 16.**
  - e = d * r * b / (d%3): We multiple d by r by b over b mod 3,
    - A little deeper, this is e = 16  * 74 * 48 / (16 % 3)
    - 56832 / (16 % 3)
    - 56832 / 1
    - Therefore, **e = 56832**
  - g = random.seed(e)
    - This generates a random seed with the value of e.
    - It is also useless.
  - f = random.random()
    - This generates a random number and assigns it to f.
  - secXYZ is an empty string.
  - Kl = len(K)
    - K is passed to us in the parameters, so is word dependent.
  - K_sum = sum([ord(c) for c in K])
    - Sums the ASCII values of all characters in 'K'.
  - Outside of the loop is finished and we now have some base values. Inside it's further revealed:
    - Cv = ord(char)
      - Again, we're taking the ASCII value of whatever character is being iterated over
    - Kc = K[i % Kl]:
      - Current character in the key K.
    - vC = f * e:
      - Some arithmetic operation stored in vC.
    - K_Cv = ord(Kc):
      - ASCII value of the current key character.
    - etTu = Cv + (K_sum * K_Cv):
      - Arithmetic operation on the ASCII value of the current character and key.
    - Dv = e % f:
      - Another arithmetic operation stored in Dv.
    - flag = vC * Dv:
      - Unused operation stored in flag.
    - etTu = etTu % r:
      - Take modulo of etTu by r.
    - etTu = etTu + b:
      - Add b to etTu.
    - secXyz += chr(etTu):
      - Append the new character to the encrypted text.
    - nC = (K_sum * K_Cv) % r + b:
      - Another unused operation stored in nC.
    - flag = flag + ord(secXyz[0]):
      - Another unused operation affecting flag.
    - nC = nC + Cv:
      - Another unused operation affecting nC.  
    - Finally, we return secXyz
  
  # Step Three: Reverse the encryption
  - With the encryption method revealed (and obfuscation ignored), we can reverse the encryption. Here's an example of how I personally decrypted:
    - ![image](https://github.com/AlfredSimpson/CTF-Chals-I-Made/assets/73041922/2158d874-db72-43c0-a9d2-de2537b1b4bf)

  # Step Four: Decrypt
  - Use the key found in doodles.txt (TeslasRevenge) to decrypt the files

  # Step Five: Submit your flag
  - Once done, you'll find the flag: jctf{T1M3_TRAV3L_RUL35}
 



