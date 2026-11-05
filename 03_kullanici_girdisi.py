# 03 - Kullanıcıdan Bilgi Alma (input)
# Öğreneceklerin: input(), tip dönüşümü (int / float / str), basit hesap
#
# Çalıştırmak için:  python3 03_kullanici_girdisi.py
# Not: Program sen yazana kadar bekler. Terminale cevap yazıp Enter'a bas.

# input() her zaman METİN (str) döndürür. Bu çok önemli!
isim = input("Adın ne? ")
print(f"Merhaba {isim}!")

# Sayı gerekiyorsa dönüştürmelisin
yas_metin = input("Kaç yaşındasın? ")
print("Dönüştürmeden önce tip:", type(yas_metin))

yas = int(yas_metin)          # metni tam sayıya çevir
print("Dönüştürdükten sonra tip:", type(yas))
print(f"10 yıl sonra {yas + 10} yaşında olacaksın.")

# Kısa yol: input'u doğrudan int() içine al
# yas = int(input("Kaç yaşındasın? "))

# Ondalıklı sayı için float()
boy = float(input("Boyun kaç metre? (örn: 1.78) "))
print(f"Boyun {boy} metre.")

# Basit bir hesap makinesi
sayi1 = float(input("Birinci sayı: "))
sayi2 = float(input("İkinci sayı: "))
print(f"Toplam: {sayi1 + sayi2}")
print(f"Fark:   {sayi1 - sayi2}")
print(f"Çarpım: {sayi1 * sayi2}")

# Bölmede sıfıra dikkat: 0'a bölmek hata verir.
# Bunu 11. dosyada try/except ile güvenli hale getireceğiz.
if sayi2 != 0:
    print(f"Bölüm:  {sayi1 / sayi2}")
else:
    print("İkinci sayı 0 olduğu için bölme yapılamaz.")

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) Kullanıcıdan ad ve soyad al, "Merhaba Ad Soyad" yazdır.
# 2) Kullanıcıdan doğum yılını int olarak al, yaşını hesapla ve yazdır.
# 3) Kullanıcıdan bir ürün fiyatı ve adet al; toplam tutarı yazdır.
# 4) Kullanıcıdan 3 not al (int), ortalamasını ondalıklı olarak yazdır.
# 5) Kullanıcıdan bir kelime al, kelimeyi 3 kez yan yana yazdır.
#    (İpucu: kelime * 3)


name = input("please enter your name:")
lastname = input("please enter your last name:")
print(f"Hello {name} {lastname}")
birth_year=int(input("please enter your birth year:"))
age=2026-birth_year
print(f"your age is {age}")
price=float(input("please enter the price of the product:"))
amount=int(input("please enter the amount of the product:"))
total=price*amount
print(f"the total amount is {total}")
note1=int(input("please enter the first note:"))
note2=int(input("please enter the second note:"))
note3=int(input("please enter the third note:"))
average=(note1+note2+note3)/3
print(f"the average of the notes is {average}")
word=input("please enter a word:")
print(word*3)