# Shor Algoritması ile Kuantum Saldırı Simülasyonu ve Teorik Analiz

## Genel Bakış
Bu adımda, Shor algoritmasının CRYSTALS-Kyber ve RSA algoritmaları üzerindeki etkisini teorik olarak analiz ettik ve RSA’nın kuantum saldırılarına karşı kırılganlığını göstermek için bir simülasyon gerçekleştirdik. Amaç, Kyber’ın kuantum dirençli yapısını doğrulamak ve RSA’nın zayıflığını vurgulamaktır.

## Shor Algoritması
- **Tanım**: Shor algoritması, kuantum bilgisayarlar için geliştirilmiş bir algoritmadır ve büyük sayıların çarpanlarına ayrılmasını polinomal sürede gerçekleştirir. Periyot bulma problemini kuantum Fourier dönüşümüyle çözer.
- **RSA Üzerindeki Etkisi**: RSA, büyük sayıların çarpanlara ayrılmasının zorluğuna dayanır. Örneğin, 2048-bit bir RSA anahtarı (N = p × q), Shor algoritmasıyla kuantum bilgisayarda kırılabilir. Bunun için yaklaşık 4096 kuantum biti gerekir, ancak günümüz teknolojisi bu ölçeğe ulaşmamıştır.
- **Sınırlamalar**: Shor algoritması, klasik bilgisayarlarda pratik değildir ve yalnızca kuantum bilgisayarlarla etkilidir.

## Kyber’ın Kuantum Direnci
- **MLWE Tabanlı Güvenlik**: CRYSTALS-Kyber, modül öğrenme-hata problemi (MLWE) üzerine inşa edilmiştir. MLWE, kuantum bilgisayarlar için bilinen etkili bir çözüm sunmaz, bu da Kyber’ı Shor algoritmasına karşı dirençli kılar.
- **NIST Standartları**: Kyber, NIST’in post-kuantum şifreleme yarışmasında ML-KEM (Module-Lattice-based Key Encapsulation Mechanism) olarak standartlaştırılmıştır (FIPS 203). Literatür, Kyber’ın kuantum saldırılarına karşı güvenliğini doğrular [pq-crystals.org].
- **Sonuç**: Shor algoritması, Kyber’ın temelini oluşturan kafes tabanlı problemleri hedef alamaz, bu nedenle Kyber kuantum sonrası şifreleme için güvenlidir.
