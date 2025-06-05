# NIST Post-Kuantum Kriptografi

## Standartlaştırılan Algoritmalar
| Algoritma            | Amaç                | Tür                | Durum              |
|----------------------|---------------------|--------------------|--------------------|
| CRYSTALS-KYBER       | Anahtar Paylaşımı   | Lattice Tabanlı    | Standart (FIPS 204)|
| CRYSTALS-Dilithium   | Dijital İmza        | Lattice Tabanlı    | Standart (FIPS 203)|
| SPHINCS+             | Dijital İmza        | Hash Tabanlı       | Standart (FIPS 205)|
| HQC                  | Anahtar Paylaşımı   | Kod Tabanlı        | Yedek (2025)       |


## Proje İçin Seçilen Algoritma
- **CRYSTALS-KYBER (ML-KEM)**
- **Neden?**
  - TLS entegrasyonu için anahtar paylaşımı yapar.
  - Hızlı ve düşük gecikme süresi sunar.
  - NIST tarafından standartlaştırılmış (FIPS 204).
  - Windows’ta Python ile test edilebilir.
