# 🏆 Aurora CS2 Maç Analiz ve Takip Aracı

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![CS2](https://img.shields.io/badge/CS2-Esports-F0A500?style=for-the-badge&logo=counter-strike&logoColor=white)
![License](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)
![Aurora](https://img.shields.io/badge/Aurora_Gaming-Dünya_%236-00BFFF?style=for-the-badge)
![Language](https://img.shields.io/badge/Dil-Türkçe-FF0000?style=for-the-badge)

```
  █████╗ ██╗   ██╗██████╗  ██████╗ ██████╗  █████╗
 ██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗
 ███████║██║   ██║██████╔╝██║   ██║██████╔╝███████║
 ██╔══██║██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██║
 ██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║
 ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
```

**XANTARES • woxic • MAJ3R • Soulfly • Wicadia**

*"Türk CS'i dünyaya kanıtlıyoruz!"* 🇹🇷

</div>

---

## 🎯 Proje Hakkında

Bu araç, **Aurora Gaming** CS2 kadrosunu yakından takip eden taraftarlar ve geliştiriciler için hazırlanmış, **tamamen Türkçe** bir terminal uygulamasıdır. Aurora Gaming; XANTARES, woxic ve MAJ3R gibi Türk CS2 efsanelerini bünyesine katarak 2025 yılında dünya sıralamalarında üst basamaklara hızla tırmanan bir yapılanmadır.

> 💡 **Neden bu proje?**  
> Gerçek bir CS2 taraftarı hem analitik hem de duygusal düşünür.  
> Bu araç her ikisini de aynı terminalde sunar.

---

## ✨ Özellikler

### 📅 Maç Takibi
- Aurora'nın yaklaşan tüm maçlarını **tarih, saat, rakip ve turnuva** bilgileriyle listeler
- Maç formatı (BO1/BO3/BO5) ve turnuva aşamasını gösterir

### 🔮 "Kazanırsa Ne Olur?" Simülasyonu
- Her maç için **dünya sırası değişim tahmini** hesaplar
- **Play-off'a kalma olasılığını** yüzdesiyle gösterir
- **HLTV puan kazanımını** simüle eder
- BO5 / BO3 format notları ekler

### ⚡ Aura Puanı Sistemi
- Her oyuncu için form + deneyim + performansa dayalı **Aura skoru**
- Görsel `█░░` çubuğu ile renk kodlu seviyeler
- **XANTARES (97 Aura)** zirvede! 🔴

### 🔥 Galibiyet Serisi (Streak Takibi)
- Son maçları analiz ederek **aktif seriyi** tespit eder
- Form yüzdesi ve kazanma/kaybetme dengesini gösterir

### 💬 Taraftar Duygusu
- **Eternal Fire** karşısında özel Türk derbisi mesajları
- Kazanma ihtimaline göre **dinamik taraftar notları**
- Her kapanışta rastgele motivasyon mesajı

### 📊 İstatistik Tablosu
- Toplam maç/galibiyet verisi görsel bar grafikle
- Aurora'nın tüm önemli turnuva başarıları

---

## 🚀 Kurulum ve Kullanım

### Gereksinimler

```bash
Python 3.8 veya üzeri
```

> Bu proje **sıfır harici bağımlılık** ile çalışır. Standart kütüphaneler dışında hiçbir şey kurmanıza gerek yok!

### Çalıştırma

```bash
# Depoyu klonla
git clone https://github.com/dorukcodes/aurora-tracker.git

# Klasöre gir
cd aurora-tracker

# Programı başlat
python aurora_tracker.py
```

### Menü Sistemi

```
  ┌─────────────────────────────────────────────┐
  │          ANA MENÜ                           │
  ├─────────────────────────────────────────────┤
  │  [1] 🎮  Takım Genel Bakış                  │
  │  [2] ⚡  Kadro & Aura Puanları              │
  │  [3] 📊  Son Maçlar & Form                  │
  │  [4] 🔮  Yaklaşan Maçlar & Simülasyon       │
  │  [5] 📋  İstatistik Tablosu                 │
  │  [6] 🚀  HEPSİNİ GÖSTER (Tam Rapor)         │
  │  [0] 🚪  Çıkış                              │
  └─────────────────────────────────────────────┘
```

---

## 💻 Örnek Terminal Çıktısı

```
╔══════════════════════════════════════════════════════════════════════╗
║       🔮 YAKLAŞAN MAÇLAR & SİMÜLASYON 🔮                          ║
╚══════════════════════════════════════════════════════════════════════╝

  ══════════════════════════════════════════════════════════════════════
  ⚔️  MAÇ #3  →  Aurora vs FaZe Clan
  ─────────────────────────────────────────────────────────────────────
  📅 Tarih   : 15 Mayıs 2025, Perşembe
  🕐 Saat    : 20:00 (TR)
  🏟️  Turnuva : ESL Pro League S23
  📍 Aşama   : Grand Final
  🎯 Format  : BO5
  💀 Zorluk  : EFSANE (%91)
  🎲 Kazanma İhtimali : %39

  🔮 KAZANIRSA NE OLUR?
  ···················································
  📈 Sıralama   : Dünya sırası #6 → #3 (+3 basamak ⬆️)
  🏆 Play-off   : %95 ihtimalle Play-off garantisi!
  🎰 HLTV Puan  : +114 tahmini puan
  📝 Format Notu: BO5 zaferi HLTV'de altın harflerle yazılır 📜
    ★ FİNAL SAHNE — Bu zafer tarih kitaplarına geçer!

  💬 Taraftar Notu: 😤 Dev katili olmak için dev olmak lazım — Aurora bunu biliyor!
```

---

## 🏗️ Teknik Mimari

```
aurora_tracker.py
├── veri_yukle()              → Veri katmanı (API'ye hazır)
├── kazanirsa_simulasyon()    → Simülasyon motoru
├── galibiyet_serisi_hesapla()→ Form analizi
├── taraftar_notu_getir()     → Dinamik mesaj sistemi
├── aura_cubugu()             → Görsel çıktı modülü
└── main()                    → Menü döngüsü
```

### 🔌 API Entegrasyonu İçin Hazır Yapı

```python
def veri_yukle() -> dict:
    # Şu an: Statik sözlük verisi
    # Gelecekte: Sadece bu fonksiyonu değiştir!
    
    # HLTV (resmi değil, üçüncü taraf):
    # import requests
    # return requests.get("https://hltv-api.example.com/aurora").json()
    
    # PandaScore API:
    # headers = {"Authorization": f"Bearer {API_KEY}"}
    # return requests.get("https://api.pandascore.co/csgo/teams/11861", headers=headers).json()
```

> **Tasarım Prensibi:** Veri kaynağı değişse bile sadece `veri_yukle()` fonksiyonu güncellenir. Sunum katmanı tamamen ayrı tutulmuştur.

---

## 📁 Dosya Yapısı

```
aurora-tracker/
├── aurora_tracker.py    # Ana uygulama
├── README.md            # Bu dosya
└── LICENSE              # MIT Lisansı
```

---

## 🗺️ Yol Haritası

- [x] Terminal tabanlı menü sistemi
- [x] Maç takip modülü
- [x] Simülasyon motoru ("Kazanırsa Ne Olur?")
- [x] Aura puanı sistemi
- [x] Taraftar notu sistemi
- [x] Galibiyet serisi takibi
- [ ] HLTV / PandaScore API entegrasyonu
- [ ] Maç hatırlatıcı (push notification)
- [ ] Geçmiş maç istatistik veritabanı (SQLite)
- [ ] Web arayüzü (Flask/FastAPI)
- [ ] Discord bot entegrasyonu 🤖

---

## 🏆 Aurora Gaming Hakkında

| Bilgi | Değer |
|-------|-------|
| 🌍 Dünya Sırası | **#6** (Nisan 2025) |
| 🗓️ Kuruluş | 2022, Sırbistan |
| 🏅 En Büyük Başarı | PGL Masters Bucharest 2025 (🥇 $400,000) |
| 🎯 2025 Kadro | XANTARES, woxic, MAJ3R, Soulfly, Wicadia |
| 💰 Toplam Kazanç | $924,200+ |

> Aurora, Nisan 2025'te Eternal Fire'ın Türk kadrosunu transfer ederek dünya sahnesinde gerçek anlamda boy göstermeye başlamıştır.

---

## 👤 Geliştirici

**dorukcodes**

- 🌐 Web: [doruk.codes](https://doruk.codes)
- 💻 GitHub: [@dorukcodes](https://github.com/dorukcodes)

---

## 📄 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakınız.

---

<div align="center">

**🏆 Başarılar Aurora, kupa bizim olsun! 🏆**

*Bu proje bir CS2 taraftarının hem teknik hem duygusal ifadesidir.*

[![Made with Python](https://img.shields.io/badge/Made%20with-Python-3776AB?style=flat-square&logo=python)](https://python.org)
[![Aurora Fan](https://img.shields.io/badge/Aurora-Fan%20Yapımı-00BFFF?style=flat-square)](https://auroragg.com)

</div>
