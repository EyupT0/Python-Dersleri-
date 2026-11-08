# 07b - Döngüler ALIŞTIRMA ve ÖRNEK DOSYASI (for / while)
# Öğreneceklerin: for, while, range(), break, continue, sayaç, akümülatör, iç içe döngü
#
# Çalıştırmak için:  python3 07b_donguler_alistirmalar.py
#
# NOT: Bu dosyadaki her örnek çalışır ve çıktı üretir.
#      input() kullanan örnekler yorum satırına alındı; istersen başındaki '#' işaretini kaldırıp dene.
#      Alıştırmaların çözümleri ilgili sorunun HEMEN ALTINDA "ÇÖZÜM" başlığı altında verildi.
#      Önce kendin dene, takılırsan çözüme bak.

# ==================================================================
# BÖLÜM 1 - for DÖNGÜSÜ ÖRNEKLERİ
# ==================================================================

print("=== Örnek 1: 1'den 10'a kadar say ===")
for sayi in range(1, 11):          # 11 dahil değil
    print(sayi, end=" ")
print()

print("\n=== Örnek 2: 1'den 20'ye kadar ÇİFT sayılar ===")
# 1. yol: adım kullanmak (en kısa yol)
for sayi in range(2, 21, 2):
    print(sayi, end=" ")
print()

# 2. yol: koşul + continue
for sayi in range(1, 21):
    if sayi % 2 != 0:              # tek ise
        continue                   # bu turu atla
    print(sayi, end=" ")
print()

print("\n=== Örnek 3: 1'den 100'e kadar toplam (akümülatör deseni) ===")
toplam = 0                         # biriktiriciyı DIŞARIDA tanımla
for sayi in range(1, 101):
    toplam += sayi                 # toplam = toplam + sayi
print("Toplam:", toplam)           # 5050

print("\n=== Örnek 4: Bir sayının çarpım (faktöriyel) hesabı ===")
sayi = 5
faktoriyel = 1                     # çarpmada başlangıç değeri 1'dir (0 değil!)
for i in range(1, sayi + 1):
    faktoriyel *= i
print(f"{sayi}! = {faktoriyel}")   # 120

print("\n=== Örnek 5: Bir kelimenin harflerini alt alta yazdır ===")
kelime = "Python"
for harf in kelime:
    print(harf)

print("\n=== Örnek 6: 5x5 yıldız karesi ===")
for satir in range(5):
    for sutun in range(5):
        print("*", end=" ")
    print()                        # satır bitince alt satıra geç

print("\n=== Örnek 7: Yıldızlarla üçgen ===")
for i in range(1, 6):
    print("*" * i)

print("\n=== Örnek 8: 1-100 arası 3'e ve 5'e tam bölünenler (FizzBuzz mantığı) ===")
for sayi in range(1, 101):
    if sayi % 15 == 0:             # 3 ve 5 -> 15'in katı
        print("FizzBuzz", end=" ")
    elif sayi % 3 == 0:
        print("Fizz", end=" ")
    elif sayi % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(sayi, end=" ")
print()

# ==================================================================
# BÖLÜM 2 - while DÖNGÜSÜ ÖRNEKLERİ
# ==================================================================

print("\n=== Örnek 9: Sayaç ile 0'dan 4'e ===")
sayac = 0
while sayac < 5:
    print("Sayaç:", sayac)
    sayac += 1                     # ⚠️ bu satır olmazsa SONSUZ DÖNGÜ

print("\n=== Örnek 10: Sayının basamaklarını topla (while + // ve %) ===")
sayi = 4729
gecici = sayi
basamak_toplami = 0
while gecici > 0:
    basamak_toplami += gecici % 10   # son basamağı al
    gecici //= 10                    # son basamağı sil
print(f"{sayi} sayısının basamakları toplamı: {basamak_toplami}")   # 22

print("\n=== Örnek 11: Sayıyı ters çevirme (while) ===")
sayi = 1234
gecici = sayi
ters = 0
while gecici > 0:
    ters = ters * 10 + gecici % 10
    gecici //= 10
print(f"{sayi} sayısının tersi: {ters}")   # 4321

