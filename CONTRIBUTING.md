# 🤝 Katkı Yapma Rehberi

Kyber-RSASimToolkit projesine katkıda bulunmak istiyorsanız, aşağıdaki rehber size yol gösterecektir.

## 🚀 Katkı Yapma Yolları

Projeye şu yollarla katkıda bulunabilirsiniz:

- **🧠 Kod Katkıları**: Simülasyon aracını geliştirmek için yeni özellikler ekleyebilir, hataları düzeltebilir veya performansı optimize edebilirsiniz.  
- **📚 Dokümantasyon**: Mevcut dokümantasyonu iyileştirebilir veya kullanıcıların aracı anlamasına ve kullanmasına yardımcı olacak yeni kılavuzlar ekleyebilirsiniz.  
- **🐞 Hata Raporları**: Araç kullanırken karşılaştığınız sorunları veya hataları bildirebilirsiniz.  
- **💡 Özellik Önerileri**: Aracı daha kullanışlı hale getirebilecek yeni özellikler veya geliştirmeler önerebilirsiniz.

---

## ⚙️ Ortam Kurulumu

Projeye katkıda bulunmak için geliştirme ortamını yerel makinenizde kurmanız gerekir. Aşağıdaki adımları izleyin:

### 1. Depoyu Klonlayın

```bash
git clone https://github.com/ibrahimyigitcetin/Kyber-RSASimToolkit.git
cd Kyber-RSASimToolkit
```

### 2. Bağımlılıkları Yükleyin

Proje, Python 3.10 veya daha yüksek bir sürüm gerektirir. Gerekli paketleri şu komutla yükleyin:

```bash
pip install -r requirements.txt
```

### 3. Aracı Çalıştırın

Simülasyon aracını şu komutla çalıştırabilirsiniz:

```bash
python kyber512_sim.py
```

---

## 🧑‍💻 Kodlama Standartları

Konsistens ve okunabilirlik sağlamak için lütfen aşağıdaki kodlama standartlarına uyun:

- Python kodları için **PEP 8** kurallarına uyun.
- Anlamlı değişken ve fonksiyon isimleri kullanın.
- Tüm fonksiyonlar ve sınıflar için **docstring** yazın.
- Gerektiğinde kodunuza açıklayıcı **yorumlar** ekleyin.

---

## 🔁 Pull Request Süreci

Değişikliklerinizi göndermeye hazır olduğunuzda şu adımları izleyin:

### 1. Yeni Bir Dal Oluşturun

```bash
git checkout -b feature/özellik-adınız
```

### 2. Değişikliklerinizi Kaydedin

```bash
git add .
git commit -m "Açıklayıcı mesajınızı buraya yazın"
```

### 3. GitHub’a Gönderin

```bash
git push origin feature/özellik-adınız
```

### 4. Pull Request Açın

GitHub deposuna gidin ve dalınızdan `main` dalına bir **pull request** açın.  
Değişikliklerinizi ve neden gerekli olduğunu açıkça tarif edin.

### 5. İnceleme Süreci

Pull request’iniz proje yöneticileri tarafından incelenecek.  
Geri bildirimlere göre düzenlemeler yapmaya hazır olun.

---

## 📄 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır.  
Projeye katkıda bulunarak, katkılarınızın aynı lisans altında lisanslanacağını kabul etmiş olursunuz.  
Lisans detayları için `LICENSE.md` dosyasını inceleyin.

---

## 📌 Ek Notlar

- **📚 Referanslar**: Proje, Kyber spesifikasyonu ve [RFC 9180](https://www.rfc-editor.org/rfc/rfc9180) gibi önemli referanslara dayanır. Daha fazla bilgi için `kyber-specification.pdf` ve `rfc9180.pdf` dosyalarına bakabilirsiniz.
- **🗺️ Yol Haritası**: Projenin gelecekteki geliştirme planları için `ROADMAP.md` dosyasını inceleyin.
- **📈 Potansiyel Geliştirme Alanları**: Daha detaylı kullanım kılavuzları, eğitim videoları veya farklı ağ protokolleriyle entegrasyon senaryoları gibi geliştirmeler projeyi daha geniş bir kitleye hitap edecek hale getirebilir.

---

## 📥 GitHub’a Ekleme Talimatları

Bu dosyayı GitHub’a eklemek için:

```bash
# Projenizin kök dizininde CONTRIBUTING.md adında bir dosya oluşturun
# Yukarıdaki içeriği dosyaya yapıştırın

git add CONTRIBUTING.md
git commit -m "Add CONTRIBUTING.md for contribution guidelines"
git push origin main
```

---

## 🙏 Teşekkürler

Kyber-RSASimToolkit projesine katkıda bulunmayı düşündüğünüz için teşekkür ederiz!  
Yardımlarınız çok değerli. Sorularınız veya ek özelleştirme talepleriniz olursa, lütfen bizimle iletişime geçin.
