# DEPO PRO - Depo ve Stok Yönetim Sistemi

DEPO PRO, küçük ve orta ölçekli işletmelerin (KOBİ) veya bireysel kullanıcıların stoklarını, depo giriş/çıkış işlemlerini ve envanter durumlarını takip edebilmeleri için geliştirilmiş modern, hızlı ve kullanıcı dostu bir masaüstü uygulamasıdır.

Uygulama, **Python** programlama dili ile yazılmış olup, grafiksel kullanıcı arayüzü (GUI) için **PyQt5**, veri depolama işlemleri için ise **SQLite** kullanmaktadır.

---

##  Özellikler

1. **Dashboard (Gösterge Paneli)**
   - Toplam ürün çeşidi, toplam stok değeri ve kritik stok durumundaki ürünlerin sayısını özet halinde sunar.
   - Son yapılan stok hareketlerini listeler.
   - Son 7 güne ait stok giriş/çıkış verilerini interaktif bir bar grafiği üzerinde gösterir.

2. **Envanter Yönetimi**
   - Kayıtlı ürünleri tablo halinde, sayfalı (pagination) bir yapıda listeler.
   - Ürün adı veya SKU koduna göre arama ve kategoriye göre filtreleme imkanı sunar.
   - Yeni ürün ekleme, var olan ürün bilgilerini güncelleme ve ürün silme işlemleri yapılabilir.
   - **SKU (Stok Tutma Birimi)** otomatik olarak kategori bazlı (Örn: ELK-12345) üretilebilir veya manuel girilebilir.

3. **Stok Giriş / Çıkış İşlemleri (Hareketler)**
   - Mevcut ürünlere hızlıca "Stok Giriş", "Stok Çıkış" veya "İade" işlemleri uygulanabilir.
   - Tüm stok hareketlerinin (hangi ürün, hangi tarihte, ne kadar girdi/çıktı) detaylı geçmişi tutulur ve tablo olarak incelenebilir.

4. **Ayarlar ve Temalar**
   - **Açık (Light) ve Koyu (Dark)** tema seçenekleri mevcuttur.
   - Uygulamada kullanılan para birimi (₺, $, €, £) değiştirilebilir.
   - "Kritik Stok Eşiği" kullanıcı tarafından belirlenebilir (Varsayılan: 10).
   - Veritabanı dosyasının yolu görüntülenebilir ve veritabanı yedeği alınabilir.

---

## 📂 Proje Yapısı

Proje temel olarak 3 ana Python dosyası ve 1 SQLite veritabanından oluşmaktadır:

- `main.py`
  Projenin giriş noktasıdır (entry-point). Uygulamayı başlatır, HiDPI desteğini ayarlar, temayı yükler ve ana pencereyi (MainWindow) ekranda gösterir. `pythonw main.py` veya `python main.py` komutuyla çalıştırılır.

- `gui.py`
  Tüm grafiksel kullanıcı arayüzü (GUI) kodlarını barındırır. Sayfaların tasarımı, stilleri, tabloların yapısı, buton tıklama olayları ve diyalog pencereleri bu dosya içerisinde yer alır. Özel olarak oluşturulmuş interaktif grafik çizimi (BarChart) ve modern CSS tabanlı stiller bu dosyadan beslenir.

- `database.py`
  Veritabanı bağlantısı, tablo oluşturma ve tüm CRUD (Oluştur, Oku, Güncelle, Sil) işlemlerini yöneten fonkisyonları içerir. Uygulama ilk kez çalıştırıldığında veritabanında (`depo.db`) gerekli tabloları oluşturur ve örnek veriler (seed data) ile sistemi doldurur.

- `depo.db`
  Uygulamanın çalışması sırasında otomatik oluşturulan SQLite veritabanı dosyasıdır. Tüm ayarlar, ürünler ve stok işlemleri burada şifresiz ve yerel olarak saklanır.

---

## 🛠 Kurulum ve Çalıştırma

1. **Gereksinimler**
   - Sisteminizde **Python 3.7** veya daha güncel bir sürümün kurulu olduğundan emin olun.
   - Kullanıcı arayüzü kütüphanesi olarak `PyQt5` gereklidir. Kurmak için terminalde:
     ```bash
     pip install PyQt5
     ```

2. **Çalıştırma**
   - Komut satırını (veya terminali) proje dizininde açın.
   - Uygulamayı çalıştırmak için:
     ```bash
     python main.py
     ```
   - *Not:* Windows sistemlerde arkada siyah konsol penceresinin açılmasını istemiyorsanız dosyayı `pythonw main.py` olarak veya uzantısını `.pyw` yaparak çalıştırabilirsiniz (`main.py` içerisinde bu durumu engelleyen platform bazlı bir kod bloğu da mevcuttur).

---

##  Veritabanı Tabloları

1. **`products` Tablosu**
   - `id`: Ürünün benzersiz kimliği.
   - `sku`: Stok tutma kodu (Örn: ELK-45214).
   - `name`: Ürün adı.
   - `category`: Ürün kategorisi.
   - `shelf`: Ürünün bulunduğu raf (Örn: Raf A1).
   - `quantity`: Mevcut stok miktarı.
   - `price`: Ürün fiyatı.
   - `min_stock`: Kritik stok uyarısı için eşik değer.
   - `image_path`: Ürüne ait görselin dosya yolu.

2. **`transactions` Tablosu**
   - `id`: İşlemin benzersiz kimliği.
   - `product_id`: İşlem gören ürünün kimliği.
   - `type`: İşlem türü ("Stok Giriş", "Stok Çıkış", "İade").
   - `quantity`: İşlem gören ürün miktarı.
   - `note`: İşleme dair eklenen notlar.
   - `date`: İşlem tarihi.

3. **`settings` Tablosu**
   - `key`: Ayar anahtarı (Örn: "theme", "currency").
   - `value`: Ayar değeri (Örn: "dark", "₺").

---

##  Gelecek Geliştirmeler (İsteğe Bağlı)

- Dışa aktarma (Excel, PDF vb.) özellikleri eklenebilir.
- Çoklu kullanıcı ve yetkilendirme (Admin, Personel vb.) eklenebilir.
- Barkod / QR kod okuyucu desteği entegre edilebilir.
sayon
