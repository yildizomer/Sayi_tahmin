import random
import time 

print("""****************************

 Sayı Tahmin Oyunu...

 Yapımcı: Ömer Faruk Yıldız.

 GitHub: o1geliyo

 Zorluk: Zor-Kolay


 Tahmin Hakkınız 10

****************************""")


time.sleep(0.5)
print("Kolay modda bulmanız gereken sayı 1 ile 50 arasındadır.")
time.sleep(0.5)
print("Zor modda bulmanız gereken sayı 1 ile 100 arasındadır.")
time.sleep(0.5)
tahmin = ()
rastgele_sayı = random.randint(1,100)
rastgele_sayı_kolay = random.randint(1,50)
tahmin_hakkı = 10
kolaylık = (input("Zorluk:"))

zorluk = kolaylık.capitalize()


kolaylık.capitalize()

while True:

    if zorluk == ("Zor"):
        tahmin = int(input("Tahmininiz:"))
        if (tahmin >= 101):
            print("Sayı 1 ve 100 arasında olmalıdır!!")
            tahmin_hakkı += 1
        if (tahmin < rastgele_sayı):
            print("Bilgiler Sorgulanıyor..")
            time.sleep(1)
            print("Daha yüksek bir sayı girin.")
            tahmin_hakkı -= 1
        elif (tahmin > rastgele_sayı):
            print("Bilgiler Sorgulanıyor..")
            time.sleep(1)
            print("Daha düşük bir sayı girin..")
            tahmin_hakkı -= 1
        elif (tahmin == rastgele_sayı):
            print("Bilgiler Sorgulanıyor..")
            time.sleep(1)
            print("Tebrikler", rastgele_sayı)
            break
        if (tahmin_hakkı == 0):
            print("Tahmin Hakkınız Bitti..")
            print("Sayımız:",rastgele_sayı)
            break



    elif zorluk == ("Kolay"):
        tahmin = int(input("Tahmininiz:"))
        if (tahmin >= 51):
            print("Sayı 1 ve 50 arasında olmalıdır!!")
            tahmin_hakkı += 1
        if (tahmin < rastgele_sayı_kolay):
            print("Bilgiler Sorgulanıyor..")
            time.sleep(1)
            print("Daha yüksek bir sayı girin.")
            tahmin_hakkı -= 1
        elif (tahmin > rastgele_sayı_kolay):
            print("Bilgiler Sorgulanıyor..")
            time.sleep(1)
            print("Daha düşük bir sayı girin.")
            tahmin_hakkı -= 1
        elif (tahmin == rastgele_sayı_kolay):
            print("Bilgiler Sorgulanıyor..")
            time.sleep(1)
            print("Tebrikler:", rastgele_sayı_kolay)
            break
        if (tahmin_hakkı == 0):
            print("Tahmin Hakkınız Bitti..")
            print("Sayımız:",rastgele_sayı_kolay)
            break
    else:
        print("Geçerli bir komut giriniz.")
        break
