import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

class Kyber512Sim:
    # Bu sınıf Kyber'i simüle etmeye devam edecek
    def keygen(self):
        pk = os.urandom(800)  # Kyber512 public key boyutu (simüle edilmiş)
        sk = os.urandom(1632) # Kyber512 secret key boyutu (simüle edilmiş)
        return pk, sk

    def encrypt(self, pk):
        # pk'yi kullanmıyoruz, sadece simülasyon olduğu için
        ct = os.urandom(768)  # Kyber512 ciphertext boyutu (simüle edilmiş)
        ss = os.urandom(32)   # Kyber512 shared secret boyutu (simüle edilmiş)
        return ct, ss

    def decrypt(self, ct, sk):
        # ct ve sk'yi kullanmıyoruz, sadece simülasyon olduğu için
        return os.urandom(32) # Kyber512 shared secret boyutu (simüle edilmiş)

class RSASim:
    def keygen(self):
        # 2048-bit RSA anahtar çifti oluşturma
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Anahtarları PEM formatında serileştirme (byte olarak göndermek için)
        pem_public_key = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        pem_private_key = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        return pem_public_key, pem_private_key

    def encrypt(self, pem_public_key):
        # Public key'i deserializasyon
        public_key = serialization.load_pem_public_key(
            pem_public_key,
            backend=default_backend()
        )
        # Shared secret olarak kullanılacak rastgele bir veri oluştur (örneğin 32 byte)
        shared_secret = os.urandom(32)
        
        # RSA ile şifreleme (OAEP padding kullanarak)
        ciphertext = public_key.encrypt(
            shared_secret,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return ciphertext, shared_secret

    def decrypt(self, ciphertext, pem_private_key):
        # Private key'i deserializasyon
        private_key = serialization.load_pem_private_key(
            pem_private_key,
            password=None,
            backend=default_backend()
        )
        # RSA ile şifre çözme (OAEP padding kullanarak)
        decrypted_shared_secret = private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted_shared_secret

