from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

print("=== RSA Çıktı Boyutu Testi ===")

# Anahtarlar
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# Key byte formatında
private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Şifreleme
plaintext = b"Test message for RSA"
ciphertext = public_key.encrypt(
    plaintext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print(f"Public Key boyutu: {len(public_bytes)} byte")
print(f"Private Key boyutu: {len(private_bytes)} byte")
print(f"Ciphertext boyutu: {len(ciphertext)} byte")
print(f"Plaintext boyutu: {len(plaintext)} byte")
