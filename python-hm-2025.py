#####################################
# Python Temelleri - Ödev Scripti
#####################################

# Soru 1:
# Bir integer, bir float ve bir complex sayı tanımlayın.
# Bu sayıların türlerini yazdırın ve aralarında 1-2 işlem yapın.

# Sayı tanımlamaları
sayi_int = 10
sayi_float = 3.14
sayi_complex = 2 + 5j

# Türleri yazdır
print(type(sayi_int))     # <class 'int'>
print(type(sayi_float))   # <class 'float'>
print(type(sayi_complex)) # <class 'complex'>

# İşlemler
toplam = sayi_int + sayi_float
print("Toplam:", toplam)

carpim = sayi_int * sayi_complex
print("Çarpım:", carpim)

# Soru 2:
# İsminizi içeren bir string değişkeni oluşturun.
# Bu stringin ilk ve son karakterini yazdırın. Ayrıca tüm harfleri büyük yaparak ekrana yazdırın.

isim = "Ahmet"

print("İlk harf:", isim[0])
print("Son harf:", isim[-1])
print("Büyük harflerle:", isim.upper())

# Soru 3:
# Aşağıdaki string içinde "veri" kelimesi geçiyor mu kontrol edin.
# Ardından bu stringi boşluklardan bölerek liste haline getirin.

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."

# "veri" kelimesi var mı? (case-insensitive)
print("veri" in sentence.lower())  # True veya False

# Boşluklardan bölme
kelimeler = sentence.split()
print(kelimeler)


# Soru 4:
# İçerisinde 3 farklı türde veri bulunan bir liste oluşturun.
# Listenin uzunluğunu, ilk ve son elemanını yazdırın.
# Ardından bu listeye yeni bir eleman ekleyin ve ikinci elemanı silin.

karisik_liste = [42, "Python", 3.14]

print("Uzunluk:", len(karisik_liste))
print("İlk eleman:", karisik_liste[0])
print("Son eleman:", karisik_liste[-1])

karisik_liste.append(True)         # Yeni eleman eklendi
del karisik_liste[1]               # İkinci eleman silindi (index 1)

print("Güncel liste:", karisik_liste)


# Soru 5:
# 2 parametre alan bir fonksiyon yazın. Bu fonksiyon, aldığı iki sayının ortalamasını dönsün.

def ortalama_hesapla(sayi1, sayi2):
    return (sayi1 + sayi2) / 2

print(ortalama_hesapla(10, 20))  # 15.0



# Soru 6:
# Kullanıcının yaşına göre mesaj yazdıran bir fonksiyon yazın:
# 18'den küçükse "Çok gençsin!", 18-40 arasıysa "Harika bir yaştasın!", 40'tan büyükse "Deneyim önemli!" mesajını yazdırsın.

def yas_mesaji(yas):
    if yas < 18:
        print("Çok gençsin!")
    elif yas <= 40:
        print("Harika bir yaştasın!")
    else:
        print("Deneyim önemli!")

yas_mesaji(25)  # Örnek kullanım


# Soru 7:
# İçerisinde sayılar olan bir liste içindeki sayıları dolaşarak 2 katını ekrana yazdırın (for döngüsü ile).
sayi_listesi = [1, 3, 5, 7, 9]

for sayi in sayi_listesi:
    print(sayi * 2)

# Soru 8:
# 1'den başlayarak 20 dahil olacak şekilde çift sayıları yazdırın (while döngüsü ile).
sayi = 1
while sayi <= 20:
    if sayi % 2 == 0:
        print(sayi)
    sayi += 1

# Soru 9:
# Bir çalışanın haftalık maaşını hesaplayan bir fonksiyon yazın.
# Saatlik ücreti ve haftalık toplam çalışma saati parametre olarak alınsın.
# Haftada 40 saatten fazla çalıştıysa, fazla saatler için %50 zamlı ücret ödensin (mesai).
# Örnek: 45 saat çalışan biri için 5 saatlik mesai uygulanmalı.

def haftalik_maas(saatlik_ucret, calisma_saati):
    if calisma_saati <= 40:
        return saatlik_ucret * calisma_saati
    else:
        normal_maas = saatlik_ucret * 40
        mesai_saati = calisma_saati - 40
        mesai_maas = mesai_saati * saatlik_ucret * 1.5
        return normal_maas + mesai_maas

print(haftalik_maas(100, 45))  # 4750 TL
