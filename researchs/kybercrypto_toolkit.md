# KyberCrypto Toolkit

**KyberCrypto Toolkit**, Python tabanlı, açık kaynaklı ve kullanıcı dostu bir post-kuantum kriptografi aracıdır. CRYSTALS-Kyber algoritmasını temel alarak kuantum-dirençli anahtar değişimi ve şifreleme süreçlerini otomatikleştirir. NIST’in PQC (Post-Quantum Cryptography) standartlaştırma sürecinde finalist olan Kyber algoritmasının üç güvenlik seviyesi olan **Kyber-512**, **Kyber-768** ve **Kyber-1024** desteklenmektedir. 

Araç; klasik şifreleme algoritmaları (RSA, ECC) ile karşılaştırmalı analizler sunar, gerçek zamanlı performans izlemesi, görsel raporlama, TLS/SSL entegrasyonu ve eğitimsel modüller gibi birçok yenilikçi özelliğe sahiptir.

---

## 🎯 Proje Hedefleri

- **Post-Kuantum Güvenlik Bilinci:** Kuantum bilgisayarların klasik şifrelemeye karşı oluşturduğu tehdide dikkat çekmek.
- **Performans Karşılaştırması:** Kyber ve klasik algoritmaların hız, bellek ve güvenlik açısından analizini yapmak.
- **Protokol Entegrasyonu:** TLS, VPN gibi protokollerde Kyber desteğini test ederek hibrit modeller geliştirmek.
- **Kullanıcı Dostu Deneyim:** Modüler yapı ve görselleştirme panelleriyle kolay kullanım.
- **Eğitim ve Araştırma Desteği:** Açık kaynak kod ve dokümantasyon ile akademik kullanımı teşvik etmek.

---

## 🚀 Temel Özellikler

### 🔐 Kyber Algoritma Implementasyonu

- Kyber-512, Kyber-768, Kyber-1024 destekli tam anahtar üretimi ve kapsülleme sistemleri.
- Lattice tabanlı kriptografi ile kuantum saldırılarına dayanıklılık.
- NIST PQC standartlarına tam uyumluluk.

### ⚖️ Performans Karşılaştırma ve Benchmarking

- RSA-2048, RSA-4096, ECC gibi klasik algoritmalarla karşılaştırmalı analiz.
- Anahtar üretim süresi, şifreleme/deşifreleme hızı ve bellek kullanımı ölçümü.
- Grafana benzeri görsellerle performans metrik sunumu.

### 📊 Gerçek Zamanlı Performans İzleme

- Gerçek zamanlı algoritma davranışı takibi.
- Hata oranları, başarısız kapsül açma girişimlerinin loglanması.
- Anomali tespiti ve uyarı sistemleri.

### 🔐 TLS/SSL Entegrasyonu

- Kyber tabanlı TLS/SSL oturumları oluşturma ve test etme.
- Hibrit şifreleme modelleri (Kyber+RSA) desteği.
- Gerçek dünya bağlantı senaryolarında performans ölçümü.

### 🛡️ MAC Adresi Tabanlı Kimlik Doğrulama

- Cihazların MAC adresleri ile ek kimlik doğrulama katmanı.
- İlk 6 hane (OUI) analiziyle üretici ve hizmet sınıfı tespiti.
- Yerel ağlarda güvenli anahtar paylaşımı için kullanışlılık.

### ⚗️ Kuantum-Dirençli Hibrit Şifreleme

- Kyber ve klasik algoritmaların kombinasyonu ile hibrit sistemler.
- Örneğin: RSA ile anahtar değişimi, Kyber ile veri şifreleme.

### 📈 Görselleştirme ve Raporlama

- Hız, bellek, hata oranı gibi metriklerin panellerle sunulması.
- PDF ve CSV formatlarında ayrıntılı rapor üretimi.
- Güvenlik derecelendirmesi (Low, Medium, High, Critical).

### 🧪 Kuantum Saldırı Simülasyonları

- Shor, Grover gibi kuantum algoritmalarına karşı simülasyonlar.
- LWE (Learning With Errors) tabanlı saldırı analizleri.

### 🧩 Modüler ve Açık Kaynak Yapı

- Python tabanlı modüler mimari.
- Kolay özelleştirme, entegrasyon ve katkı için MIT lisansı.
- Geliştiricilere yönelik kapsamlı API ve dökümantasyon.

### 🎓 Eğitimsel Materyaller

- Kyber algoritmasının temelini açıklayan interaktif rehberler.
- Lattice kriptografisi, modüler aritmetik ve kuantum tehditlerine dair içerikler.
- Üniversiteler ve meraklılar için rehber belgeler.

---

## 🧠 Teknik Detaylar

- **Gereksinimler:**
  - Python 3.8+
  - `numpy` (matematik ve matris işlemleri)
  - `pycryptodome` (kriptografik işlemler)
  - `matplotlib` (grafik çizimleri)

- **Performans Optimizasyonu:**
  - Vektörleştirme ve paralel işlem desteğiyle matris tabanlı hızlandırma.

- **Güvenlik Notu:**
  - Eğitim ve araştırma amaçlıdır. Sabit zamanlı işlemler eksik olabilir; üretim ortamında dikkatli kullanım önerilir.

---

## 💡 Kullanım Senaryoları

- 🔐 **Güvenlik Araştırmaları:** Post-kuantum algoritmalar üzerine pratik testler.
- 🎓 **Akademik Çalışmalar:** Üniversite dersleri ve seminerlerde kullanım.
- 🧪 **Protokol Geliştirme:** TLS, VPN gibi sistemlerde Kyber prototipleme.
- 🏢 **Kurumsal Planlama:** Kuantum sonrası geçiş senaryolarının test edilmesi.

---

## 📝 Lisans

Bu proje **MIT Lisansı** altında açık kaynak olarak sunulmaktadır. Herkesin katkısına açıktır.

---

## 📚 Katkıda Bulunun

Pull request'ler, sorun bildirimleri ve öneriler memnuniyetle karşılanır. Daha fazla bilgi için `CONTRIBUTING.md` dosyasını inceleyin.

---

## 🌐 Bağlantılar

- [Kyber Resmi Dokümantasyon](https://pq-crystals.org/kyber/)
- [NIST PQC Standartlaştırma Süreci](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [GitHub Repository (örnek)](https://github.com/kullanici/kybercrypto-toolkit)

