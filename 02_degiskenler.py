# 02 - Değişkenler ve Veri Tipleri
# Öğreneceklerin: değişken tanımlama, int / float / str / bool, type(), f-string
#
# Çalıştırmak için:  python3 02_degiskenler.py

# Değişken = bir değere taktığın isim (etiket).
# Python'da tip belirtmen gerekmez, değerden anlar.
isim = "Ali"
yas = 20
boy = 1.78
ogrenci_mi = True

print(isim)
print(yas)
print(boy)
print(ogrenci_mi)

# type() bir değerin tipini söyler
print(type(isim))        # <class 'str'>   -> metin
print(type(yas))         # <class 'int'>   -> tam sayı
print(type(boy))         # <class 'float'> -> ondalıklı sayı
print(type(ogrenci_mi))  # <class 'bool'>  -> True / False

# Değişkenin değeri sonradan değiştirilebilir
yas = 21
print("Yeni yaş:", yas)

# Aynı satırda birden fazla değişken
a, b, c = 1, 2, 3
print(a, b, c)

# Takas (swap) — diğer dillerde geçici değişken gerekir, Python'da gerekmez
a, b = b, a
print("Takas sonrası:", a, b)

# İsimlendirme kuralları:
# - harf veya _ ile başlar, sayı ile başlayamaz
# - boşluk içeremez, Türkçe karakter kullanmamak daha güvenlidir
# - büyük/küçük harfe duyarlıdır: yas != Yas
# - okunabilirlik için snake_case tercih edilir: toplam_fiyat

# f-string: metnin içine değişken gömmenin en kolay yolu
print(f"Benim adım {isim}, {yas} yaşındayım ve boyum {boy} metre.")

# f-string içinde işlem de yapabilirsin
print(f"Gelecek yıl {yas + 1} yaşında olacağım.")

# Ondalık basamak sayısını ayarlama
print(f"Boy: {boy:.1f} m")   # 1 ondalık basamak

# Metin birleştirme (dikkat: metin + sayı hata verir)
print("Ad: " + isim)          # ikisi de metin -> sorun yok
# print("Yaş: " + yas)        # HATA! str + int olmaz
print("Yaş: " + str(yas))     # str() ile metne çevirince olur

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) Kendi adın, şehrin ve doğum yılın için üç değişken oluştur.
#    Hepsini tek bir f-string ile yazdır.
# 2) doğum yılından yaşını hesaplayan bir değişken yaz (2026 - dogum_yili).
# 3) Bir ürünün fiyatı (float) ve adedi (int) için değişken oluştur,
#    toplam tutarı f-string ile "Toplam: 125.5 TL" biçiminde yazdır.
# 4) x = 10, y = 3 tanımla; x/y sonucunu 2 ondalık basamakla yazdır.


name = "ali"
city = "istanbul"
birth_year = 2000
print(f"Benim adım {name}, {city} şehrinde yaşıyorum ve {birth_year} doğumluyum.")
age = 2026 - birth_year


price = 5.60
amount = 5
total = price * amount
print(f"Toplam: {total} TL")

x = 10
y = 3
result = x / y
print(f"x / y = {result:.2f}")
