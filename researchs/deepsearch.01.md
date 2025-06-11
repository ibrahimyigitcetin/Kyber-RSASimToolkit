Proje ve Hedefler ve Özellikler

KyberCrypto Toolkit
Bu Python tabanlı post-kuantum kriptografi aracı, CRYSTALS-Kyber algoritmasını temel alarak kuantum-dirençli anahtar değişimi ve şifreleme süreçlerini otomatikleştiren, kapsamlı, modüler ve kullanıcı dostu bir çözümdür. NIST’in post-kuantum kriptografi standartlaştırma sürecinde finalist olan Kyber algoritmasının (Kyber-512, Kyber-768, Kyber-1024) referans implementasyonlarını sunar ve klasik şifreleme algoritmaları (RSA, ECC) ile karşılaştırmalı analizler sağlar. Anahtar üretimi, kapsülleme, kapsül açma, hata oranı analizi ve kuantum saldırılarına karşı direnç testi gibi temel özelliklere ek olarak, Grafana tarzı görselleştirme panelleri ile performans metriklerini (anahtar üretimi süresi, bellek kullanımı, şifreleme hızı) net ve görsel bir şekilde sunar. TLS/SSL protokollerine entegrasyon, hibrit şifreleme senaryoları ve MAC adresi tabanlı kimlik doğrulama gibi yenilikçi özellikler içerir. Gerçek zamanlı performans izleme ve detaylı loglama ile algoritma davranışlarını analiz eder, böylece kullanıcıların hem eğitimsel hem de profesyonel senaryolarda Kyber’ı anlaması ve optimize etmesi kolaylaşır. Esnek, güvenli ve açık kaynaklı yapısıyla, bu araç post-kuantum kriptografi analizlerini basitleştirir ve kuantum bilgisayar tehditlerine karşı proaktif çözümler sunar.

Hedefler





Post-Kuantum Güvenlik Bilinci: Kuantum bilgisayarların klasik şifreleme algoritmalarını (RSA, ECC) tehdit ettiği bir gelecekte, Kyber gibi lattice tabanlı algoritmaların önemini vurgulamak ve kullanıcıları eğitmek.



Performans Karşılaştırması: Kyber’ın farklı güvenlik seviyelerini (Kyber-512, Kyber-768, Kyber-1024) ve klasik algoritmaları (RSA-2048, RSA-4096) hız, bellek kullanımı ve güvenlik açısından karşılaştırmak.



Protokol Entegrasyonu: TLS, VPN ve diğer güvenlik protokollerine Kyber’ın entegrasyonunu test ederek hibrit şifreleme modelleri (Kyber+RSA) geliştirmek.



Kullanıcı Dostu Deneyim: Grafik tabanlı görselleştirme ve modüler yapı ile geliştiriciler ve kriptografi meraklıları için erişilebilir bir platform sağlamak.



Araştırma ve Eğitim Desteği: Açık kaynak kod ve ayrıntılı dokümantasyon ile akademik çalışmaları ve eğitimsel projeleri desteklemek.

Özellikler





Kyber Algoritma Implementasyonu:





Kyber-512, Kyber-768 ve Kyber-1024 güvenlik seviyelerinde anahtar üretimi, kapsülleme ve kapsül açma işlemleri.



Lattice tabanlı kriptografi ile kuantum bilgisayarlara karşı direnç.



NIST post-kuantum kriptografi standartlarına tam uyumluluk.



Karşılaştırmalı Performans Analizi:





Kyber ile RSA ve ECC algoritmalarını karşılaştıran benchmarking araçları.



Anahtar üretimi, şifreleme/deşifreleme hızı ve bellek kullanımı metriklerinin ölçümü.



Grafana tarzı görselleştirme ile sonuçların kullanıcı dostu sunumu.



Gerçek Zamanlı Performans İzleme:





Algoritma işlemlerini gerçek zamanlı takip eden bir monitör sistemi.



Hata oranları ve başarısız kapsül açma denemelerini detaylı loglama.



Anormallik tespiti için otomatik uyarı mekanizmaları.



TLS/SSL Protokol Entegrasyonu:





Kyber’ı TLS/SSL protokollerine entegre ederek modern web güvenliği senaryolarını test etme.



Hibrit şifreleme modelleri (Kyber+RSA) için deneysel destek.



HTTPS bağlantıları gibi gerçek dünya senaryolarında performans analizi.



MAC Adresi Tabanlı Kimlik Doğrulama:





Cihazların MAC adreslerini kullanarak ek bir kimlik doğrulama katmanı.



İlk 6 hane (OUI) analizi ile hizmet türü ve üretici tespiti.



Yerel ağlarda güvenli anahtar paylaşımı için entegrasyon.



Kuantum-Dirençli Hibrit Şifreleme:





Kyber’ı klasik algoritmalarla birleştirerek kuantum öncesi ve sonrası geçiş döneminde güvenli sistemler oluşturma.



Örneğin, RSA ile anahtar değişimi sonrası Kyber ile veri şifreleme.



Görselleştirme ve Raporlama:





Grafana tarzı panellerle performans metriklerinin görselleştirilmesi (hız, bellek, hata oranları).



PDF ve CSV formatında ayrıntılı raporlar.



Güvenlik seviyelerine göre (low, medium, high, critical) derecelendirme.



Kuantum Saldırı Simülasyonu:





Kyber’ın kuantum saldırılara (örneğin, Grover, Shor algoritmaları) karşı direncini test eden simülasyonlar.



LWE (Learning With Errors) tabanlı saldırılara karşı dayanıklılık analizi.



Modüler ve Açık Kaynak Yapı:





Python tabanlı modüler kod yapısı ile kolay özelleştirme ve entegrasyon.



MIT lisansı altında açık kaynak paylaşım, topluluk katkısına açık.



Geliştiriciler için kapsamlı API ve dokümantasyon.



Eğitimsel Araçlar:





Kyber algoritmasının çalışma prensiplerini açıklayan interaktif rehberler.



Lattice kriptografisi, modüler aritmetik ve kuantum tehditleri üzerine eğitim materyalleri.



Üniversiteler ve kriptografi meraklıları için rehber dokümantasyon.

Teknik Detaylar





Bağımlılıklar: Python 3.8+, numpy (matris işlemleri), pycryptodome (kriptografik primitifler), matplotlib (görselleştirme).



Performans Optimizasyonu: Kyber’ın matris tabanlı hesaplamaları için vektörleştirilmiş işlemler ve paralel hesaplama desteği.



Güvenlik Uyarısı: Eğitim ve araştırma amaçlı implementasyon; üretim ortamları için uygun değil. Sabit zamanlı işlemler eksik olabilir, yan kanal saldırılarına karşı ek önlemler gereklidir.

Kullanım Senaryoları





Güvenlik Araştırması: Kuantum-dirençli şifreleme algoritmalarını test eden güvenlik uzmanları için pratik bir araç.



Akademik Çalışmalar: Post-kuantum kriptografi dersleri ve araştırmaları için ideal.



Protokol Geliştirme: TLS, VPN ve diğer protokollerde Kyber entegrasyonunu prototiplemek isteyen geliştiriciler için.



Kurumsal Güvenlik Planlaması: Kuantum sonrası dünyaya geçiş için mevcut sistemlerin analiz ve adaptasyonu.
