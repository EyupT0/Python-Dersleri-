# 06 - Koşullar (if / elif / else)
# Öğreneceklerin: if, elif, else, and, or, not, iç içe koşullar, truthy/falsy
#
# Çalıştırmak için:  python3 06_kosullar.py

# Girinti (indentation) Python'da zorunludur. Genelde 4 boşluk kullanılır.
# Girintili blok, koşul doğruysa çalışır.

yas = 20

if yas >= 18:
    print("Ehliyet alabilirsin.")
else:
    print("Henüz ehliyet alamazsın.")

# elif: birden fazla durum
not_degeri = 75

if not_degeri >= 90:
    harf = "AA"
elif not_degeri >= 80:
    harf = "BA"
elif not_degeri >= 70:
    harf = "BB"
elif not_degeri >= 60:
    harf = "CC"
else:
    harf = "FF"

print(f"Not: {not_degeri} -> Harf: {harf}")

# and: iki koşul da doğru olmalı
kullanici_adi = "ali"
sifre = "1234"

if kullanici_adi == "ali" and sifre == "1234":
    print("Giriş başarılı.")
else:
    print("Kullanıcı adı veya şifre hatalı.")

# or: en az biri doğru olmalı
gun = "cumartesi"
if gun == "cumartesi" or gun == "pazar":
    print("Hafta sonu!")

# not: tersine çevirir
acik_mi = False
if not acik_mi:
    print("Mağaza kapalı.")


# ben alterantif olarak bunu da yazabilirim
acik_mi = False
if acik_mi == False:
    print("Mağaza kapalı.")



# in: bir değer içinde var mı?
meyveler = ["elma", "armut", "kiraz"]
if "elma" in meyveler:
    print("Elma listede var.")

# Zincirleme karşılaştırma (Python'a özgü)
if 18 <= yas < 65:
    print("Çalışma yaşında.")

# İç içe koşullar
sayi = 0
if sayi >= 0:
    if sayi == 0:
        print("Sayı sıfır.")
    else:
        print("Sayı pozitif.")
else:
    print("Sayı negatif.")

# Truthy / Falsy: bazı değerler koşulda doğrudan False sayılır
# False, 0, 0.0, "", [], {}, None  -> falsy
# Diğer her şey -> truthy
isim = ""
if isim:
    print(f"Merhaba {isim}")
else:
    print("İsim boş!")

# Tek satırlık if (kısa kullanım)
durum = "reşit" if yas >= 18 else "reşit değil"
print("Durum:", durum)

# match / case (Python 3.10+) — çoklu eşleştirme
komut = "başlat"
match komut:
    case "başlat":
        print("Sistem başlatılıyor...")
    case "durdur":
        print("Sistem durduruluyor...")
    case _:
        print("Bilinmeyen komut.")

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) Kullanıcıdan bir sayı al; pozitif / negatif / sıfır olduğunu yazdır.
# 2) Kullanıcıdan yaş al; 0-12 çocuk, 13-17 genç, 18-64 yetişkin,
#    65+ yaşlı yazdır.
# 3) Kullanıcı adı ve şifre al; ikisi de doğruysa "Giriş başarılı" yazdır.
#    (Doğru değerleri kendin belirle.)
# 4) Bir yıl al; artık yıl mı? (4'e tam bölünür ve 100'e bölünmüyorsa
#    VEYA 400'e tam bölünüyorsa artık yıldır.)
# 5) Bir sayı al; 1-100 arasında mı kontrol et (and ile).
# 6) Bir harf al; sesli harf mi (a,e,i,o,u) kontrol et (in ile).

print("ALIŞTIRMALAR")

#1
sayi = int(input("Bir sayı giriniz:  "))
if sayi >= 0:
    if sayi == 0: 
        print("Sayı sıfıra eşittir")
    else:
        print("Sayı pozitiftir")
else:
    print("Sayı negatiftir")

#2
yas = int(input("Yaşınızı giriniz:  "))
if 0<= yas <= 12:
    print("Çocuk")
elif 13<= yas <= 17:
    print("Genç")
elif 18<= yas <= 64:
    print("Yetişkin")
else:
    print("Yaşlı")

#3
kullanici_adi = input("Kullanıcı adınızı giriniz:  ")
sifre = input("Şifrenizi giriniz:  ")
if kullanici_adi == "admin" and sifre == "1234":
    print("Giriş başarılı")
else:
    print("Kullanıcı adı veya şifre hatalı")

#4
yil = int(input("Bir yıl giriniz:  "))
if yil % 4 == 0 and yil % 100 != 0 or yil % 400 == 0:
    print(f"{yil} bir artık yıldır.")
else:
    print(f"{yil} bir artık yıl değildir.")


#5
sayi = int(input("Bir sayı giriniz:  "))
if sayi >= 1 and sayi <= 100:
    print("Sayı 1-100 arasındadır.")
else:
    print("Sayı 1-100 arasında değildir.")

#6
sesli_harfler = ["a", "e", "i", "o", "u", "ı", "ö", "ü", "A", "E", "İ", "O", "U", "I", "Ö", "Ü"]
harf = input("Bir harf giriniz:  ")
if harf in sesli_harfler:
    print(f"{harf} bir sesli harftir.")
else:
    print(f"{harf} bir sesli harf değildir.")