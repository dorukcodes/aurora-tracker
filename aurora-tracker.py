"""
╔══════════════════════════════════════════════════════════════════════╗
║        🏆 AURORA CS2 MAÇ ANALİZ VE TAKİP ARACI v1.0 🏆             ║
║         XANTARES | woxic | MAJ3R | Soulfly | Wicadia                ║
╚══════════════════════════════════════════════════════════════════════╝

Yazar      : dorukcodes (github.com/dorukcodes)
Açıklama   : Aurora Gaming CS2 takımı için maç takip,
             simülasyon ve taraftar analiz aracı.
Yapı       : Sözlük tabanlı veri modeli, ileride HLTV/PandaScore
             API entegrasyonuna uygun esnek mimari.
"""

import datetime
import random
import sys
import time

# ──────────────────────────────────────────────────────────────────────────────
# RENK ve STIL SABİTLERİ (ANSI)
# ──────────────────────────────────────────────────────────────────────────────

class Renk:
    SIFIRLA     = "\033[0m"
    KALIN       = "\033[1m"
    YESIL       = "\033[92m"
    SARI        = "\033[93m"
    MAVI        = "\033[94m"
    KIRMIZI     = "\033[91m"
    CYAN        = "\033[96m"
    BEYAZ       = "\033[97m"
    GRI         = "\033[90m"
    MAGENTA     = "\033[95m"
    TURUNCU     = "\033[33m"

def renkli(metin: str, *renkler) -> str:
    """Metni istenen renklerle biçimlendirip döndürür."""
    return "".join(renkler) + metin + Renk.SIFIRLA


# ──────────────────────────────────────────────────────────────────────────────
# VERİ MODELI  (API bağlantısına hazır yapı)
# NOT: Gerçek verilerde bu sözlüklerin yerini HLTV/PandaScore API
#       çağrıları alacak. Sadece `veri_yukle()` fonksiyonunu güncellemek yeterli.
# ──────────────────────────────────────────────────────────────────────────────

