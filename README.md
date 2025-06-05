<div align="center">
  <img src="https://img.shields.io/github/languages/count/YOUR_USERNAME/QUANTUMTESTERPROJECT?style=flat-square&color=blueviolet" alt="Language Count">
  <img src="https://img.shields.io/github/languages/top/YOUR_USERNAME/QUANTUMTESTERPROJECT?style=flat-square&color=1e90ff" alt="Top Language">
  <img src="https://img.shields.io/github/last-commit/YOUR_USERNAME/QUANTUMTESTERPROJECT?style=flat-square&color=ff69b4" alt="Last Commit">
  <img src="https://img.shields.io/github/license/YOUR_USERNAME/QUANTUMTESTERPROJECT?style=flat-square&color=yellow" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-green?style=flat-square" alt="Status">
  <img src="https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square" alt="Contributions">
</div>

# Kyber-RSASimToolkit

*Kyber-RSASimToolkit*, kuantum dirençli şifreleme algoritmalarını (örneğin CRYSTALS-Kyber (Kyber512)) geleneksel algoritmalar (RSA-2048 gibi) ile karşılaştıran bir araştırma ve test projesidir.  
Python tabanlı simülasyonlar ve performans testleri aracılığıyla hız, bellek kullanımı ve çıktı boyutları gibi temel metrikleri analiz ederek kuantum sonrası şifrelemenin pratik etkilerini anlamayı amaçlar.

---

## Features / *Özellikler*

- **Kyber512 Simülasyonu:** Kyber512'nin yapısal ve performans testleri için simülasyonu.  
- **Karşılaştırmalı Analiz:** Kyber512 ve RSA-2048'in hız, bellek ve çıktı boyutları açısından karşılaştırmalı analizi.  
- **NIST Dokümantasyonu:** NIST Kuantum Sonrası Şifreleme standartları ve algoritma seçim sürecinin detaylı dokümantasyonu.

---

## Team / *Ekip*

- **2320191010** - *İbrahim Yiğit ÇETİN*  
- **2420191037** - *Eray TURAN*

---

## Roadmap / *Yol Haritası*

See our plans in [ROADMAP.md](ROADMAP.md).  
*Yolculuğu görmek için [ROADMAP.md](ROADMAP.md) dosyasına göz atın.*

---

## Research / *Araştırmalar*

| Topic / *Başlık*              | Link                                        | Description / *Açıklama*                                                         |
|------------------------------|---------------------------------------------|----------------------------------------------------------------------------------|
| Kyber Spesifikasyonu         | [references/kyber-specification.pdf](references/kyber-specification.pdf) | CRYSTALS-Kyber algoritmasının resmi spesifikasyonları ve NIST standartları.     |
| RFC 9180 - Hibrit Şifreleme  | [references/rfc9180.pdf](references/rfc9180.pdf)           | Hibrit Kamu Anahtar Şifreleme (HPKE) standartları ve Kyber entegrasyonu.        |

---

## Installation / *Kurulum*

1. **Clone the Repository / *Depoyu Klonlayın***:  
   ```bash
   git clone https://github.com/YOUR_USERNAME/QUANTUMTESTERPROJECT.git
   cd QUANTUMTESTERPROJECT
   ```

2. **Set Up Virtual Environment / *Sanal Ortam Kurulumu*** (Recommended):  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
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

## Usage / *Kullanım*

Projeyi çalıştırın:  
```bash
python sim_and_test_files/kyber512_sim.py
```

**Steps / *Adımlar***:  
1. **Giriş Verilerini Hazırlayın**: Harici giriş verisine gerek yoktur; veriler dahili olarak üretilir (`os.urandom`).  
2. **Betiği Argümanlarla Çalıştırın**:  
   - Zamanlama testi: `python sim_and_test_files/kyber_timing_test.py`  
   - Bellek testi: `python sim_and_test_files/kyber_memory_test.py`  
   - Çıktı boyutu testi: `python sim_and_test_files/kyber_output_size_test.py`

3. **Çıktıyı Kontrol Edin**:  
   - Sonuçlar konsola yazdırılır.  
   - Ayrıca `kyber512_test_results.txt` gibi dosyalara ya da `kyber_and_rsa_results.md` gibi Markdown dosyalarına kaydedilir.

---

## Contributing / *Katkıda Bulunma*

Topluluk katkılarını memnuniyetle karşılıyoruz! Katkıda bulunmak için:  
1. Fork the repository.  
2. Clone your fork (`git clone git@github.com:YOUR_USERNAME/QUANTUMTESTERPROJECT.git`).  
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

