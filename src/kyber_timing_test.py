import timeit
import os

class Kyber512Sim:
    def keygen(self):
        public_key = os.urandom(800)
        secret_key = os.urandom(1632)
        return public_key, secret_key

    def encrypt(self, public_key):
        ciphertext = os.urandom(768)
        shared_secret = os.urandom(32)
        return ciphertext, shared_secret

    def decrypt(self, ciphertext, secret_key):
        return ciphertext[:32]

kem = Kyber512Sim()
pk, sk = kem.keygen()
ct, ss = kem.encrypt(pk)

# Ortalama süreyi hesapla
keygen_time = timeit.timeit(lambda: kem.keygen(), number=100) / 100
encrypt_time = timeit.timeit(lambda: kem.encrypt(pk), number=100) / 100
decrypt_time = timeit.timeit(lambda: kem.decrypt(ct, sk), number=100) / 100

print(f"Ortalama Anahtar Üretim Süresi: {keygen_time:.6f} saniye")
print(f"Ortalama Şifreleme Süresi: {encrypt_time:.6f} saniye")
print(f"Ortalama Şifre Çözme Süresi: {decrypt_time:.6f} saniye")
