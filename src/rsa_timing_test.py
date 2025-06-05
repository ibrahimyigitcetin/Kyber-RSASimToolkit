import timeit
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# RSA anahtarları oluştur
def keygen():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Şifreleme
def encrypt(public_key, plaintext):
    return public_key.encrypt(
        plaintext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

# Şifre çözme
def decrypt(private_key, ciphertext):
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

print("=== RSA Zaman Testi ===")

# Ortalama anahtar üretim süresi
keygen_time = timeit.timeit("keygen()", globals=globals(), number=10) / 10
print(f"Ortalama Anahtar Üretim Süresi: {keygen_time:.6f} saniye")

# Anahtarları oluştur
private_key = keygen()
public_key = private_key.public_key()

plaintext = "Test mesajı".encode('utf-8')

# Ortalama şifreleme süresi
encrypt_time = timeit.timeit("encrypt(public_key, plaintext)", globals=globals(), number=100) / 100
print(f"Ortalama Şifreleme Süresi: {encrypt_time:.6f} saniye")

# Şifrele
ciphertext = encrypt(public_key, plaintext)

# Ortalama şifre çözme süresi
decrypt_time = timeit.timeit("decrypt(private_key, ciphertext)", globals=globals(), number=100) / 100
print(f"Ortalama Şifre Çözme Süresi: {decrypt_time:.6f} saniye")
