<div align="center">
  <img src="https://img.shields.io/github/languages/count/ibrahimyigitcetin/Kyber-RSASimToolkit?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/ibrahimyigitcetin/Kyber-RSASimToolkit?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/ibrahimyigitcetin/Kyber-RSASimToolkit?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/ibrahimyigitcetin/Kyber-RSASimToolkit?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# 🔐 Kyber-RSASimToolkit

**Kyber-RSASimToolkit**, kuantum dirençli şifreleme algoritması **CRYSTALS-Kyber** ile geleneksel **RSA** algoritmasını karşılaştırmalı olarak test etmeye yönelik geliştirilen bir simülasyon aracıdır. Bu araç, gerçek dünya senaryolarına uygun olarak soket üzerinden anahtar değişimi, şifreleme ve performans ölçümü gerçekleştirir.

---

## 📌 Proje Hakkında

Bu araç; post-kuantum (PQC) ve klasik kriptografi çözümlerinin:
- Gerçek zamanlı şifreleme/deşifreleme senaryolarında nasıl davrandığını,
- Hız, güvenlik, bellek ve çıktı boyutu açısından kıyaslanmasını,
- Teorik kuantum saldırılarına (Shor algoritması gibi) karşı güvenliğini,

incelemek ve görselleştirmek amacıyla Python diliyle geliştirilmiştir.

---

## ⚙️ Kullanılan Teknolojiler

- 🔐 **CRYSTALS-Kyber512** (NIST PQC Standardı)
- 🔐 **RSA-2048** (Klasik açık anahtarlı şifreleme)
- 🐍 **Python 3.10+**
- 🧪 `socket`, `time`, `secrets`, `Crypto`, `numpy` (opsiyonel)
- 📦 CLI tabanlı kullanıcı etkileşimi
- 🔌 Gerçek zamanlı soket iletişimi (server ↔ client)

---

## ✨ Temel Özellikler

- **NIST Dokümantasyonu:** NIST Kuantum Sonrası Şifreleme standartları ve algoritma seçim sürecinin detaylı dokümantasyonu.

- **Kyber512 Simülasyonu:** Kyber512'nin yapısal ve performans testleri için simülasyonu.  

- **Karşılaştırmalı Analiz:** Kyber512 ve RSA-2048'in hız, bellek ve çıktı boyutları açısından karşılaştırmalı analizi.  

- **Anahtar Üretimi ve Şifreleme:** RSA ve Kyber algoritmaları kullanılarak güvenli anahtar üretimi ve mesaj şifreleme senaryoları.  

- **Sunucu-İstemci Simülasyonu:** Gerçek zamanlı ağ iletişimini modelleyen istemci ↔ sunucu yapısı ile tam simülasyon ortamı.  

- **Hibrit Mod Desteği:** RSA ve Kyber algoritmalarının ayrı ayrı ya da aynı anda kullanıldığı senaryo testleri.  

- **Performans Ölçümü:** Mikrosaniye (μs) düzeyinde zamanlama ile hızlı ve detaylı performans ölçüm modülü.  

- **Kuantum Saldırı Simülasyonu:** Shor algoritmasına dayalı teorik kuantum saldırı modellemesi ile klasik algoritmaların kırılganlığının test edilmesi.  

- **TLS Entegrasyonu:** CRYSTALS-Kyber destekli TLS 1.3 protokolünün simülasyon ortamına entegrasyonu (RFC 9180 uyumlu).


## Team / *Ekip*

- **2320191010** - *İbrahim Yiğit ÇETİN*  
- **2420191037** - *Eray TURAN*

---

## Roadmap / *Yol Haritası*

Tam yol haritası için: [`ROADMAP.md`](./ROADMAP.md)