def veri_yukle() -> dict:
    """
    Takım verilerini yükler.
    İleride API bağlantısı için bu fonksiyonu güncelle:
        import requests
        response = requests.get("https://api.pandascore.co/csgo/teams/aurora", ...)
        return response.json()
    """
    bugun = datetime.date.today()

    return {
        "takim": {
            "isim": "Aurora Gaming",
            "kisaltma": "AUR",
            "ulke": "TR/RS 🇹🇷",
            "dunya_sirasi": 6,
            "kurulis_yili": 2022,
            "toplam_mac": 461,
            "galibiyet": 268,
            "kazanma_yuzdesi": 58.1,
        },

        "kadro": [
            {"nick": "XANTARES",  "isim": "İsmailcan Dörtkardeş", "rol": "Rifler/Entry",   "aura_puani": 97},
            {"nick": "woxic",     "isim": "Özgür Eker",           "rol": "AWPer",           "aura_puani": 93},
            {"nick": "MAJ3R",     "isim": "Engin Küpeli",         "rol": "IGL/Rifler",      "aura_puani": 89},
            {"nick": "Soulfly",   "isim": "Caner Kesici",         "rol": "Support/Rifler",  "aura_puani": 85},
            {"nick": "Wicadia",   "isim": "Ali Haydar Yalçın",    "rol": "Rifler/Lurker",   "aura_puani": 83},
        ],

        "son_maclar": [
            {
                "rakip": "Natus Vincere",
                "tarih": str(bugun - datetime.timedelta(days=7)),
                "sonuc": "KAZANDI",
                "skor": "2-0",
                "turnuva": "ESL Pro League S23",
            },
            {
                "rakip": "FaZe Clan",
                "tarih": str(bugun - datetime.timedelta(days=14)),
                "sonuc": "KAYBETTİ",
                "skor": "1-2",
                "turnuva": "ESL Pro League S23",
            },
            {
                "rakip": "G2 Esports",
                "tarih": str(bugun - datetime.timedelta(days=21)),
                "sonuc": "KAZANDI",
                "skor": "2-1",
                "turnuva": "ESL Pro League S23",
            },
            {
                "rakip": "Team Spirit",
                "tarih": str(bugun - datetime.timedelta(days=28)),
                "sonuc": "KAZANDI",
                "skor": "2-0",
                "turnuva": "IEM Dallas 2025",
            },
            {
                "rakip": "Virtus.pro",
                "tarih": str(bugun - datetime.timedelta(days=35)),
                "sonuc": "KAYBETTİ",
                "skor": "0-2",
                "turnuva": "IEM Dallas 2025",
            },
        ],

        "gelecek_maclar": [
            {
                "id": 1,
                "rakip": "Natus Vincere",
                "tarih": bugun + datetime.timedelta(days=3),
                "saat": "19:00",
                "turnuva": "ESL Pro League S23",
                "format": "BO3",
                "aşama": "Çeyrek Final",
                "rakip_sirasi": 4,
                "zorluk_yuzdesi": 82,
                "kazanma_olasiligi": 48,
            },
            {
                "id": 2,
                "rakip": "MOUZ",
                "tarih": bugun + datetime.timedelta(days=8),
                "saat": "17:30",
                "turnuva": "ESL Pro League S23",
                "format": "BO3",
                "aşama": "Yarı Final",
                "rakip_sirasi": 3,
                "zorluk_yuzdesi": 78,
                "kazanma_olasiligi": 51,
            },
            {
                "id": 3,
                "rakip": "FaZe Clan",
                "tarih": bugun + datetime.timedelta(days=15),
                "saat": "20:00",
                "turnuva": "ESL Pro League S23",
                "format": "BO5",
                "aşama": "Grand Final",
                "rakip_sirasi": 1,
                "zorluk_yuzdesi": 91,
                "kazanma_olasiligi": 39,
            },
            {
                "id": 4,
                "rakip": "Eternal Fire",
                "tarih": bugun + datetime.timedelta(days=22),
                "saat": "18:00",
                "turnuva": "StarLadder Budapest Major 2025",
                "format": "BO3",
                "aşama": "Grup Aşaması",
                "rakip_sirasi": 9,
                "zorluk_yuzdesi": 65,
                "kazanma_olasiligi": 71,
            },
            {
                "id": 5,
                "rakip": "Team Vitality",
                "tarih": bugun + datetime.timedelta(days=29),
                "saat": "21:00",
                "turnuva": "StarLadder Budapest Major 2025",
                "format": "BO3",
                "aşama": "Grup Aşaması",
                "rakip_sirasi": 2,
                "zorluk_yuzdesi": 88,
                "kazanma_olasiligi": 44,
            },
        ],
    }


# ──────────────────────────────────────────────────────────────────────────────
# YARDIMCI FONKSİYONLAR
# ──────────────────────────────────────────────────────────────────────────────

def bolme_cizgisi(uzunluk: int = 70, karakter: str = "─") -> str:
    return renkli(karakter * uzunluk, Renk.GRI)


def baslik_kutusu(metin: str, ikon: str = "🏆") -> None:
    genislik = 68
    bosluk = (genislik - len(metin) - 4) // 2
    print()
    print(renkli("╔" + "═" * genislik + "╗", Renk.CYAN, Renk.KALIN))
    print(renkli("║" + " " * bosluk + f" {ikon} {metin} {ikon}" + " " * bosluk + "║", Renk.CYAN, Renk.KALIN))
    print(renkli("╚" + "═" * genislik + "╝", Renk.CYAN, Renk.KALIN))