print("\n=== Örnek 12: 'q' yazılana kadar sayı toplama (MENÜ DESENİ) ===")
# Aşağıdaki blok input() istediği için yorumda bırakıldı. Kaldırıp deneyebilirsin.
#
# toplam = 0
# while True:                          # sonsuz döngü
#     cevap = input("Sayı gir (çıkmak için q): ")
#     if cevap.lower() == "q":
#         break                          # döngüden çık
#     toplam += int(cevap)
# print("Toplam:", toplam)
#
# Aynı mantığın input'suz, otomatik test edilebilir hâli:
girdiler = ["10", "25", "5", "q"]      # sanki kullanıcı bunları yazmış gibi
toplam = 0
for girdi in girdiler:
    if girdi == "q":
        break
    toplam += int(girdi)
print("Girilen sayıların toplamı:", toplam)   # 40

print("\n=== Örnek 13: while + doğrulama (parola denemesi) ===")
dogru_parola = "python123"
denemeler = ["abc", "123", "python123"]
hak = 0
while hak < len(denemeler):
    tahmin = denemeler[hak]
    hak += 1
    if tahmin == dogru_parola:
        print(f"Parola doğru! {hak}. denemede bulundu.")
        break
    print(f"{hak}. deneme yanlış: {tahmin}")
else:
    print("Hakkın bitti.")              # while da else destekler (break olmazsa çalışır)

print("\n=== Örnek 14: Asal sayı kontrolü (for + break + else) ===")
sayi = 29
for bolen in range(2, int(sayi ** 0.5) + 1):
    if sayi % bolen == 0:
        print(sayi, "asal değil (bölen:", bolen, ")")
        break
else:                                   # hiç bölen bulunmadıysa
    print(sayi, "asal sayıdır.")

print("\n=== Örnek 15: 1-50 arası asal sayıları listele ===")
asallar = []
for sayi in range(2, 51):
    for bolen in range(2, sayi):
        if sayi % bolen == 0:
            break
    else:
        asallar.append(sayi)
print(asallar)

# ==================================================================
# BÖLÜM 3 - for ve while KARŞILAŞTIRMASI
# ==================================================================
#
#   for   -> Kaç kez döneceği BELLİ ise (liste, range, kelime, dosya satırları)
#   while -> Kaç kez döneceği BELİRSİZ ise (kullanıcı q yazana kadar, koşul sağlanana kadar)
#
#   break    -> döngüyü tamamen bitirir
#   continue -> o turu atlar, sonraki tura geçer
#   else     -> döngü break OLMADAN bittiyse çalışır

# ==================================================================
# ALIŞTIRMALAR  (çözümler hemen altında)
# ==================================================================

# ------------------------------------------------------------------
# ALIŞTIRMA 1
# 1'den 20'ye kadar olan sayıların KARESİNİ yazdır.
# Beklenen çıktı: 1 4 9 16 ... 400
# ------------------------------------------------------------------
print("\n--- Alıştırma 1: 1-20 arası sayıların karesi ---")
for sayi in range(1, 21 ):
    print(sayi ** 2)
# ------------------------------------------------------------------
# ALIŞTIRMA 2
# Kullanıcıdan alınan bir sayıya kadar olan sayıların toplamını hesapla.
# input() kullanmadan, sayi = 25 kabul ederek yaz.
# ------------------------------------------------------------------
print("\n--- Alıştırma 2: 1..N toplamı ---")
sayi = int(input("Bir sayı giriniz: "))
toplam = 0
for i in range(1, sayi + 1):
    toplam += i
print(f"1..{sayi} toplamı: {toplam}")

# ------------------------------------------------------------------
# ALIŞTIRMA 3
# 1'den 10'a kadar sayıların 3'erli katlarını yazdır (3, 6, 9 ... 30).
# ------------------------------------------------------------------
print("\n--- Alıştırma 3: 3'ün katları ---")
for i in range(0,10,3):
    print(i)
# ------------------------------------------------------------------
# ALIŞTIRMA 4
# Bir kelimenin harflerini aralarına "-" koyarak yazdır: p-y-t-h-o-n
# ------------------------------------------------------------------
print("\n--- Alıştırma 4: harfleri tireyle birleştir ---")
kelime = "python"
sonuc = ""
for harf in kelime:
    sonuc += harf + "-"
print(sonuc[:-1])            # sondaki fazla "-" i çıkar

# ------------------------------------------------------------------
# ALIŞTIRMA 5
# 1'den 50'ye kadar sayılardan hem 4'e hem 6'ya bölünenleri yazdır.
# ------------------------------------------------------------------
print("\n--- Alıştırma 5: 4 ve 6'ya bölünenler ---")
for i in range(0,51):
    if i % 4 == 0 and i % 6 ==0:
        print(i)
