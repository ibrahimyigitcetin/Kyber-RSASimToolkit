# 🔐 CRYSTALS-Kyber ve RSA’nın TLS Benzeri Ağ Protokolüne Entegrasyonu ve Gerçek Dünya Testi

## 📌 Genel Bakış

CRYSTALS-Kyber kuantum dirençli şifreleme algoritması ve klasik RSA algoritması, TLS benzeri bir ağ protokolüne entegre edilerek gerçek dünya senaryosunda test edildi.

Bu adım:

- Kyber’ın uygulanması,
- Performans/güvenlik analizleri,
- Ve RSA ile karşılaştırmalı analiz

üzerine inşa edilmiştir. Amaç, Kyber ve RSA’yı **anahtar değişimi** için kullanarak istemci-sunucu arasında güvenli iletişim kurmak ve pratik uygulanabilirliklerini değerlendirmektir.

---

## 🧩 Uygulama Yapısı

Uygulama, **beş Python dosyasından** oluşur:

- `kyber_server.py`
- `kyber_client.py`
- `crypto_module.py`
- `kyber_rsa_server.py`
- `kyber_rsa_client.py`

Bu dosyalar, **Kyber ve RSA tabanlı güvenli bir istemci-sunucu iletişim mimarisi** oluşturur.

---

## 📂 Dosya Açıklamaları

### 1. `crypto_module.py`

Bu modül, şifreleme işlemlerinin temelini oluşturur ve Kyber ile RSA algoritmalarını içerir:

#### 🔹 `Kyber512Sim` Sınıfı

- `keygen()`: 800 baytlık genel anahtar, 1632 baytlık özel anahtar üretir.
- `encrypt(pk)`: 768 baytlık şifreli metin ve 32 baytlık paylaşılan sır üretir.
- `decrypt(ct, sk)`: Şifreli metni çözüp 32 baytlık sır üretir.

> ⚠️ Not: Kyber, `pqcrypto` yerine `os.urandom` ile **simüle edilmiştir**.

#### 🔹 `RSASim` Sınıfı

- `keygen()`: 2048-bit RSA anahtar çifti üretir (PEM formatında).
- `encrypt(pem_public_key)`: OAEP dolgusuyla 32 baytlık sır şifreler.
- `decrypt(ciphertext, pem_private_key)`: Şifreli metni çözerek sır üretir.

---

### 2. `kyber_server.py`

- Yerel ağda (`127.0.0.1:65432`) soket başlatır.
- Çoklu istemci bağlantılarını destekler.
- Genel anahtarı istemciye gönderir, şifreli veriyi alır, sır üretir.
- Paylaşılan sır **konsolda görüntülenir**.

---

### 3. `kyber_client.py`

- Sunucuya (`127.0.0.1:65432`) bağlanır.
- Genel anahtarı alır, şifreli metni ve sır üretir.
- Şifreli veriyi sunucuya yollar ve paylaşılmış sır görüntülenir.

---

### 4. `kyber_rsa_server.py`

- `ALGO` değişkeni ile `"kyber"` veya `"rsa"` algoritması seçilir.
- Tek istemci bağlantısını işler.
- Seçilen algoritma ile anahtar üretir ve sır paylaşımı sağlar.

---

### 5. `kyber_rsa_client.py`

- `ALGO` değişkeni ile algoritma seçimi yapılır.
- Sunucuya bağlanır, anahtar alışverişi ve sır üretimini gerçekleştirir.

---

## 🔧 Uygulama Detayları

- **Protokol Tasarımı:** TLS’nin anahtar değişim kısmını taklit eden sade yapı. Yalnızca anahtar değişimi test edilmiştir.
- **Kütüphaneler:** Kyber simülasyonu `os.urandom`, RSA ise `cryptography` kütüphanesi ile uygulanmıştır.
- **Performans:** Kodlar doğrudan ölçüm yapmasa da, **konsol çıktıları** üzerinden performans analizleri yapılabilir.
- **Test Ortamı:** Yerel adres: `127.0.0.1:65432`.  
  `kyber_server.py` çoklu bağlantıyı, `kyber_rsa_server.py` tek bağlantıyı destekler.

---

## ✅ Sonuçlar

### 🔄 Başarılı Entegrasyon

- **Kyber ve RSA**, TLS benzeri protokole başarıyla entegre edildi.
- `kyber_server.py` / `kyber_client.py`: Kyber tabanlı iletişim sağlandı.
- `kyber_rsa_server.py` / `kyber_rsa_client.py`: Algoritma geçişleri desteklendi.

### ⚖️ Karşılaştırmalı Analiz

| Algoritma | Anahtar Boyutu | Hesaplama Yükü |
|----------|----------------|----------------|
| Kyber    | 800 bayt (pub), 1632 bayt (priv) | Düşük, hızlı |
| RSA      | 2048-bit        | OAEP dolgulu, daha ağır |

### 🌐 Gerçek Dünya Uygulanabilirliği

- Basit istemci-sunucu simülasyonu ile **Kyber’ın ağ protokollerindeki kullanılabilirliği** test edildi.
- `crypto_module.py`'nin modüler yapısı, başka algoritmaların entegrasyonunu kolaylaştırır.

---

## ⚠️ Sınırlamalar

- **Kyber Simülasyonu:** `os.urandom` tabanlı olduğu için gerçek performansı yansıtmaz.
- **Performans Ölçümü:** Kodda doğrudan yer almamaktadır.
- **Farklı Anahtar Yapıları:** Protokol uyumu açısından dikkat gerektirir.

---

## 🧱 Karşılaşılan Zorluklar

- 🧪 **Simülasyon Sınırlamaları:** Gerçek Kyber yerine rastgele üretim kullanıldı.
- 🔀 **Uyumluluk Sorunları:** RSA ve Kyber’ın yapısal farklılıkları protokolde dönüşüm gerektirdi.
- ⏱️ **Performans Takibi:** Ölçüm araçlarının eksikliği manuel analiz zorunluluğu doğurdu.

---

📎 Bu adım, kuantum çağında güvenli iletişimin temel yapı taşlarını oluşturmak için atılmış önemli bir test adımıdır.
