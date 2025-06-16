import math

def period_finding(a, N):
    # Shor'un periyot bulma adımını simüle eder (basitleştirilmiş)
    r = 1
    while pow(a, r, N) != 1:
        r += 1
    return r

def shor_classical(N):
    # N=15 için çarpanlara ayırma
    for a in range(2, N):
        if math.gcd(a, N) > 1:
            return math.gcd(a, N), N // math.gcd(a, N)
    # Periyot bulma (basitleştirilmiş)
    a = 2
    r = period_finding(a, N)
    if r % 2 == 0:
        p = math.gcd(pow(a, r//2) - 1, N)
        q = math.gcd(pow(a, r//2) + 1, N)
        if p * q == N:
            return p, q
    return None

# Test
N = 15
factors = shor_classical(N)
print(f"Çarpanlar: {factors}")  # Çıktı: (3, 5)