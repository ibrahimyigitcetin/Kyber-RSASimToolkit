# Kyber-RSASim Toolkit ile Kuantum Dirençli Şifreleme ve Klasik Şifreleme Testlerini Geliştirme ve Karşılaştırma

## Giriş

Bu yol haritası, kuantum dirençli **CRYSTALS-Kyber (Kyber512)** algoritmasının Python tabanlı simülasyonunu geliştirmeyi ve bu simülasyonu geleneksel **RSA-2048** algoritması ile karşılaştırmayı detaylı bir şekilde sunar.

> ⚠️ **Önemli Uyarı:** Bu bilgiler yalnızca eğitim ve araştırma amaçlıdır. Gerçek ağlarda veya sistemlerde yetkisiz kullanım yasa dışı ve etik dışıdır. Testler yalnızca açık izin alınmış kontrollü ortamlarda yapılmalıdır.

Bu rehber, post-kuantum şifreleme ve klasik şifreleme algoritmalarının **zamanlama performansını**, **bellek kullanımını** ve **çıktı boyutlarını** karşılaştırmak, simüle etmek ve analiz etmek için etik ve yasal sınırlar içinde bir yol haritası sunar.

---

## Ön Koşullar

### Yazılım

- **Python 3.x**: Geliştirme ve simülasyonlar için temel dil (önerilen sürüm: `3.11.9`).
- **Kütüphaneler**:
  - `psutil`: Bellek kullanımı ölçümü için (`pip install psutil`)
  - `cryptography`: RSA işlemleri için (`pip install cryptography`)
  - `os`, `timeit`: Zamanlama ve simülasyon için (standart Python modülleri)

### Bilgi Gereksinimleri

- Python programlama temelleri
- Kriptografi ve post-kuantum algoritmalar (Kyber, RSA) hakkında temel bilgi
- Dosya sistemi ve sanal ortam yönetimi

### Araçlar

- Python `venv` modülü
- Metin editörü (VS Code, PyCharm, vb.)

---

## Test Ortamını Kurma

### Sanal Ortam Kurulumu

```bash
python -m venv venv
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### Bağımlılıkları Yükleme

```bash
pip install psutil cryptography
```

> Testler için fiziksel bir ağa ihtiyaç yoktur; tüm simülasyonlar yerel olarak gerçekleştirilir.

---

## Temel Bileşenlerin Geliştirilmesi

### 1. Kyber512 Simülasyon Betiği

📁 `src/kyber512_sim.py`

```python
import os
import time

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

def main():
    output_lines = []
    def print_and_log(text):
        print(text)
        output_lines.append(text)

    print_and_log("=== Kyber512 Saf Python Simülasyonu Başladı ===")
    kem = Kyber512Sim()

    start_time = time.time()
    pk, sk = kem.keygen()
    print_and_log(f"Anahtarlar üretildi: Public Key({len(pk)} bytes), Secret Key({len(sk)} bytes)")

    ct, ss_enc = kem.encrypt(pk)
    print_and_log(f"Şifreleme tamamlandı: Ciphertext({len(ct)} bytes), Shared Secret({len(ss_enc)} bytes)")

    ss_dec = kem.decrypt(ct, sk)
    print_and_log(f"Şifre çözme tamamlandı: Shared Secret({len(ss_dec)} bytes)")

    if ss_enc == ss_dec:
        print_and_log("✅ Doğruluk testi geçti.")
    else:
        print_and_log("⚠️ Doğruluk testi başarısız (simülasyondan dolayı olağan sonuç).")

    end_time = time.time()
    print_and_log(f"Toplam işlem süresi: {end_time - start_time:.4f} saniye")

    with open("kyber512_test_results.txt", "w", encoding="utf-8") as f:
        for line in output_lines:
            f.write(line + "\n")

if __name__ == "__main__":
    main()
```

---

### 2. Kyber512 Zaman Ölçüm Betiği

📁 `src/kyber_timing_test.py`

```python
import timeit
import os

class Kyber512Sim:
    def keygen(self):
        return os.urandom(800), os.urandom(1632)

    def encrypt(self, pk):
        return os.urandom(768), os.urandom(32)

    def decrypt(self, ct, sk):
        return ct[:32]

