import random


def encrypt(vis, K):
    r = ord('J')
    b = ord('0')
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