def yukleniyor_animasyonu(mesaj: str = "Veriler yükleniyor", sure: float = 0.8) -> None:
    adimlar = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    bitis = time.time() + sure
    i = 0
    while time.time() < bitis:
        print(f"\r{renkli(adimlar[i % len(adimlar)], Renk.CYAN)} {renkli(mesaj + '...', Renk.GRI)}",
              end="", flush=True)
        time.sleep(0.08)
        i += 1
    print(f"\r{renkli('✓', Renk.YESIL)} {renkli(mesaj, Renk.GRI)} {renkli('tamamlandı!', Renk.YESIL)}")


def aura_cubugu(puan: int, genislik: int = 20) -> str:
    """Görsel aura çubuğu oluşturur."""
    dolu = int((puan / 100) * genislik)
    bos  = genislik - dolu
    if puan >= 90:
        renk = Renk.KIRMIZI
        sembol = "█"
    elif puan >= 75:
        renk = Renk.TURUNCU
        sembol = "█"
    else:
        renk = Renk.SARI
        sembol = "█"
    cizgi = renkli(sembol * dolu, renk) + renkli("░" * bos, Renk.GRI)
    return f"[{cizgi}] {renkli(str(puan), renk, Renk.KALIN)}/100"


def zorluk_rengi(zorluk: int) -> str:
    if zorluk >= 85:
        return renkli(f"EFSANE (%{zorluk})", Renk.KIRMIZI, Renk.KALIN)
    elif zorluk >= 70:
        return renkli(f"ZOR (%{zorluk})", Renk.TURUNCU, Renk.KALIN)
    elif zorluk >= 50:
        return renkli(f"ORTA (%{zorluk})", Renk.SARI, Renk.KALIN)
    else:
        return renkli(f"KOLAY (%{zorluk})", Renk.YESIL, Renk.KALIN)


# ──────────────────────────────────────────────────────────────────────────────
# TARAFTAR NOTU FONKSİYONU
# ──────────────────────────────────────────────────────────────────────────────

def taraftar_notu_getir(rakip: str, kazanma_olasiligi: int) -> str:
    """
    Rakip ve kazanma olasılığına göre uygun taraftar mesajı döndürür.
    Eternal Fire ve belirli rakipler için özel mesajlar içerir.
    """
    eternal_fire_notlar = [
        "🔥 EF kardeşlerimiz... Bu maç özel, kalpler karışık ama saha ayrı!",
        "🔥 Eternal Fire'a saygı, Aurora'ya zafer! Arkadaşları sahnede yenin!",
        "🔥 Türk derbisi! XANTARES vs eski ekibi — sinir krizi garantili!",
        "🔥 EF ile aynı DNA, farklı formalar. Kupa Aurora'da kalsın!",
    ]

    yuksek_olasilik_notlar = [
        "💪 Aura yükseliyor, bu maç bizim!",
        "🚀 Kadro formda, rakip titresin!",
        "🏆 Bu galibiyetle tavan yapıyoruz!",
        "💚 XANTARES ateş açtı mı durmuyor — hazır mısın?",
        "✨ Wicadia lurk, XANTARES entry, woxic AWP = GG EZ!",
    ]

    dusuk_olasilik_notlar = [
        "😤 Kâğıt üzerinde zor ama kalp üzerinde değil, haydi Aurora!",
        "🔥 Dev katili olmak için dev olmak lazım — Aurora bunu biliyor!",
        "💜 Underdog olmak bize yakışır, sürpriz hazır mı?",
        "🎯 MAJ3R stratejisi kuruldu, woxic AWP hazır — imkânsız yok!",
        "⚡ Umarım kazanırız! Ama gösteri yaparlar kesin!",
    ]

    standart_notlar = [
        "🎮 Her round için ter döküyoruz taraftarca!",
        "💛 Kadro kararlı, kupa görünüyor — git Aurora!",
        "🏅 Umarım kazanırız! Türk CS'i dünyaya kanıtlıyoruz!",
        "🔮 Kaderini kendin yaz, Aurora!",
    ]

    if "eternal" in rakip.lower() or "ef" in rakip.lower():
        return random.choice(eternal_fire_notlar)
    elif kazanma_olasiligi >= 65:
        return random.choice(yuksek_olasilik_notlar)
    elif kazanma_olasiligi <= 45:
        return random.choice(dusuk_olasilik_notlar)
    else:
        return random.choice(standart_notlar)


