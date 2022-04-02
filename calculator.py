# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:20:43 2022

@author: Furkan
"""
special_characters = list("/-=!@#$%^&*(),.;:")


islemler = ("Toplama (+)","Çıkarma (-)","Çarpma (x)","Bölme (/)")
girdi = int(input("""Hangi işlemi yapmak istiyorsunuz?
1) {}
2) {}
3) {}
4) {}
İşlem: """.format(islemler[0],islemler[1],islemler[2],islemler[3])))

if girdi < 5 and girdi > 0: # girilen sayı 1 ile 4 arasında mı kontrol edelim.
    print("""{} İşlemi Yapılacak! Hesaplama için lütfen "=" yazınız.
Lütfen özel karakter kullanmayınız.""".format(islemler[girdi-1]))
    if girdi == 1:  
        toplam = 0
        i=1
        girdi2=0  
        while True:
            girdi2=input("{}.Sayi = ".format(i))
            if girdi2 != "=":
                girdi2=int(girdi2)
                toplam+=girdi2
                i+=1
            elif girdi2 == "=":
                print("Toplam: {}".format(toplam))
                break
    if girdi == 2:
        pass #bu satırı silip kodunuzu buraya yazın
    if girdi == 3:
        pass #bu satırı silip kodunuzu buraya yazın
    if girdi == 4:
        pass #bu satırı silip kodunuzu buraya yazın    
else:
    print("Lütfen 1 ile 4 arasında bir sayı giriniz!")    
    
    
    