# 04 - Sayılar ve Operatörler
# Öğreneceklerin: + - * / // % ** , round(), abs(), karşılaştırma operatörleri
#
# Çalıştırmak için:  python3 04_sayilar_ve_operatorler.py

a = 17
b = 5

print("a =", a, " b =", b)
print("Toplama      a + b  =", a + b)
print("Çıkarma      a - b  =", a - b)
print("Çarpma       a * b  =", a * b)

# Bölme her zaman float döndürür
print("Bölme        a / b  =", a / b)

# Tam bölme (kalanı atar, sonuç int)
print("Tam bölme    a // b =", a // b)

# Mod (kalan) — çok işine yarayacak
print("Kalan        a % b  =", a % b)

# Kuvvet
print("Kuvvet       a ** 2 =", a ** 2)
print("Karekök      9 ** 0.5 =", 9 ** 0.5)

# İşlem önceliği: parantez > kuvvet > çarpma/bölme > toplama/çıkarma
print("2 + 3 * 4   =", 2 + 3 * 4)      # 14
print("(2 + 3) * 4 =", (2 + 3) * 4)    # 20

# round(): yuvarlama
print("round(3.14159, 2) =", round(3.14159, 2))
print("round(2.5)        =", round(2.5))   # 2 (banker's rounding)
print("round(3.4)        =", round(3.4))   # 3

# abs(): mutlak değer
print("abs(-42) =", abs(-42))

# int() ondalık kısmı atar, yuvarlamaz
print("int(9.99) =", int(9.99))

# Karşılaştırma operatörleri -> sonuç her zaman True / False
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a == b :", a == b)   # eşit mi? (tek = atama, çift == karşılaştırma)
print("a != b :", a != b)   # eşit değil mi?
print("a >= 17:", a >= 17)

# Pratik: çift / tek sayı kontrolü **
sayi = 42
print(f"{sayi} çift mi? ->", sayi % 2 == 0)

# Pratik: bir sayının basamaklarını ayırma
# 17 // 5 = 3  -> bölüm
# 17 %  5 = 2  -> kalan
print(f"{a} sayısı {b}'e bölününce bölüm {a // b}, kalan {a % b}")

# Pratik: saniyeyi saat/dakika/saniyeye çevirme
toplam_saniye = 3725
saat = toplam_saniye // 3600
kalan = toplam_saniye % 3600
dakika = kalan // 60
saniye = kalan % 60
print(f"{toplam_saniye} saniye = {saat} saat {dakika} dakika {saniye} saniye")

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) Bir ürünün fiyatı 89.99, adedi 3. Toplamı hesapla ve 2 basamak yuvarla.
# 2) Kullanıcıdan bir sayı al; çift mi tek mi olduğunu % ile bul ve yazdır.
# 3) 1234 saniyeyi saat/dakika/saniye biçiminde yazdır.
# 4) Bir sayının karesini ve küpünü ** ile hesapla.
# 5) 7'nin 3'e bölümünde bölüm ve kalanı ayrı ayrı yazdır.
# 6) İki sayı al; büyük olanı karşılaştırma operatörü ile bul (if kullanmadan
#    sadece True/False yazdırmak yeterli).

print ("\nALIŞTIRMALAR\n")

price = 89.99
amount = 3
total=round(price * amount, 2)
print("Toplam fiyat:", total)

number = int(input("Bir sayı girin: "))
print(f"{number} çift mi -->", number % 2 == 0)

total_seconds = 1234
hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60
print(f"{total_seconds} saniye = {hours} saat {minutes} dakika {seconds} saniye")

input_number = int(input("Bir sayı girin: "))
square = input_number ** 2
cube = input_number ** 3    
print(f"{input_number} sayısının karesi: {square}, küpü: {cube}")

number_1 = 7
number_2 = 3
bolum = 7 // 3 
kalan = 7 % 3
print(f"7'nin 3'e bölümünde bölüm: {bolum}, kalan: {kalan}")

a = 92
b= 39
print(f"{a} > {b} -->", a > b) 