# ──────────────────────────────────────────────────────────────────────────────
# KAZANİRSA NE OLUR? SİMÜLASYONU
# ──────────────────────────────────────────────────────────────────────────────

def kazanirsa_simulasyon(mac: dict, takim_sirasi: int) -> dict:
    """
    Maçı kazanmanın olası sonuçlarını simüle eder.
    Döndürür: sıralama değişimi, play-off ihtimali, turnuva etkisi.

    TODO: Gerçek ELO/HLTV puanı hesaplaması için API entegrasyonu ekle.
    """
    rakip_sirasi = mac["rakip_sirasi"]
    zorluk = mac["zorluk_yuzdesi"]
    asama = mac["aşama"]
    format_tip = mac["format"]

    # Sıralama kazancı hesapla (rakip ne kadar iyi → o kadar fazla puan)
    baz_kazanim = max(1, (rakip_sirasi - takim_sirasi + 10))
    bonus = 3 if "Final" in asama else (2 if "Yarı" in asama else 1)
    tahmin_siralama = max(1, takim_sirasi - (baz_kazanim + bonus))

    # Turnuva aşamasına göre play-off ihtimali
    playoff_base = {
        "Grup Aşaması": 35,
        "Çeyrek Final": 60,
        "Yarı Final": 80,
        "Grand Final": 95,
    }
    playoff_olasilik = playoff_base.get(asama, 50)
    if zorluk >= 85:
        playoff_olasilik -= 8
    elif zorluk <= 60:
        playoff_olasilik += 12

    # HLTV puan tahmini
    hltv_puan = int(zorluk * 0.9 + (100 - takim_sirasi) * 0.4 + bonus * 15)

    # Format bonusu
    format_notu = ""
    if format_tip == "BO5":
        format_notu = "BO5 zaferi HLTV'de altın harflerle yazılır 📜"
    elif format_tip == "BO3":
        format_notu = "BO3 formatı — her map kritik, mental güçlü olmalı 🧠"

    return {
        "yeni_siralama_tahmini": tahmin_siralama,
        "siralama_kazanimi": takim_sirasi - tahmin_siralama,
        "playoff_olasiligi": min(99, playoff_olasilik),
        "hltv_puan": hltv_puan,
        "format_notu": format_notu,
        "asama": asama,
    }


# ──────────────────────────────────────────────────────────────────────────────
# GALİBİYET SERİSİ SAYACI
# ──────────────────────────────────────────────────────────────────────────────

def galibiyet_serisi_hesapla(son_maclar: list) -> dict:
    """Son maçları analiz ederek mevcut seriyi ve istatistikleri döndürür."""
    seri = 0
    seri_tipi = None
    win_streak = 0
    lose_streak = 0

    for mac in son_maclar:
        if seri == 0:
            seri_tipi = mac["sonuc"]
            seri = 1
        elif mac["sonuc"] == seri_tipi:
            seri += 1
        else:
            break

    kazanilan = sum(1 for m in son_maclar if m["sonuc"] == "KAZANDI")
    kaybedilen = sum(1 for m in son_maclar if m["sonuc"] == "KAYBETTİ")

    return {
        "mevcut_seri": seri,
        "seri_tipi": seri_tipi,
        "son_5_kazanim": kazanilan,
        "son_5_kayip": kaybedilen,
        "form_yuzdesi": round((kazanilan / len(son_maclar)) * 100),
    }


# ──────────────────────────────────────────────────────────────────────────────
# EKRAN MODÜLLERI
# ──────────────────────────────────────────────────────────────────────────────

