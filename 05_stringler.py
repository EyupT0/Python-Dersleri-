# 05 - String (Metin) İşlemleri
# Öğreneceklerin: len, upper/lower, strip, replace, split, join, dilimleme, in
#
# Çalıştırmak için:  python3 05_stringler.py

metin = "  Python Öğreniyorum  "

print("Orijinal :", repr(metin))
print("len()    :", len(metin))          # boşluklar dahil karakter sayısı

# Boşluk temizleme
print("strip()  :", repr(metin.strip()))     # iki taraftan
print("lstrip() :", repr(metin.lstrip()))    # soldan
print("rstrip() :", repr(metin.rstrip()))    # sağdan

temiz = metin.strip()

# Büyük / küçük harf
print("upper()  :", temiz.upper())
print("lower()  :", temiz.lower())
print("title()  :", temiz.title())
print("capitalize():", temiz.capitalize())

# Değiştirme
print("replace  :", temiz.replace("Öğreniyorum", "seviyorum"))

# Arama
print("find('Öğr') :", temiz.find("Öğr"))   # bulunamazsa -1
print("'Python' in temiz :", "Python" in temiz)   # True / False

# Sayma
print("count('o') :", temiz.count("o"))

# Metni parçalama -> liste döner
cumle = "elma, armut, kiraz"
parcalar = cumle.split(", ")
print("split()  :", parcalar)
print("tipi     :", type(parcalar))

kelimeler = "Python öğrenmek çok keyifli".split()
print("split() boşlukla:", kelimeler)

# Listeyi metne birleştirme
print("join()   :", " | ".join(parcalar))

# Dilimleme (slicing): metin[başlangıç:bitiş:adım]
s = "abcdefgh"
print("s        :", s)
print("s[0]     :", s[0])       # ilk karakter
print("s[-1]    :", s[-1])      # son karakter
print("s[0:3]   :", s[0:3])     # 0,1,2 (bitiş dahil değil)
print("s[:3]    :", s[:3])      # baştan 3 karakter
print("s[3:]    :", s[3:])      # 3'ten sona
print("s[::2]   :", s[::2])     # ikişer atlayarak
print("s[::-1]  :", s[::-1])    # ters çevir

# Metinler değiştirilemez (immutable)
# s[0] = "X"  -> HATA verir. Yeni metin oluşturmalısın:
s2 = "X" + s[1:]
print("s2       :", s2)

# Biçimlendirme
print("Ad: {:<10}|".format("Ali"))     # sola yasla
print("Ad: {:>10}|".format("Ali"))     # sağa yasla
print("Ad: {:^10}|".format("Ali"))     # ortala
print(f"Sayı: {42:05d}")               # 00042
print(f"Yüzde: {0.756:.1%}")           # 75.6%

# Faydalı kontroller
print("'123'.isdigit() :", "123".isdigit())
print("'abc'.isalpha() :", "abc".isalpha())
print("'   '.isspace() :", "   ".isspace())

# ------------------------------------------------------------------
# ALIŞTIRMALAR
# ------------------------------------------------------------------
# 1) Kullanıcıdan bir cümle al; kaç karakter olduğunu ve kaç kelime
#    olduğunu yazdır. (İpucu: len() ve split())
# 2) Kullanıcıdan bir kelime al, tersini yazdır. (İpucu: [::-1])
# 3) "  merhaba dünya  " metnini temizle, baş harflerini büyüt ve yazdır.
# 4) Bir e-posta adresi al; "@" işaretinden önceki kısmı yazdır.
#    (İpucu: split("@") veya find())
# 5) "a-b-c-d" metnini "-" ile parçala, sonra " > " ile birleştir.
# 6) Bir metindeki tüm boşlukları "_" ile değiştir.

print("\nALIŞTIRMALAR\n")

sentence = input("Bir Cümle Gİr    :")
print("cümlenin karakter sayısı : ", len(sentence))
print("cümlenin kelime sayısı : ", len(sentence.split()))

word = input("Bir kelime gir : ")
print("Kelimenin tersi : ", word[::-1])

word_ = "  merhaba dünya  "
print("temiz ve baş harfleri büyük" , word_.strip().title())

mail = input("Bir e-posta adresi gir : ")
mail_kok = mail.split("@")
print(f"mailin kökü : {mail_kok[0]}")

letters = "a-b-c-d-e-f-g"
split_letters = letters.split("-")
print("parçala ve birleştir : ", " > ".join(split_letters))


metin_ = "Bu bir örnek metindir"    
print("boşlukları _ ile değiştir : ", metin_.replace(" ", "_"))