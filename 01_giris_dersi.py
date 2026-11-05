# 01 - Giriş dersi
# Öğreneceklerin: print(), yorum satırları, kaçış karakterleri
#
# Çalıştırmak için:  python3 01_merhaba_dunya.py

# Bu satır bir yorumdur. Python bu satırı görmezden gelir.
# Yorumlar, kodu kendine (veya başkasına) açıklamak içindir.

print("Merhaba Dünya!")
print("Python öğrenmeye başladım.")

# print() birden fazla değeri virgülle alabilir.
# Virgül koyduğunda Python araya otomatik boşluk ekler.
print("Adım", "Ali", "ve", "20", "yaşındayım")

# sep: değerler arasına ne konacağını belirler
print("2026", "10", "21", sep="-")

# end: satır sonuna ne konacağını belirler (varsayılan: yeni satır)
print("Bu satır bitmedi...", end=" ")
print("...devamı aynı satırda.")

# Kaçış karakterleri
print("Çift tırnak yazmak için: \"merhaba\"")
print("Ters bölü: \\")
print("Alt satıra geç:\nİkinci satır")
print("Araya tab (boşluk) koy:\tburada")

# Boş print() sadece bir boş satır bırakır
print()

# Metni üç tırnak ile çok satırlı yazabilirsin
print("""Bu yazı
birden fazla
satıra yayıldı.""")

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) Kendi adını ve yaşını tek bir print() ile yazdır.
# 2) sep=" -> " kullanarak "Python -> Kolay -> Eğlenceli" yazdır.
# 3) end=" " kullanarak 1'den 5'e kadar sayıları TEK satırda yazdır.
#    (İpucu: beş ayrı print() çağrısı kullan.)
# 4) Aşağıdaki çıktıyı tek bir print() ile üret:
#       Ürün: "Kalem"
#       Fiyat: 25 TL
#    (İpucu: \n ve \" kaçış karakterleri)


isim = "Ali"    
yas = 20    
print(f"Benim adım {isim}, {yas} yaşındayım.")

print("Python", "Kolay", "Eğlenceli", sep=" -> ")

print(1, end=" ")
print(2, end=" ")
print(3, end=" ")       
print(4, end=" ")
print(5)  
ürün = "Kalem"  
fiyat = 25
print(f'Ürün: "{ürün}"\nFiyat: {fiyat} TL')