def hosgeldin_ekrani() -> None:
    """Açılış animasyonu ve başlık."""
    print()
    print(renkli("  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░", Renk.GRI))
    print()
    satir1 = "   █████╗ ██╗   ██╗██████╗  ██████╗ ██████╗  █████╗ "
    satir2 = "  ██╔══██╗██║   ██║██╔══██╗██╔═══██╗██╔══██╗██╔══██╗"
    satir3 = "  ███████║██║   ██║██████╔╝██║   ██║██████╔╝███████║"
    satir4 = "  ██╔══██║██║   ██║██╔══██╗██║   ██║██╔══██╗██╔══██║"
    satir5 = "  ██║  ██║╚██████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║"
    satir6 = "  ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝"

    for s in [satir1, satir2, satir3, satir4, satir5, satir6]:
        print(renkli(s, Renk.CYAN, Renk.KALIN))
        time.sleep(0.04)

    print()
    print(renkli("          🏆  CS2 MAÇ ANALİZ & TAKİP ARACI  🏆", Renk.SARI, Renk.KALIN))
    print(renkli("       XANTARES • woxic • MAJ3R • Soulfly • Wicadia", Renk.GRI))
    print()
    print(renkli("  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░", Renk.GRI))
    print()

    yukleniyor_animasyonu("Takım verileri alınıyor")
    yukleniyor_animasyonu("Maç takvimi senkronize ediliyor")
    yukleniyor_animasyonu("Simülasyon motoru başlatılıyor")


def takim_genel_bakis(veri: dict) -> None:
    """Takım bilgileri ve genel istatistikler."""
    t = veri["takim"]
    baslik_kutusu("TAKIM GENEL BAKIŞ", "🎮")

    print(f"\n  {'Takım':<20} {renkli(t['isim'], Renk.CYAN, Renk.KALIN)}")
    print(f"  {'Ülke/Bölge':<20} {t['ulke']}")
    _s = f"#{t['dunya_sirasi']}"
    print(f"  {'Dünya Sırası':<20} {renkli(_s, Renk.SARI, Renk.KALIN)}")
    print(f"  {'Toplam Maç':<20} {t['toplam_mac']}")
    print(f"  {'Galibiyet':<20} {renkli(str(t['galibiyet']), Renk.YESIL)}")
    _k = f"%{t['kazanma_yuzdesi']}"
    print(f"  {'Kazanma %':<20} {renkli(_k, Renk.TURUNCU, Renk.KALIN)}")
    print()


def kadro_goster(kadro: list) -> None:
    """Oyuncu kadrosunu aura puanlarıyla birlikte gösterir."""
    baslik_kutusu("OYUNCU KADROSU & AURA PUANLARI", "⚡")
    print()
    print(f"  {renkli('Nick', Renk.KALIN):<22} {renkli('Rol', Renk.KALIN):<28} {renkli('Aura Seviyesi', Renk.KALIN)}")
    print("  " + bolme_cizgisi(64))

    for oyuncu in sorted(kadro, key=lambda x: x["aura_puani"], reverse=True):
        nick = renkli(f"★ {oyuncu['nick']}", Renk.SARI, Renk.KALIN)
        rol  = renkli(oyuncu["rol"], Renk.GRI)
        aura = aura_cubugu(oyuncu["aura_puani"])
        print(f"  {nick:<32} {rol:<28} {aura}")

    print()
    print(f"  {renkli('💡 Aura = Mevcut Form + Deneyim + Performans', Renk.GRI)}")
    print()


