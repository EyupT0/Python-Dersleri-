# 07 - Döngüler (for / while)
# Öğreneceklerin: for, range(), while, break, continue, else, iç içe döngü
#
# Çalıştırmak için:  python3 07_donguler.py

# for: bir koleksiyonun elemanları üzerinde gezer
for harf in "Python":
    print(harf)

print("---")

# range(bitiş) -> 0'dan başlar, bitiş dahil değil
for i in range(5):
    print(i, end=" ")
print()

# range(başlangıç, bitiş)
for i in range(1, 6):
    print(i, end=" ")
print()

# range(başlangıç, bitiş, adım)
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# Geriye sayma
for i in range(5, 0, -1):
    print(i, end=" ")
print("Başla!")

# Toplam hesaplama (klasik akümülatör deseni)
toplam = 0
for i in range(1, 101):
    toplam += i          # toplam = toplam + i
print("1..100 toplamı:", toplam)

# while: koşul doğru olduğu sürece döner
sayac = 0
while sayac < 5:
    print("Sayaç:", sayac)
    sayac += 1           # BU SATIR OLMASA SONSUZ DÖNGÜ OLUR

# break: döngüyü tamamen bitirir
for i in range(10):
    if i == 3:
        break
    print("break öncesi:", i)

# continue: o turu atlar, sonraki tura geçer
for i in range(6):
    if i % 2 == 0:
        continue
    print("tek sayı:", i)

# else: döngü break olmadan bittiyse çalışır
for i in range(3):
    print("tur", i)
else:
    print("Döngü normal bitti.")

# Sonsuz döngü + break (menü deseni)
# while True:
#     cevap = input("Çıkmak için q: ")
#     if cevap == "q":
#         break

# enumerate: hem index hem değer
meyveler = ["elma", "armut", "kiraz"]
for index, meyve in enumerate(meyveler, start=1):
    print(f"{index}. {meyve}")

# zip: iki listeyi paralel gez
isimler = ["Ali", "Ayşe", "Mehmet"]
notlar = [85, 92, 78]
for isim, notu in zip(isimler, notlar):
    print(f"{isim}: {notu}")

# İç içe döngü: çarpım tablosu
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="  ")
    print()   # her satırdan sonra alt satıra geç

# Yıldızlarla üçgen
for i in range(1, 6):
    print("*" * i)

# Ters üçgen
for i in range(5, 0, -1):
    print("*" * i)

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) 1'den 20'ye kadar sadece çift sayıları yazdır.
# 2) Kullanıcıdan bir sayı al; 1'den o sayıya kadar toplamı hesapla.
# 3) 1'den 10'a kadar sayıların karesini yazdır.
# 4) Bir kelime al; harflerini alt alta yazdır.
# 5) 5x5'lik bir kare yıldız deseni çiz.
# 6) Kullanıcı "q" yazana kadar sayı alıp toplamını tutan bir while döngüsü yaz.
# 7) 1-100 arası sayılardan 3'e ve 5'e tam bölünenleri yazdır.


print("ALIŞTIRMA 1")
for i in range(2,21,2):
    print(i)



print("ALIŞTIRMA 2")
sayi = int(input("bir sayi giriniz. :"))
toplam=0
for i in range(1,sayi + 1):
    toplam +=i
print(toplam)



print("ALIŞTIRMA 3")
gecici=0
for i in range(1,11):
    gecici= i**2
    print(gecici)


print( "Alıştırma 5")
for i in range(0,5):
    print("*" * 5)



print("Alıştırma 6")
toplam = 0
adet = 0
while True:                                 
    cevap = input("Sayı gir (çıkmak için q): ")
    if cevap.lower() == "q": 
        break
    toplam += int(cevap)     
    adet += 1
print(f"Girilen {adet} sayının toplamı: {toplam}")




