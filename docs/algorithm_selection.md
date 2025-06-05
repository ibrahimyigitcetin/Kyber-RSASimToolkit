# Neden ML-KEM (Kyber512)?

- **TLS için hızlı**: ~0.6 ms şifreleme süresi, düşük gecikme.
- **Güvenli**: NIST Seviye 1, kuantum saldırılara karşı AES-128 eşdeğeri güvenlik.
- **OpenSSL ile uyumlu**: liboqs entegrasyonu sayesinde TLS 1.3 ile çalışır.
- **Windows’ta çalışır**: Python (pqcrypto) ile kolayca test edilebilir.


## Alternatifler
- **ML-DSA (Dilithium)**: Dijital imza için tasarlandı, TLS anahtar paylaşımı için uygun değil.
- **SPHINCS+**: Yavaş (~10 ms), büyük anahtar boyutları (~32 KB), donanım kısıtlamaları için uygun değil.

## Karşılaştırma Tablosu
| Özellik         | Kyber512       | Dilithium      | SPHINCS+       |
|-----------------|----------------|----------------|----------------|
| Amaç            | Anahtar paylaşımı | İmza         | İmza           |
| Hız             | Hızlı (~0.6 ms) | Hızlı (~1 ms) | Yavaş (~10 ms) |
| Anahtar Boyutu  | Küçük (~800 B) | Orta (~2 KB)  | Büyük (~32 KB) |
| TLS Uyumu       | Evet           | Hayır          | Hayır          |
