# Kyber512 ve RSA-2048 Performans ve Bellek Karşılaştırması

## 1. Performans Zamanları (saniye)

| Algoritma | Anahtar Üretim | Şifreleme | Şifre Çözme |
|-----------|----------------|-----------|-------------|
| Kyber512  | 0.000002       | 0.000001  | 0.000000    |
| RSA-2048  | 0.069922       | 0.000046  | 0.000733    |

---

## 2. Bellek Kullanımı (KB)

| Algoritma | Başlangıç | Anahtar Üretimi Sonrası | Şifreleme Sonrası | Şifre Çözme Sonrası |
|-----------|-----------|-------------------------|-------------------|--------------------|
| Kyber512  | 21772     | 21772                   | 21772             | 21772              |
| RSA-2048  | 24452     | 25556                   | 25956             | 25972              |

---

## 3. Çıktı Boyutları (byte)

| Algoritma | Public Key | Secret/Private Key | Ciphertext | Diğer               |
|-----------|------------|--------------------|------------|---------------------|
| Kyber512  | 800        | 1632               | 768        | Shared Secret: 32    |
| RSA-2048  | 294        | 1218               | 256        | Plaintext: 20        |

---

## 4. Yorumlar ve Değerlendirme

- **Kyber512**, klasik RSA-2048’e göre anahtar üretme işlemlerinde kat kat hızlıdır. Bu, kuantum dirençli algoritmaların avantajlarından biridir.
- Bellek kullanımı açısından Kyber daha az artış gösterirken, RSA işlem adımlarında belirgin bir artış yapmaktadır.
- Kyber512’nin çıktı boyutları RSA’ya göre daha büyüktür; fakat bu, kuantum dayanıklılığı ve hız avantajlarıyla dengelenir.
- RSA, kuantum saldırılarına karşı savunmasızdır ve Shor algoritmasıyla kırılabilirken, Kyber LWE temelli yapısı ile kuantuma dayanıklı olarak öne çıkar.

---

> **Not:** Bu testler saf Python simülasyonlarıdır. Gerçek uygulamalarda C/C++ ve optimize kütüphaneler kullanılmalıdır.

---

