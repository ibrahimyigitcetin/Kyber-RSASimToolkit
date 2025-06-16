# 🔐 Shor Algoritması ile Kuantum Saldırı Simülasyonu ve Teorik Analiz

## 🧠 Genel Bakış
Bu adımda, **Shor algoritmasının** CRYSTALS-Kyber ve RSA algoritmaları üzerindeki etkisini teorik olarak analiz ettik ve klasik bir simülasyonla **RSA’nın kuantum saldırılarına karşı kırılganlığını** gösterdik.  
Amaç, **Kyber’ın kuantum dirençli yapısını doğrulamak** ve RSA’nın zayıflığını vurgulamaktır.  
Analiz, Shor algoritmasının matematiksel temellerine ve **Kyber’ın MLWE (Modül Öğrenme-Hata) güvenliğine** odaklanırken, `shor_classical_sim.py` dosyasındaki simülasyon RSA’nın kırılganlığını pratik olarak göstermektedir.

---

## ⚛️ Shor Algoritması

- **Tanım:**  
  Shor algoritması, kuantum bilgisayarlar için geliştirilmiş bir algoritmadır ve **büyük sayıları polinomal sürede çarpanlarına ayırır**.  
  Periyot bulma problemini **kuantum Fourier dönüşümü** ile çözer.

- **RSA Üzerindeki Etkisi:**  
  RSA, büyük sayıların çarpanlara ayrılmasının zorluğuna dayanır.  
  Örneğin, **2048-bit bir RSA anahtarı (N = p × q)**, Shor algoritması ile kuantum bilgisayarda kırılabilir.  
  Bunun için yaklaşık **4096 kuantum biti** gerekir; ancak günümüz teknolojisi bu ölçeğe ulaşamamıştır.

- **Sınırlamalar:**  
  Shor algoritması **klasik bilgisayarlarda pratik değildir** ve yalnızca kuantum bilgisayarlarla etkilidir.

---

## 🛡️ Kyber’ın Kuantum Direnci

- **MLWE Tabanlı Güvenlik:**  
  CRYSTALS-Kyber, **modül öğrenme-hata problemi (MLWE)** üzerine inşa edilmiştir.  
  MLWE, kuantum bilgisayarlar için bilinen etkili bir çözüm sunmaz, bu da Kyber’ı **Shor algoritmasına karşı dirençli** kılar.

- **NIST Standartları:**  
  Kyber, NIST’in kuantum sonrası şifreleme yarışmasında **ML-KEM (FIPS 203)** olarak standartlaştırılmıştır.  
  Literatür, Kyber’ın kuantum saldırılarına karşı güvenliğini doğrular ([pq-crystals.org](https://pq-crystals.org)).

- **Sonuç:**  
  Shor algoritması, Kyber’ın temelini oluşturan **kafes tabanlı problemleri hedef alamaz**, bu nedenle Kyber **kuantum sonrası şifreleme için güvenlidir**.

---

## 🧪 Simülasyon Sonuçları

- **Uygulama:**  
  `shor_classical_sim.py` dosyasında klasik bir Shor algoritması simülasyonu gerçekleştirildi.  
  Kod, **N = 15** için periyot bulma işlemini simüle ederek **3 ve 5 çarpanlarını** buldu.

- **Bulgular:**  
  Simülasyon, **RSA’nın çarpanlara ayırma saldırılarına karşı kırılganlığını** gösteriyor.  
  N = 15 için algoritma, çarpanları (3, 5) doğru bir şekilde belirledi ve RSA’nın teorik zayıflığını doğruladı.

- **Sınırlamalar:**  
  Klasik simülasyon, gerçek bir kuantum uygulaması değildir;  
  ancak RSA’nın zayıflığını göstermek için **yeterlidir**.  
  Kyber, MLWE tabanlı olduğu için bu tür saldırılardan **etkilenmez**.

---

## ⚖️ Karşılaştırmalı Analiz

| Özellik     | Kyber                                | RSA                                   |
|-------------|---------------------------------------|----------------------------------------|
| Temel Güvenlik | MLWE (modül öğrenme-hata) problemi   | Çarpanlara ayırma problemi              |
| Kuantum Saldırı Direnci | ✅ Shor algoritmasına dirençli | ❌ Shor algoritmasıyla kırılabilir     |
| Standartlaşma | NIST FIPS 203 (ML-KEM)               | Geleneksel (kuantum sonrası güvensiz)  |
| Uygulama     | TLS, VPN, post-kuantum sistemler     | Eski TLS, e-posta şifreleme vb.        |

---

## ✅ Sonuç
Kyber, kuantum direnci sayesinde RSA’ya **açık bir üstünlük sağlar**.  
Shor algoritması RSA’yı tehdit ederken, Kyber gibi MLWE tabanlı algoritmalar kuantum sonrası güvenlikte **geleceğin standardı olmaya adaydır**.