# ------------------------------------------------------------------
# ALIŞTIRMA 6
# Tersten 10'dan 1'e kadar say ve sonunda "Başla!" yaz.
# ------------------------------------------------------------------
print("\n--- Alıştırma 6: geri sayım ---")
for i in range(10 ,0, -1):
    print(i)
print("Başla!")

# ------------------------------------------------------------------
# ALIŞTIRMA 7
# while ile: 1'den başlayıp her adımda 2 ile çarp; 1000'i geçince dur.
# Kaç adımda geçtiğini yazdır.
# ------------------------------------------------------------------
print("\n--- Alıştırma 7: 2'nin kuvvetleri ---")
i = 1
adim=0
while i <=1000:
    i = i*2
    adim += 1
print(i)
print(f"sonuca {adim} adımda ulaşıldı")
# ------------------------------------------------------------------
# ALIŞTIRMA 8
# while ile: bir sayının rakamlarını topla. sayi = 98765
# ------------------------------------------------------------------
print("\n--- Alıştırma 8: rakamlar toplamı ---")
sayi = 2**902
gecici = sayi
toplam =0
while gecici > 0:
    toplam += gecici % 10
    gecici //= 10
print(f"{sayi}'sının rakamlarının toplamı = {toplam}")

# ------------------------------------------------------------------
# ALIŞTIRMA 9
# 1'den 100'e kadar sayılarda 3'e bölünen İLK 5 sayıyı yazdır,
# sonra döngüden çık (break + sayaç).
# ------------------------------------------------------------------
print("\n--- Alıştırma 9: ilk 5 sayı (break) ---")
bulunan = 0
for sayi in range(1, 101):
    if sayi % 3 == 0:
        print(sayi, end=" ")
        bulunan += 1
        if bulunan == 5:
            break
print()

# ------------------------------------------------------------------
# ALIŞTIRMA 10
# 1-10 arası çarpım tablosunu (10x10) yazdır. İç içe döngü kullan.
# ------------------------------------------------------------------
print("\n--- Alıştırma 10: 10x10 çarpım tablosu ---")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:4}", end="")      # :4 -> 4 karakterlik hizalama
    print()

# ------------------------------------------------------------------
# ALIŞTIRMA 11 (BONUS)
# Girilen bir metindeki sesli harf sayısını bul (for + koşul).
# ------------------------------------------------------------------
print("\n--- Alıştırma 11: sesli harf sayısı ---")
metin = "Merhaba Dünya, Python öğreniyorum"
sesli_harfler = "aeıioöuüAEIİOÖUÜ"
adet = 0
for harf in metin:
    if harf in sesli_harfler:
        adet += 1
print(f"'{metin}' içinde {adet} sesli harf var.")

# ------------------------------------------------------------------
# ALIŞTIRMA 12 (BONUS)
# while True + break ile basit bir menü yaz:
#   1) Topla  2) Çıkar  3) Çıkış
# Seçimleri bir listeden alarak dene: secimler = ["1", "2", "3"]
# ------------------------------------------------------------------
print("\n--- Alıştırma 12: while True + menü ---")
secimler = ["1", "2", "3"]
sira = 0
while True:
    if sira >= len(secimler):
        break
    secim = secimler[sira]
    sira += 1

    if secim == "1":
        print("Toplama seçildi: 10 + 5 =", 10 + 5)
    elif secim == "2":
        print("Çıkarma seçildi: 10 - 5 =", 10 - 5)
    elif secim == "3":
        print("Çıkış yapılıyor...")
        break                          # döngüyü bitir
    else:
        print("Geçersiz seçim:", secim)

print("\nTüm örnekler ve alıştırmalar bitti. Şimdi sıra sende:"
      " değerleri değiştirip çıktıların nasıl değiştiğini gözlemle.")




a = int(input("bir sayı giriniz.  :"))
b = int(input("bir sayı giriniz.  :"))
c = int(input("bir sayı giriniz.  :"))
if a>b:
    if a>c:
        if b>c:
            print(f"{a} > {b} > {c}")
        else :
            print(f"{a} > {c} > {b}")
    else:
        print(f"{c} > {a} > {b}")
else:
    if b>c:
        if a>c:
            print(f"{b} > {a} > {c}")
        else:
            print(f"{b} > {c} > {a}")
    else:
        print(f"{c} > {b} > {a}")