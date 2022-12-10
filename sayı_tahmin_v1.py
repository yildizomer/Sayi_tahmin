import random
import time 

print("""***********************

Sayı Tahmin Oyunu.

GitHub: o1geliyo

1 ile 50 arasında bir sayı.

Tahmin Hakkınız: 8
***********************""")

rastgele_sayı = random.randint(1,50)
tahmin_hakkı = 8

while True:
    tahmin = int(input("Tahmininiz:"))
    if (tahmin >= 51):
        print("Sayı 1 veya 50 arasında olmalıdır!!")
        tahmin_hakkı += 1
    if (tahmin < rastgele_sayı):
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin...")
        tahmin_hakkı -= 1
    elif (tahmin > rastgele_sayı):
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Daha düşük bir sayı söyleyin...")
        tahmin_hakkı -= 1
    else:
        print("Bilgiler Sorgulanıyor..")
        time.sleep(1)
        print("Tebrikler", rastgele_sayı)
        break
    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti..")
        print("Sayımız:",rastgele_sayı)
        break
    
        