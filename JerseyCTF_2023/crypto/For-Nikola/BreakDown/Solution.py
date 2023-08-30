import csv
import random


def encrypt(vis, K):
    r = ord("J")
    b = ord("0")
    d = r * b % 26
    e = d * r * b / (d % 3)
    g = random.seed(e)
    f = random.random()
    secXyz = ""
    Kl = len(K)
    K_sum = sum([ord(c) for c in K])
    for i, char in enumerate(vis):
        Cv = ord(char)
        Kc = K[i % Kl]
        vC = f * e
        K_Cv = ord(Kc)
        etTu = Cv + (K_sum * K_Cv)
        Dv = e % f
        flag = vC * Dv
        etTu = etTu % r
        etTu = etTu + b
        secXyz += chr(etTu)
        nC = (K_sum * K_Cv) % r + b
        flag = flag + ord(secXyz[0])
        nC = nC + Cv
    return secXyz


def encrypt_file(filename, K):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    newFilename = "testreturn.csv"
    with open(newFilename, "w", newline="") as outFile:
        writer = csv.writer(outFile)
        for row in rows:
            encrypted_row = [encrypt(cell, K) for cell in row]
            writer.writerow(encrypted_row)


def decrypt(secXyz, K):
    vis = ""
    Kl = len(K)
    K_sum = sum([ord(c) for c in K])
    for i, char in enumerate(secXyz):
        Cv = ord(char)
        Kc = K[i % Kl]
        K_Cv = ord(Kc)
        etTu = Cv - (K_sum * K_Cv) % 74 - 48
        if etTu < 48:
            etTu += 74
        vis += chr(etTu)
    return vis


def decrypt_file(filename, K):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
    newFile2 = "./decrypted.csv"
    with open(newFile2, "a", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            decrypted_row = [decrypt(cell, K) for cell in row]
            writer.writerow(decrypted_row)


def main():
    choice = input("Would you like to encrypt (1) or decrypt (2)? ")
    filename = input("Enter the full path of the file: ")
    K = input("Enter the K: ")
    if int(choice) == 1:
        encrypt_file(filename, K)
        print("Encryption complete!")
    elif int(choice) == 2:
        decrypt_file(filename, K)
        print("Decryption complete!")
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