def son_maclar_goster(son_maclar: list, seri_bilgisi: dict) -> None:
    """Son maç sonuçlarını ve galibiyet serisini gösterir."""
    baslik_kutusu("SON MAÇLAR & FORM ANALİZİ", "📊")
    print()

    # Seri bilgisi
    seri_renk = Renk.YESIL if seri_bilgisi["seri_tipi"] == "KAZANDI" else Renk.KIRMIZI
    seri_emoji = "🔥" if seri_bilgisi["seri_tipi"] == "KAZANDI" else "❄️"
    print(f"  {seri_emoji} Mevcut Seri: {renkli(str(seri_bilgisi['mevcut_seri']), seri_renk, Renk.KALIN)} "
          f"maç üst üste {renkli(seri_bilgisi['seri_tipi'], seri_renk, Renk.KALIN)}")
    print(f"  📈 Son 5 Maç: {renkli(str(seri_bilgisi['son_5_kazanim']), Renk.YESIL)} kazandı / "
          f"{renkli(str(seri_bilgisi['son_5_kayip']), Renk.KIRMIZI)} kaybetti "
          f"({renkli('%' + str(seri_bilgisi['form_yuzdesi']), Renk.TURUNCU)} form)")
    print()
    print("  " + bolme_cizgisi(64))
    print(f"  {'Tarih':<14} {'Rakip':<22} {'Skor':<10} {'Turnuva':<20}")
    print("  " + bolme_cizgisi(64))

    for mac in son_maclar:
        sonuc_renk = Renk.YESIL if mac["sonuc"] == "KAZANDI" else Renk.KIRMIZI
        sonuc_ikon = "✅" if mac["sonuc"] == "KAZANDI" else "❌"
        tarih = renkli(mac["tarih"], Renk.GRI)
        rakip = renkli(mac["rakip"], Renk.BEYAZ)
        skor  = renkli(mac["skor"], sonuc_renk, Renk.KALIN)
        turnuva = renkli(mac["turnuva"], Renk.GRI)
        print(f"  {tarih:<14} {sonuc_ikon} {rakip:<22} {skor:<18} {turnuva}")

    print()


def gelecek_maclar_goster(maclar: list, takim_sirasi: int) -> None:
    """Gelecek maçları detaylı simülasyon bilgileriyle gösterir."""
    baslik_kutusu("YAKLAŞAN MAÇLAR & SİMÜLASYON", "🔮")

    for mac in maclar:
        sim = kazanirsa_simulasyon(mac, takim_sirasi)
        taraftar_notu = taraftar_notu_getir(mac["rakip"], mac["kazanma_olasiligi"])

        # Maç başlığı
        print()
        print("  " + bolme_cizgisi(68, "═"))
        print(f"  {renkli('⚔️  MAÇ #' + str(mac['id']), Renk.SARI, Renk.KALIN)}  "
              f"{renkli('→', Renk.GRI)}  "
              f"{renkli('Aurora', Renk.CYAN, Renk.KALIN)} "
              f"{renkli('vs', Renk.GRI)} "
              f"{renkli(mac['rakip'], Renk.KIRMIZI, Renk.KALIN)}")
        print("  " + bolme_cizgisi(68, "─"))

        # Maç detayları
        tarih_str = mac["tarih"].strftime("%d %B %Y, %A")
        print(f"  📅 Tarih   : {renkli(tarih_str, Renk.BEYAZ)}")
        print(f"  🕐 Saat    : {renkli(mac['saat'] + ' (TR)', Renk.BEYAZ)}")
        print(f"  🏟️  Turnuva : {renkli(mac['turnuva'], Renk.CYAN)}")
        print(f"  📍 Aşama   : {renkli(mac['aşama'], Renk.MAGENTA, Renk.KALIN)}")
        print(f"  🎯 Format  : {renkli(mac['format'], Renk.SARI)}")
        print(f"  💀 Zorluk  : {zorluk_rengi(mac['zorluk_yuzdesi'])}")

        kaz_ren = Renk.YESIL if mac["kazanma_olasiligi"] >= 50 else Renk.TURUNCU
        print(f"  🎲 Kazanma İhtimali : {renkli('%' + str(mac['kazanma_olasiligi']), kaz_ren, Renk.KALIN)}")

        # Kazanırsa ne olur?
        print()
        print(f"  {renkli('🔮 KAZANIRSA NE OLUR?', Renk.MAGENTA, Renk.KALIN)}")
        print("  " + bolme_cizgisi(50, "·"))

        yeni_siralama = sim["yeni_siralama_tahmini"]
        kazanim = sim["siralama_kazanimi"]

        if kazanim > 0:
            siralama_mesaj = (f"Dünya sırası #{takim_sirasi} → "
                              f"{renkli(f'#{yeni_siralama}', Renk.YESIL, Renk.KALIN)} "
                              f"({renkli(f'+{kazanim} basamak ⬆️', Renk.YESIL)})")
        else:
            siralama_mesaj = f"Sıralama sabit kalır ({renkli(f'#{takim_sirasi}', Renk.SARI)})"

        print(f"  📈 Sıralama   : {siralama_mesaj}")
        print(f"  🏆 Play-off   : {renkli('%' + str(sim['playoff_olasiligi']) + ' ihtimalle Play-off garantisi!', Renk.SARI, Renk.KALIN)}")
        print(f"  🎰 HLTV Puan  : {renkli('+' + str(sim['hltv_puan']) + ' tahmini puan', Renk.CYAN)}")

        if sim["format_notu"]:
            print(f"  📝 Format Notu: {renkli(sim['format_notu'], Renk.GRI)}")

        # Aşama yorumu
        if "Final" in sim["asama"]:
            print(f"  {renkli('  ★ FİNAL SAHNE — Bu zafer tarih kitaplarına geçer!', Renk.SARI, Renk.KALIN)}")

        # Taraftar notu
        print()
        print(f"  {renkli('💬 Taraftar Notu:', Renk.TURUNCU, Renk.KALIN)} {renkli(taraftar_notu, Renk.BEYAZ)}")
        print()

    print("  " + bolme_cizgisi(68, "═"))