kem = Kyber512Sim()
pk, sk = kem.keygen()
ct, _ = kem.encrypt(pk)

keygen_time = timeit.timeit(lambda: kem.keygen(), number=100) / 100
encrypt_time = timeit.timeit(lambda: kem.encrypt(pk), number=100) / 100
decrypt_time = timeit.timeit(lambda: kem.decrypt(ct, sk), number=100) / 100

print(f"Anahtar Üretimi: {keygen_time:.6f} s")
print(f"Şifreleme: {encrypt_time:.6f} s")
print(f"Şifre Çözme: {decrypt_time:.6f} s")
```

---

### 3. RSA-2048 Zaman Ölçüm Betiği

📁 `src/rsa_timing_test.py`

```python
import timeit
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def keygen():
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)

def encrypt(public_key, plaintext):
    return public_key.encrypt(plaintext, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

def decrypt(private_key, ciphertext):
    return private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

print("=== RSA Zaman Testi ===")

keygen_time = timeit.timeit("keygen()", globals=globals(), number=10) / 10
print(f"Anahtar Üretimi: {keygen_time:.6f} s")

private_key = keygen()
public_key = private_key.public_key()
plaintext = b"Test mesajı"

encrypt_time = timeit.timeit("encrypt(public_key, plaintext)", globals=globals(), number=100) / 100
ciphertext = encrypt(public_key, plaintext)

decrypt_time = timeit.timeit("decrypt(private_key, ciphertext)", globals=globals(), number=100) / 100

print(f"Şifreleme: {encrypt_time:.6f} s")
print(f"Şifre Çözme: {decrypt_time:.6f} s")
```

---

## Gelişmiş Testler

### Kyber512 Bellek Kullanımı

📁 `src/kyber_memory_test.py`

```python
import os
import psutil
from kyber512_sim import Kyber512Sim

def memory_usage():
    return psutil.Process(os.getpid()).memory_info().rss / 1024

kem = Kyber512Sim()
print("=== Bellek Kullanımı Testi ===")

print(f"Başlangıç: {memory_usage():.2f} KB")
kem.keygen()
print(f"Anahtar Üretimi: {memory_usage():.2f} KB")
kem.encrypt(os.urandom(800))
print(f"Şifreleme: {memory_usage():.2f} KB")
kem.decrypt(os.urandom(768), os.urandom(1632))
print(f"Şifre Çözme: {memory_usage():.2f} KB")
```

---

### RSA Bellek Kullanımı

📁 `src/rsa_memory_test.py`

```python
import psutil, os
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

process = psutil.Process(os.getpid())

print("=== RSA Bellek Kullanımı ===")
print(f"Başlangıç: {process.memory_info().rss / 1024:.2f} KB")

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
print(f"Anahtar Üretimi: {process.memory_info().rss / 1024:.2f} KB")

public_key = private_key.public_key()
ciphertext = public_key.encrypt(b"Test", padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
print(f"Şifreleme: {process.memory_info().rss / 1024:.2f} KB")

private_key.decrypt(ciphertext, padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))
print(f"Şifre Çözme: {process.memory_info().rss / 1024:.2f} KB")
```

---

## Çıktı Boyutları

### Kyber512 Çıktı Analizi

📁 `src/kyber_output_size_test.py`

```python
from kyber512_sim import Kyber512Sim

kem = Kyber512Sim()
pk, sk = kem.keygen()
ct, ss = kem.encrypt(pk)

print(f"Public Key: {len(pk)} byte")
print(f"Secret Key: {len(sk)} byte")
print(f"Ciphertext: {len(ct)} byte")
print(f"Shared Secret: {len(ss)} byte")
```

---

### RSA-2048 Çıktı Analizi

📁 `src/rsa_output_size_test.py`

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

private_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

public_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

ciphertext = public_key.encrypt(b"Test message", padding.OAEP(mgf=padding.MGF1(hashes.SHA256()), algorithm=hashes.SHA256(), label=None))

print(f"Public Key: {len(public_bytes)} byte")
print(f"Private Key: {len(private_bytes)} byte")
print(f"Ciphertext: {len(ciphertext)} byte")
print(f"Plaintext: {len(b'Test message')} byte")
```

---

## Test Aşamaları

| Test Betiği                        | Dosya                            | Çıktı/Kontrol                                       |
|-----------------------------------|----------------------------------|-----------------------------------------------------|
| Kyber Simülasyon                  | kyber512_sim.py                  | `kyber512_test_results.txt`                        |
| Kyber Zaman Testi                 | kyber_timing_test.py             | Ortalama süreler                                    |
| RSA Zaman Testi                   | rsa_timing_test.py               | Ortalama süreler                                    |
| Kyber Bellek Testi                | kyber_memory_test.py             | Bellek tüketimi (KB)                                |
| RSA Bellek Testi                  | rsa_memory_test.py               | Bellek tüketimi (KB)                                |
| Kyber Çıktı Boyutu Testi          | kyber_output_size_test.py        | 800, 1632, 768, 32 byte                             |
| RSA Çıktı Boyutu Testi            | rsa_output_size_test.py          | 256 byte ciphertext, ~1700 byte private key         |

---



## 🔗 Socket Tabanlı Kyber512 Simülasyonu

Kyber512 algoritmasının ağ üzerinden nasıl kullanılabileceğini test etmek amacıyla, basit bir istemci-sunucu mimarisi kurulmuştur. Bu yapı, `socket` ve `threading` modülleri ile çalışmakta, istemciye public key gönderip, istemciden ciphertext alarak shared secret üretmektedir.

> ❗ Bu yapı sadece eğitim ve test amaçlıdır. Gerçek şifreleme sistemleri için ağ güvenliği ve kimlik doğrulama katmanları da gereklidir.

---

### 📁 src/kyber_server.py

```python
import socket
import threading
from kyber512_sim import Kyber512Sim

HOST = '127.0.0.1'
PORT = 65432

kem = Kyber512Sim()
public_key, secret_key = kem.keygen()

def handle_client(conn, addr):
    print(f"[+] {addr} bağlandı.")

    conn.sendall(public_key)
    print("[>] Public key gönderildi.")

    ciphertext = conn.recv(1024)
    print("[<] Ciphertext alındı.")

    shared_secret = kem.decrypt(ciphertext, secret_key)
    print(f"[✓] Shared secret (server): {shared_secret.hex()}")

    conn.close()
    print(f"[-] {addr} bağlantısı kapatıldı.")

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"[⚡] Sunucu {HOST}:{PORT} dinleniyor...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()
```
### 📁 src/kyber_client.py

```python
import socket
from kyber512_sim import Kyber512Sim

HOST = '127.0.0.1'
PORT = 65432

kem = Kyber512Sim()

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        public_key = s.recv(1024)
        print("[<] Public key alındı.")

        ciphertext, shared_secret = kem.encrypt(public_key)
        print(f"[✓] Shared secret (client): {shared_secret.hex()}")

        s.sendall(ciphertext)
        print("[>] Ciphertext gönderildi.")

if __name__ == "__main__":
    start_client()
```

## 🧪 Test Senaryosu

| Rol     | Script            | Açıklama                                                                 |
|---------|-------------------|--------------------------------------------------------------------------|
| Sunucu  | `kyber_server.py` | Kyber512 public key gönderir, ciphertext alır, shared secret üretir.    |
| İstemci | `kyber_client.py` | Public key alır, shared secret üretir ve ciphertext gönderir.           |

🔐 Bu yapı, TLS-benzeri key exchange yapılarının temelini anlamak için iyi bir örnektir.

---

## 🔁 RSA ve Kyber512 Tabanlı Plug-in Anahtar Paylaşım Modülü

Bu bölümde, hem geleneksel RSA algoritmasını hem de post-kuantum CRYSTALS-Kyber512 algoritmasını destekleyen modüler ve değiştirilebilir bir istemci-sunucu altyapısı tanımlanmıştır.

Bu yapı sayesinde sadece bir parametre (ALGO) değiştirilerek farklı algoritmalar kolayca test edilebilir.

⚙️ Kullanıcı, `ALGO = "rsa"` veya `ALGO = "kyber"` olarak algoritmayı belirler.

---

### 📁 src/crypto_module.py

```python
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

class Kyber512Sim:
    def keygen(self):
        pk = os.urandom(800)   # Simüle edilmiş public key
        sk = os.urandom(1632)  # Simüle edilmiş secret key
        return pk, sk

    def encrypt(self, pk):
        ct = os.urandom(768)
        ss = os.urandom(32)
        return ct, ss

    def decrypt(self, ct, sk):
        return os.urandom(32)

class RSASim:
    def keygen(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()
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
        public_key = serialization.load_pem_public_key(pem_public_key, backend=default_backend())
        shared_secret = os.urandom(32)
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
        private_key = serialization.load_pem_private_key(pem_private_key, password=None, backend=default_backend())
        return private_key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
```

### 📁 src/kyber_rsa_server.py

```python
import socket
from crypto_module import Kyber512Sim, RSASim

ALGO = "kyber"  # Değiştirilebilir: "rsa" / "kyber"
PORT = 65432

algo = Kyber512Sim() if ALGO == "kyber" else RSASim()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', PORT))
    s.listen()
    print(f"[🔌] Sunucu dinlemede ({ALGO.upper()} modu)...")
    conn, addr = s.accept()
    with conn:
        print(f"[+] Bağlantı: {addr}")
        pk, sk = algo.keygen()
        conn.sendall(pk)
        ct = conn.recv(2048)
        ss = algo.decrypt(ct, sk)
        print(f"[🔐] Shared Secret (Server): {ss.hex()}")
```

### 📁 src/kyber_rsa_client.py

```python
import socket
from crypto_module import Kyber512Sim, RSASim

ALGO = "kyber"  # Değiştirilebilir: "rsa" / "kyber"
PORT = 65432

algo = Kyber512Sim() if ALGO == "kyber" else RSASim()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', PORT))
    pk = s.recv(2048)
    ct, ss = algo.encrypt(pk)
    print(f"[🔐] Shared Secret (Client): {ss.hex()}")
    s.sendall(ct)
```

## ✅ Test Durumları

| Senaryo         | Ayar          | Açıklama                                |
|-----------------|---------------|----------------------------------------|
| ALGO = "kyber"  | Post-kuantum test | Kyber512 key exchange simülasyonu yapılır. |
| ALGO = "rsa"    | Geleneksel algoritma testi | RSA ile shared secret aktarımı test edilir. |

---

### 🧠 Fayda

Bu yapı sayesinde aynı test ortamı kullanılarak hem klasik RSA hem de post-kuantum Kyber algoritmalarının karşılaştırmalı performans ve işlev testleri yapılabilir.

---

## ⚠️ Shor Algoritması ile Kuantum Saldırı Simülasyonu (Klasik Model)

Bu adımda, RSA algoritmasının kuantum bilgisayarlar tarafından nasıl kırılabileceğini göstermek amacıyla, Shor algoritmasının klasik (simüle edilmiş) bir versiyonu uygulanmıştır. Gerçek Shor algoritması kuantum devreleriyle çalışsa da, burada simülasyon yalnızca küçük sayılarla sınırlıdır (N = 15, N = 21, vb.).

---

### 📁 src/shor_classical_sim.py

```python
import math

def period_finding(a, N):
    r = 1
    while pow(a, r, N) != 1:
        r += 1
    return r

def shor_classical(N):
    for a in range(2, N):
        if math.gcd(a, N) > 1:
            return math.gcd(a, N), N // math.gcd(a, N)
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
print(f"Çarpanlar: {factors}")
```

---

### 🧪 Örnek Çıktı

`Çarpanlar: (3, 5)`

### 📝 Notlar:

- Bu simülasyon, RSA'nın kuantum saldırılara karşı kırılgan yapısını teorik olarak göstermeyi amaçlar.
- Gerçek kuantum Shor algoritması çok daha büyük N değerleri için kuantum Fourier dönüşümü ile çalışır.
- CRYSTALS-Kyber gibi MLWE tabanlı algoritmalar bu tür kuantum saldırılara karşı dirençlidir.
