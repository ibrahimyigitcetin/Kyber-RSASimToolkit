import psutil
import os
import time
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

process = psutil.Process(os.getpid())

print("=== RSA Bellek Kullanımı Testi ===")

start_mem = process.memory_info().rss / 1024
print(f"Başlangıç Bellek Kullanımı: {start_mem:.2f} KB")

# Anahtar üretimi
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
mem_after_keygen = process.memory_info().rss / 1024
print(f"Anahtar Üretimi Sonrası Bellek: {mem_after_keygen:.2f} KB")

# Şifreleme
public_key = private_key.public_key()
plaintext = b"Test message for RSA"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
mem_after_encrypt = process.memory_info().rss / 1024
print(f"Şifreleme Sonrası Bellek: {mem_after_encrypt:.2f} KB")

# Şifre çözme
decrypted = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
mem_after_decrypt = process.memory_info().rss / 1024
print(f"Şifre Çözme Sonrası Bellek: {mem_after_decrypt:.2f} KB")
