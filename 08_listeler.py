# 08 - Listeler
# Öğreneceklerin: liste oluşturma, index, append, remove, sort, dilimleme,
#                 list comprehension, kopyalama tuzağı
#
# Çalıştırmak için:  python3 08_listeler.py

# Liste: sıralı, değiştirilebilir, tekrara izin verir
meyveler = ["elma", "armut", "kiraz"]
print(meyveler)
print("Uzunluk:", len(meyveler))

# Erişim
print("İlk:", meyveler[0])
print("Son:", meyveler[-1])

# Dilimleme
print("İlk iki:", meyveler[0:2])
print("Ters:", meyveler[::-1])

# Ekleme
meyveler.append("muz")            # sona ekle
print("append:", meyveler)

meyveler.insert(1, "çilek")       # belirtilen index'e ekle
print("insert:", meyveler)

# Silme
meyveler.remove("armut")          # değere göre sil (yoksa hata verir)
print("remove:", meyveler)

silinen = meyveler.pop()          # son elemanı çıkar ve döndür
print("pop:", silinen, "->", meyveler)

silinen = meyveler.pop(0)         # index'e göre çıkar
print("pop(0):", silinen, "->", meyveler)

# del ile index silme
sayilar = [10, 20, 30, 40]
del sayilar[1]
print("del:", sayilar)

# Değiştirme
sayilar[0] = 99
print("değiştir:", sayilar)

# Arama
print("20 var mı?", 20 in sayilar)
print("index(30):", sayilar.index(30))

# Sıralama
puanlar = [85, 42, 92, 78, 60]
puanlar.sort()                    # kalıcı, küçükten büyüğe
print("sort:", puanlar)

puanlar.sort(reverse=True)
print("sort(reverse):", puanlar)

# sorted(): orijinali bozmaz, yeni liste döner
orijinal = [3, 1, 2]
yeni = sorted(orijinal)
print("orijinal:", orijinal, " yeni:", yeni)

# Ters çevirme
orijinal.reverse()
print("reverse:", orijinal)

# Birleştirme
a = [1, 2]
b = [3, 4]
print("a + b:", a + b)
a.extend(b)                       # a'yı yerinde büyütür
print("extend:", a)

# Tekrarlama
print("[0] * 5:", [0] * 5)

# İstatistikler
notlar = [70, 85, 90, 60, 100]
print("min:", min(notlar))
print("max:", max(notlar))
print("sum:", sum(notlar))
print("ortalama:", sum(notlar) / len(notlar))

# List comprehension: kısa ve güçlü liste üretimi
kareler = [x ** 2 for x in range(1, 6)]
print("kareler:", kareler)

ciftler = [x for x in range(10) if x % 2 == 0]
print("çiftler:", ciftler)

# Koşullu dönüşüm
etiketler = ["büyük" if x > 50 else "küçük" for x in [10, 60, 30, 80]]
print("etiketler:", etiketler)

# İç içe liste (matris)
matris = [
    [1, 2, 3],
    [4, 5, 6],
]
print("matris[1][2]:", matris[1][2])

# ÖNEMLİ TUZAK: = ile kopyalama aynı listeyi paylaşır
liste1 = [1, 2, 3]
liste2 = liste1          # kopya DEĞİL, aynı liste
liste2.append(4)
print("liste1:", liste1)  # [1, 2, 3, 4] -> ikisi de değişti!

# Gerçek kopya
liste3 = liste1.copy()   # veya liste1[:] veya list(liste1)
liste3.append(5)
print("liste1:", liste1)
print("liste3:", liste3)

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) 5 sayıdan oluşan bir liste oluştur; en büyük, en küçük ve
#    ortalamasını yazdır.
# 2) Kullanıcıdan 5 sayı alıp listeye ekle, sonra sıralı yazdır.
# 3) Bir listedeki tekrar eden elemanları temizle. (İpucu: set() veya
#    yeni liste + "in" kontrolü)
# 4) 1-20 arası sayılardan 3'e bölünenlerin karelerini list comprehension
#    ile üret.
# 5) Bir alışveriş listesi oluştur; eleman ekle, sil, hepsini yazdır.
# 6) İki listeyi zip ile birleştirip "isim - not" biçiminde yazdır.

#alıştırma 1 
list= [x for x in range(1,6)]
print(list)
print(f"min -> {min(list)}")
print(f"max -> {max(list)}")
print(f"ortalaması -> {sum(list) / len(list)}")


#alıştırma 2
sayilar =[]
for i in range (1,6):
    deger = int((input(f"{i}. sayıyı giriniz.   :")))
    sayilar.append(deger)
print(sayilar)



#alıştırma 3
sayilar = [2,3,45,2,2,34,67,3,9]
unique = []
for sayi in sayilar:
    if sayi not in unique:
        unique.append(sayi)
print(unique)



#alıştırmalar 4
ucler = []
for i in range(1,21):
    if i % 3 == 0:
        ucler.append(i)
print(ucler)


#alıştırmalar 5
avlist =["muz" , "elma","tuvalet kağıdı","redbull","nutella"]
avlist.append("cips")
avlist.remove(avlist[1])
print(avlist)



#alıştırma 6 
list = [
    ["ali", "ahmet" , "mehmet"],
    [70,80,90] ,
    ]
for i in range(0, len(list)+1):
    print(list[0][i],list[1][i])