def ana_istatistikler(veri: dict) -> None:
    """Özet istatistik tablosu."""
    baslik_kutusu("HIZLI İSTATİSTİKLER", "📋")
    t = veri["takim"]

    toplam_mac = t["toplam_mac"]
    galibiyet  = t["galibiyet"]
    maglup     = toplam_mac - galibiyet

    print()
    print(f"  {'Kategori':<30} {'Değer':<20} {'Bar'}")
    print("  " + bolme_cizgisi(64))

    veriler = [
        ("Toplam Maç",       toplam_mac, toplam_mac, Renk.CYAN),
        ("Galibiyet",        galibiyet,  toplam_mac, Renk.YESIL),
        ("Mağlubiyet",       maglup,     toplam_mac, Renk.KIRMIZI),
        ("Kazanma Oranı",    int(t["kazanma_yuzdesi"]), 100, Renk.TURUNCU),
    ]

    for kategori, deger, maksimum, renk in veriler:
        bar_dolusu  = int((deger / maksimum) * 25) if maksimum > 0 else 0
        bar         = renkli("█" * bar_dolusu, renk) + renkli("░" * (25 - bar_dolusu), Renk.GRI)
        deger_str   = renkli(str(deger), renk, Renk.KALIN)
        print(f"  {kategori:<30} {deger_str:<28} {bar}")

    print()

    # Turnuva başarıları
    print(f"  {renkli('🏆 Öne Çıkan Başarılar:', Renk.SARI, Renk.KALIN)}")
    basarilar = [
        ("🥇", "PGL Masters Bucharest 2025",    "$400,000"),
        ("🥈", "Esports World Cup 2025",         "$230,000"),
        ("🥉", "PGL Astana 2025",                "3. Sıra"),
        ("🥇", "Skyesports Masters 2024",        "$105,000"),
    ]
    for madalya, turnuva, odul in basarilar:
        print(f"     {madalya} {renkli(turnuva, Renk.BEYAZ)} — {renkli(odul, Renk.YESIL)}")
    print()


