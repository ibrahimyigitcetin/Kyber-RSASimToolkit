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

📁 `sim_and_test_files/kyber512_sim.py`

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

📁 `sim_and_test_files/kyber_timing_test.py`

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

📁 `sim_and_test_files/rsa_timing_test.py`

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

📁 `sim_and_test_files/kyber_memory_test.py`

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

📁 `sim_and_test_files/rsa_memory_test.py`

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

📁 `sim_and_test_files/kyber_output_size_test.py`

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

📁 `sim_and_test_files/rsa_output_size_test.py`

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

## Karşılaştırmalı Raporlama

📄 `kyber_and_rsa_results.md` içeriğinde:

- Kyber ve RSA zamanlamaları (keygen/encrypt/decrypt süreleri)
- Bellek kullanımı analizleri
- Çıktı boyutu karşılaştırmaları
- Grafikler/tablolarla özetlenmiş veriler

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

## Sonuç

Bu yol haritası ile post-kuantum ve klasik şifreleme algoritmalarının temel simülasyonlarını geliştirdiniz, performanslarını ölçtünüz ve karşılaştırdınız. Gelecekte, bu altyapı üzerine gerçek kriptografik kütüphanelerle performans testlerini entegre etmek mümkündür.