- ✅ Adım 1: Kyber algoritmasının entegrasyonu
- ✅ Adım 2: RSA algoritmasının entegrasyonu
- ✅ Adım 3: Performans karşılaştırmaları
- ✅ Adım 4: Hibrit şifreleme senaryoları
- ✅ Adım 5: Socket-tabanlı güvenli kanal simülasyonu
- ✅ Adım 6: Kyber-TLS entegrasyonu (RFC 9180'ye uygun)
- ✅ Adım 7: Shor algoritması ile kuantum saldırı analizi

---

## Researchs / *Araştırmalar*

| Topic / *Başlık*        | Link                                    | Description / *Açıklama*                        |
|-------------------------|-----------------------------------------|------------------------------------------------|
| Kyber-RsaSimToolkit Perspective DeepSearch    | [researchs/kyber-rsa_10_trend.md](researchs/kyber-rsa_10_trend.md) | Araç hakkında deepsearch bilgisi.* |
| Example Perspective Research Pdf  | [researchs/kyber-rsa_10_trend.pdf](researchs/kyber-rsa_10_trend.pdf) | Araştırma sonucunda oluşturulan pdf dosyası* |
| Kyber-RSASimToolkit Trends DeepSearch    | [researchs/kyber-rsasimtoolkit_trends.md](researchs/kyber-rsasimtoolkit_trends.md) | Araç hakkında deepsearch bilgisi.* |
| Example Trends Research Pdf  | [researchs/kyber_rsasimtoolkit_trends.pdf](researchs/kyber_rsasimtoolkit_trends.pdf) | Araştırma sonucunda oluşturulan pdf dosyası* |

---

## References / *Referanslar*

| Topic / *Başlık*              | Link                                        | Description / *Açıklama*                                                         |
|------------------------------|---------------------------------------------|----------------------------------------------------------------------------------|
| Kyber Spesifikasyonu         | [references/kyber-specification.pdf](references/kyber-specification.pdf) | CRYSTALS-Kyber algoritmasının resmi spesifikasyonları ve NIST standartları.     |
| RFC 9180 - Hibrit Şifreleme  | [references/rfc9180.pdf](references/rfc9180.pdf)           | Hibrit Kamu Anahtar Şifreleme (HPKE) standartları ve Kyber entegrasyonu.        |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/ibrahimyigitcetin/Kyber-RSASimToolkit.git
   cd Kyber-RSASimToolkit
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/macOS
   ```

3. **Install Dependencies / *Bağımlılıkları Yükleyin***:  
   ```bash
   pip install -r requirements.txt
   ```

   **Not:** Eğer `requirements.txt` yoksa:  
   ```bash
   pip install psutil cryptography
   ```

---

## 🚀 Basic Usage / Temel Kullanım

Projeyi çalıştırmak için aşağıdaki adımları izleyin:

---

### 🧪 Kyber512 Simülasyonu

**Temel Çalıştırma:**
```bash
python src/kyber512_sim.py
```

#### 🔹 Test Betikleri

- **Zamanlama testi:**
  ```bash
  python src/kyber_timing_test.py
  ```

- **Bellek testi:**
  ```bash
  python src/kyber_memory_test.py
  ```

- **Çıktı boyutu testi:**
  ```bash
  python src/kyber_output_size_test.py
  ```

### 🔐 RSA Simülasyonu

#### 🔹 Test Betikleri

- **Zamanlama testi:**
  ```bash
  python src/rsa_timing_test.py
  ```

- **Bellek testi:**
  ```bash
  python src/rsa_memory_test.py
  ```

- **Çıktı boyutu testi:**
  ```bash
  python src/rsa_output_size_test.py
  ```

#### 🔹 Çıktılar

- Sonuçlar konsola yazdırılır.
- Ayrıca `kyber512_test_results.txt`, `kyber512_sim_test_results.md` veya `kyber_and_rsa_results.md` gibi dosyalara kaydedilir.

---


## 🔐 TLS Benzeri Anahtar Değişim Simülasyonu

**Sunucu (Kyber veya RSA Modunda):**
```bash
python kyber_rsa_server.py
```

**İstemci:**
```bash
python kyber_rsa_client.py
```

Bu yapı ile:

- İstemci ve sunucu arasında bağlantı kurulur,
- Seçilen algoritmaya göre (Kyber veya RSA) **anahtar değişimi** gerçekleştirilir,
- Rastgele sır şifrelenip gönderilir ve çözülür,
- Performans çıktıları terminal ekranına yazdırılır.

---

**📊 Örnek Çıktı:**
```
[🔌] Sunucu dinlemede (KYBER modu)...
[+] Bağlantı: ('127.0.0.1', 57805)
[🔐] Shared Secret (Server): f83a05481fe36db7dbbbc907fee3767868da1abcdc54b91cb41a07d364543...

=== Performans Zamanları (saniye) ===
Anahtar Üretimi:   0.000002
Şifreleme:         0.000001
Şifre Çözme:       0.000000
```

> 🔧 Not: `ALGO = "kyber"` veya `"rsa"` olarak değiştirerek kullanılacak algoritma seçilir.

---

---

## 🧪 Shor Algoritması Simülasyonu (Klasik)

**📂 Dosya: `src/shor_classical_sim.py`**

Bu dosya, **Shor algoritmasının klasik (non-kuantum) bir simülasyonunu** içerir. Amaç, küçük sayılar (örneğin `N = 15`) üzerinden RSA’nın kırılganlığını görsel olarak göstermektir.

---

**🚀 Çalıştırmak için:**

```bash
python src/shor_classical_sim.py
```

**🔍 Ne Yapar?**  
Bu Python dosyası şu işlemleri gerçekleştirir:

- RSA benzeri bir sayı N (örneğin 15) için rastgele bir a seçer (1 < a < N).
- a^r mod N = 1 olacak şekilde periyot r bulmaya çalışır.
- Eğer r çiftse ve a^(r/2) ± 1 değerleri N ile bölünebiliyorsa, bunlardan biri veya ikisi RSA'nın asal çarpanlarıdır.
- Amaç: Shor algoritmasının mantığını klasik ortamda taklit ederek RSA’nın teorik zayıflığını ortaya koymak.

**📊 Örnek Çıktı:**

```matlab
[*] N = 15 için Shor algoritması klasik simülasyon başlatıldı.
[*] a = 7 seçildi.
[*] Periyot r = 4 bulundu (7^r mod 15 = 1)
[*] Çarpanlar bulundu: gcd(7^2 - 1, 15) = 3,  gcd(7^2 + 1, 15) = 5
[+] Başarılı: 15 = 3 x 5
```

**📌 Notlar:**

- Bu simülasyon yalnızca çok küçük N değerleri için geçerlidir (örneğin N = 15, N = 21, N = 33).
- Gerçek Shor algoritması, kuantum bilgisayarlarda büyük N için etkilidir.
- Amaç: Shor’un RSA üzerindeki etkisini gözle görülür şekilde göstermek.
- Kyber gibi MLWE tabanlı algoritmalar bu tür saldırılardan etkilenmez.

---

## Contributing / *Katkıda Bulunma*

Topluluk katkılarını memnuniyetle karşılıyoruz! Katkıda bulunmak için:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:ibrahimyigitcetin/Kyber-RSASimToolkit.git`).  
3. Create a branch (`git checkout -b feature/your-feature`).  
4. Commit changes with clear messages.  
5. Push to your fork (`git push origin feature/your-feature`).  
6. Open a Pull Request.  

Follow our coding standards (see [CONTRIBUTING.md](CONTRIBUTING.md)).

---

## License / *Lisans*

Licensed under the [MIT License](LICENSE.md).  
*MIT Lisansı altında lisanslanmıştır.*

---

## Acknowledgements / *Teşekkürler*

Thanks to:  
- **CRYSTALS Ekibi** – Kyber algoritmasını geliştirdiği ve spesifikasyonları sağladığı için.  
- **Cryptography Kütüphanesi** – Python’da güvenli RSA implementasyonları sağladığı için.  
- **NIST PQC Girişimi** – Kuantum sonrası şifreleme standartlaştırmasını yönlendirdiği için.

---