def veda_mesaji() -> None:
    """Program kapanış mesajı."""
    print()
    print(bolme_cizgisi(70, "═"))
    print()
    mesajlar = [
        "🏆 Başarılar Aurora, kupa bizim olsun!",
        "🔥 XANTARES ateş açsın, woxic'in AWP'si konuşsun!",
        "💚 Türk CS'i zirveye taşıyacak, söz veriyoruz!",
        "🎮 Maçları kaçırma, aura yükseliyor!",
    ]
    print(renkli("  " + random.choice(mesajlar), Renk.SARI, Renk.KALIN))
    print()
    print(renkli("  github.com/dorukcodes  •  doruk.codes", Renk.GRI))
    print(renkli(f"  {datetime.datetime.now().strftime('%d.%m.%Y %H:%M')}", Renk.GRI))
    print()
    print(bolme_cizgisi(70, "═"))
    print()


# ──────────────────────────────────────────────────────────────────────────────
# MENÜ SİSTEMİ
# ──────────────────────────────────────────────────────────────────────────────

def menu_goster() -> None:
    print()
    print(renkli("  ┌─────────────────────────────────────────────┐", Renk.CYAN))
    print(renkli("  │", Renk.CYAN) + renkli("          ANA MENÜ", Renk.SARI, Renk.KALIN) + renkli("                          │", Renk.CYAN))
    print(renkli("  ├─────────────────────────────────────────────┤", Renk.CYAN))
    secenekler = [
        ("1", "🎮", "Takım Genel Bakış"),
        ("2", "⚡", "Kadro & Aura Puanları"),
        ("3", "📊", "Son Maçlar & Form"),
        ("4", "🔮", "Yaklaşan Maçlar & Simülasyon"),
        ("5", "📋", "İstatistik Tablosu"),
        ("6", "🚀", "HEPSİNİ GÖSTER (Tam Rapor)"),
        ("0", "🚪", "Çıkış"),
    ]
    for no, ikon, aciklama in secenekler:
        print(renkli("  │", Renk.CYAN) +
              f"  {renkli('[' + no + ']', Renk.SARI, Renk.KALIN)} {ikon}  {renkli(aciklama, Renk.BEYAZ):<38}" +
              renkli("│", Renk.CYAN))
    print(renkli("  └─────────────────────────────────────────────┘", Renk.CYAN))
    print()


def tam_rapor(veri: dict, seri: dict) -> None:
    """Tüm modülleri sırayla çalıştırır."""
    takim_genel_bakis(veri)
    kadro_goster(veri["kadro"])
    son_maclar_goster(veri["son_maclar"], seri)
    gelecek_maclar_goster(veri["gelecek_maclar"], veri["takim"]["dunya_sirasi"])
    ana_istatistikler(veri)


# ──────────────────────────────────────────────────────────────────────────────
# ANA PROGRAM
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    hosgeldin_ekrani()

    veri = veri_yukle()
    seri = galibiyet_serisi_hesapla(veri["son_maclar"])

    try:
        while True:
            menu_goster()
            secim = input(renkli("  ➤ Seçiminiz: ", Renk.CYAN, Renk.KALIN)).strip()

            if secim == "1":
                takim_genel_bakis(veri)
            elif secim == "2":
                kadro_goster(veri["kadro"])
            elif secim == "3":
                son_maclar_goster(veri["son_maclar"], seri)
            elif secim == "4":
                gelecek_maclar_goster(veri["gelecek_maclar"], veri["takim"]["dunya_sirasi"])
            elif secim == "5":
                ana_istatistikler(veri)
            elif secim == "6":
                tam_rapor(veri, seri)
            elif secim == "0":
                veda_mesaji()
                sys.exit(0)
            else:
                print(renkli("\n  ⚠️  Geçersiz seçim! Lütfen 0-6 arası bir sayı girin.\n", Renk.KIRMIZI))

    except KeyboardInterrupt:
        veda_mesaji()
        sys.exit(0)


if __name__ == "__main__":
    main()
