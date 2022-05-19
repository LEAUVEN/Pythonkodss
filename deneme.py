#print('HELLO WORLD!')
#print("a" * 3)
#name = 'Mert ARAS'
#type(name) str
#type(3) int
#type(34.2) float
#A= 1
#B= 3
#D=6 
#B=61
#print(A+B)
#print(type(A*B/D))
#a='Hayatımızın bir önemi olduğunu düşünen insanların kendi sorunlarına bakamıyor oluşunun trajedisi'
#len(a)
#------------------ # --------------------BİR KAÇ METHOD------------- # -------------------
#a='hayatımızın bir önemi olduğunu düşünen insanların kendi sorunlarına bakamıyor oluşunun trajedisi ' 
#a.upper() içeriği büyütmeye yarıyor
#a.lower() içeriği küçültmeye yarıyor
#a.islower() içeriğin hepsi küçük mü diye soruyor
#a.isupper() içeriğin hepsi büyük mü diye soruyor
#a.replace('a','7') içeriğin içindeki tüm a harflerini 7 ile değiştiriyor
#B=a.upper() Burda içeriği hem büyütüyor hemde bunu bir string olarak atıyıp kullanılabilir bir hale getiriyor.
#print(B)
#a.title() Hepsinin baş harflerini büyütür
#a.capitalize()  Sadece baş harfi büyütür
#len(a) toplam kaç karakterden oluştuğunu söylüyor
#dir(a)  Uygulanabilir methodlara bakma 
#------------------ # -------------------- # Strip methodu ve kullanımı #------------------ # --------------------
#string = '  xoxo love xoxo   '

#print(string.strip()) sadece baştaki boşluklar için

#print(string.strip(' xol')) baştaki boşluk x o ve l için

#print(string.strip('stx')) başta boşluk yok o yüzden uygulanamadı

#string = 'android is awesome'
#print(string.strip('an')) başta boşluk olmadığı için an ile başlayan kısmı sildi.
#a='hayatımızın bir önemi olduğunu düşünen insanların kendi sorunlarına bakamıyor oluşunun trajedisi '
#a[7] bu a için 7.karakteri gösteriyor.(0 dan başlar h harfi 0 a harfi 1 dir.)
#a[0:15] bu a için 0 dan 15 e kadar karakterleri gösteriyor.
#a=1
#b=64
#c=a*7
#d=b/8
#e=b**3
#print(c)
#print(d)
#birinci_sayı=input()
#ikinci_sayı=input()
#print(type(birinci_sayı)) 
#a=int(birinci_sayı)*int(ikinci_sayı) int ile str olan birinci_sayı olan değeri int e çevirmemiz gerekiyor ki işlem yapabilelim.
#print(a)
#[] #------------------ # ----------------------------------lİSTELER #------------------ # --------------------------------------
#                                          -Değiştirilebilir,Sıralı,Kapsayıcı
#liste=[7,'ayhan',9,'mert',6.54,2] 
#liste_2=[13,liste,777]
#print(liste)
#print(liste_2)
#                                                                                                                                          Liste arasından seçim yapma
#liste_0=[7,'ayhan',9,'mert',6.54,2]
#liste_1=[13,liste,777]
#liste_2=[liste_0,liste_1]
#print(liste_2)
#liste_0[:3]                                                                                                             liste_0 için 0 dan 3 e kadar olan birimleri listele
#liste_2[1][3]                                                   liste_2 için 1.birimin 3.birimini göster. 2 listenin birleştiği yerlerde kullanılır çünkü [] ile listeler arasında seçim yaplabilinir
#print(7 in liste_0)  veya (not 7 in liste_0)                                    #listede 7 sayısı var mı diye sorar evet iste true der hayırsa false veya 7 elamanı değil midir diye soruyor elemensa false
#liste=[7,'ayhan',9,'mert',6.54,2]
#liste[0:3] = 'Mert', 19,79,'aras'                                                                                     Listenin 0dan 3 e kadar olan elemanlarını değiştirdim.
#liste_0=[7,'ayhan',9,'mert',6.54,2] 
#liste_0= liste_0 + ['KEMAL2']                                                                                                             LİSTEYE ELEMAN EKLEME
#del liste_0[0:2]                                                                                                                          LİSTEDEN ELEMAN SİLME
#print(liste_0)
#liste_0=[7,'ayhan',9,'mert',6.54,2,9] 
#liste_0.insert(0,'Deneme')                                                                                             #.insert methodu (kaçıncı basamaktaki ürün, yerine koyacağınız şey.)
#len(liste_0)
#liste_0.insert(len(liste_0),'kısayol')                                                 #listenin kaç elemanlı olduğunu gösteren len fonksiyonu ile listenin sonuncu elemanından sonraya ekleme yaptık
#liste.pop() # .pop(kaçıncı eleman istiyorsan) listenin içinden birşey silmek için gerekli fonksiyon
#max(list_0) veya min(liste_0)                                                          # max ile en yüksek değerli elemeanı min ile en düşük elemanı söyler
#liste_0.count(9)                                                                       # .count(aranan eleman) listenin içindeki o elemandan kaç adet olduğunu söyler.Frekans söyler.
#liste_yedek=liste.copy()                                                               #.copy methodu ile bir şeyi yedeklemek istediğimizde.
#liste_0.extend(['a','b','cevahir'])                                                    #.extend([]) methodu ile istenilen listeye birşeyler ekleme veya liste ekleme
#liste_1=['LİSTE 2']
#liste_0.extend(liste_1)                                                                #.extend fonksiyonu için birim ekleme olabileceği gibi aynı zamanda yeni bir liste eklenebilir.
#liste_0.index('mert')                                                                  #.index() fonksiyonu ile aradığımız şeyin kaçıncı sırada olduğunu öğrenebiliriz.
#liste_0.reverse()                                                                      #.reverse() ile bir listeyi terse çevirebiliriz.
#liste_6=[1,6,93,977,862123,1234.7]
#liste_6.sort()                                                                          #.sort() methodu listeyi sıralar değerlerine göre.
#liste_0.clear()                                                                         #.clear() ile liste temizlenir.

#-Öğrencinin ders sonu notu ve başarı durumu hesaplama
#liste=[input(),input(),input()]
#sınav_1=int(liste[1])
#sınav_2=int(liste[0])
#sınav_3=int(liste[2])
#ortalama=(sınav_1+sınav_2+sınav_3)/3
#print(ortalama)
#print((sınav_1+sınav_2+sınav_3)/3)
#geçme_notu=60
#if ortalama > geçme_notu:
    #    print('Öğrenci bu dersten başarılıdır.')
#else:
#    print('Öğrenci bu dersten başarısızdır.')


#---------------------------- # -----------------------------# TUPLE #---------------------------- # -----------------------------#
    
                              #kapsayıcıdır,sıralıdır ve değiştirilemez. Değiştirilememesi listeden farklılaştırır onu.
#t = ('ilk tuple',)                                    # tuple oluştururken tek birimlik olucak ise sonuna , koyulmalı
#t = ('ali','veli','özge',9,81,999,[159115])

#---------------------------- # -----------------------------# Sözlük #---------------------------- # -----------------------------#
#                                                      DEĞİŞTİRİLEBİLİR SIRASIZ VE KAPSAYICI 
#sözlük = {'Class' : 'Sınıf',        #sözlük için birşeyler atama 'class' kelimesi için : kullanarak bir değer atadık.
#          'fifth' : ' 15',
#         'okulun bitme ihtimali' : ['Muhtemelen',' %0']}  #bir değer için 1 den fazla şey atanabilir
#sözlük['Class']                                   #ile istediğimiz birim için atanan değeri alabiliriz.

#sözlük_1 = {'ÖĞRETİCİ' : {'DBE' : ' HAZIRLIK',   # SÖZLÜK İÇİNE BİR SÖZLÜK DAHA EKLENEBİLİR.
#                         'Gelecek' : 'Kötü',
#                          'Hayat' : 'Çok Zor'},
#            'LOL' : 'Oynama',
#            'Para' :     {'Dolar' : 'Bitti',
#                         'BNB'   : 'Umarım yükselir.',
#                         'Altın' : 'Hiç olmadı'}}
#Sözlük_1['Para']['BNB']                          # BİR SÖZLÜK İÇİNDEN BİRİM SEÇME 
#sözlük_1['Ekleme'] = 'Bu method ile olur'        # Sözlük[] ile birim seçilir ve değer atanır. 
#sözlük_1['LOL']='Yeni Yama'                      # Seçilen birim yoksa direk sözlüğe eklenir, eğer varsa değiştirilir.
#t= ( "Tuple kullanarak",),                       #Sözlüğe birşey eklerken ilk başta verilen değer değiştirilemeyeceği için tuple kullanılmalı.
#sözlük_1[t]= 'sözlüğe birşey ekleme'             #Burda 'tuple kullanarak' kısmı sabit kalırken 'sözlüğe birşey ekleme' kısmı için birşeyler atanabilir.

#---------------------------- # -----------------------------# SETLER #---------------------------- # -----------------------------# 
                             # 1-) Belli bir sırası yoktur. 2-) Değerleri eşsizdir. 3-) Değerleri değiştirilebilir. 4-) Farklı tip barındırabilir.

        
#l=[1,'41','BeterAli',19.7]
#b=set(l)
#print(b)
#fruits = {"banana", "grape", "cherry"}
#print("banana" in fruits) # True                                  # in kullanarak banana bu setin elemanı mı diye sorguladık.
# = {"banana", "grape", "cherry"}
#print(fruits)  # {"grape", "banana", "cherry"}
#for fruit in fruits:                                              # for set_adı in set_adı : ile setin elemanlarına ulaşabiliriz.
    #print(fruit)                                                  #burdan sonra enter yapıp bir alt satırda boşluk bırakmak lazım.
#fruits.add("orange")                                              #.add() fonksiyonu ile set içine yalnızca -1- eleman eklenebilir.
#fruits.update(['blueberry','mango'])                              #.update([,]) fonksiyonu ile bir den fazla eleman eklenebilir.
#fruits.remove("grape")  or  fruits.discard("grape")               #.remove() fonksiyonu ile veya .discord() foknsiyonu ile setten eleman silinebilir.
#fruits.pop()                                                      #.pop fonksiyonun son elemanını siler ama fonksiyon sıralı değil o yüzden random.
#fruits.clear()                                                    #.clear() fonksiyonu ile tüm set silinir.
#kilo_sayıları = {6,9,7}
#genel_kasa =fruits.union(kilo_sayıları)                            #.union() fonksiyonu ile 2 set birleştirilir ve yeni bir set oluşturulur
#fruits.update(kilo_sayıları)                                       #.update() fonksiyonu ile bir seti diğerinin içine ekleriz.
#print(fruits)                                                      #{'cherry', 'banana', 6, 7, 9, 'grape'}
#print(genel_kasa)                                                  #{'cherry', 'banana', 6, 7, 9, 'grape'}
#fruits_1 = {'banana', 'apple', 'cherry'}                           #.difference() fonksiyonu ile 2 set farkına bakılır
#fruits.difference(fruits_1)                                        #fruits ile fruits_1 kıyaslanır ve farklı olan fruits elemanları sıralanır.
#fruits_1.difference(fruits)                                        #fruits_1 ile fruits kıyaslanır ve farklı olan fruits_1 elamanları sıralanır.
#fruits.isdisjoint(fruits_1)                                        #.isdisjoint() keşisim boş mu diye soruyor. 
#fruits.issubset(fruits_1)                                          #.issubset() ile bir küme diğerinin alt kümesi mi diye soruyor.
#fruits.issuperset(fruits_1)                                        #.issuperset() ile bir küme diğerinin kapsıyor mu diye soruyoruz.

#---------------------------- # -----------------------------# BMI KODU #---------------------------- # -----------------------------# 
#height = float(input("Enter your height in cm: "))
#weight = float(input("Enter your weight in kg: "))
#BMI = weight / (height/100)**2
#BMI_2=round(BMI)                                       #round() ile BMI için çıkan değeri yuvarladık.
#print(f"You BMI is {BMI_2}")
#if BMI_2 <= 18.4:                                      # if ile başladığımız kod else ile biter ama aradaki 
#    print("You are underweight.")                      # değerler için  else ve if toplamı olan elif kullanılır
#elif BMI_2 <= 24.9:
#    print("You are normal weight")
#elif BMI_2 <= 29.9:
#    print("You are over weight.")
#else:
#    print("You are obese.")
#---------------------------- # -----------------------------#  Def ile çabalamalar #---------------------------- # -----------------------------# 
#def carpma(x,y):
#    print('Çarpılan sayılar sırasıyla '+ str(x) + ' ve ' + str(y) +' Çarpımları: ' + str(x*y))
#carpma(9,7)
#                                              DEF İLE BİRŞEY TANIMLAYIP KULLANICAKSAK İNPUTTA PRİNT İLE KULLANILIR
#def hesaplamam(isi,nem,sarj,gider):
#    print((isi+nem)/sarj*gider)
#hesaplamam(float(input()),float(input()),float(input()),float(input()))

#                                DEF İLE TANIMLANAN ŞEYDEN GELECEK HESAPLAMAYI(BURDA HESAPLAMAM SONUCUNDA ÇIKACAK OLAN DEĞERİ)KULLANMAK İÇİN BÖYLE YAPILIR
#def hesaplamam(isi,nem,sarj,gider):
#    return((isi+nem)*sarj*gider)
#deger = hesaplamam(float(input()),float(input()),float(input()),float(input()))**0.5
#if deger >= 1000 :
#    print('Sistem düzgün çalışıyor')
#else :
#    print('Sisteminiz düzgün çalışmamaktadır.')
                                #            DEF İLE SADECE TANIM İÇİNE DEĞİL DIŞINA(GLOBAL'E) ETKİ EDİLEBİLİNİR.
                                #        BURDA PYTHON ÖNCELİKLE X ARIYOR DEF İÇİNDE BULAMAYINCA DIŞARI BAKIYOR BAKTI X İ BULDU APPEND İLE Y ELEMANINI EKLEDİ
#x=[]
#def eleman_ekle(y):
#    x.append(y)
#    print(str(y) + " ifadesi x listesine eklemiştir.")  
#eleman_ekle(7)
#print(x)



#---------------------------- # -----------------------------#  HESAP MAKİNESİ #---------------------------- # -----------------------------#  
# Toplama Fonksiyonu
#def Topla(x, y):
#   return x + y
 
# Çıkarma Fonksiyonu
#def Cikar(x, y):
#   return x - y
 
# Çarpma Fonksiiyonu
#def Carp(x, y):
#   return x * y
 
# Bölme Fonksiyonu
#def Bol(x, y):
#   return x / y
 
#print("Yapılacak İşlemi Seçin.")
#print("=======================")
#print("1.Toplama")
#print("2.Çıkarma")
#print("3.Çarpma")
#print("4.Bölme")
 
# Kullanıcıdan Seçim İsteme
#secim = input("Seçiminiz (1/2/3/4):")
 
#sayi1 = int(input("1. Sayı: "))
#sayi2 = int(input("2. Sayı: "))
 
#if secim == '1':
#   print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2))
 
#elif secim == '2':
#   print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2))
 
#elif secim == '3':
#   print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2))
 
#elif secim == '4':
#   print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
#else:
#   print("Geçersiz Giriş")
#---------------------------- # -----------------------------#  RANDOM SİFRE YARATICI #---------------------------- # -----------------------------#  
#import random
#Chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
 
#password_len = int(input("Şifre kaç karakterden oluşturulsun : "))
#password_count = int(input("Kaç adet şifre oluşturulsun : "))
#for x in range(0, password_count):
#        password = ""
#        for x in range(0, password_len):
#            password_char = random.choice(Chars)
#            password      = password + password_char
#        print("Random Şifreniz : " , password)
#---------------------------- # -----------------------------#  TAKVİM #---------------------------- # -----------------------------#  
#import calendar
#yil = int(input("Yıl Gir : "))
#ay = int(input("Ay Gir : "))
#print(calendar.month(yil, ay))
#---------------------------- # -----------------------------# ASAL SAYI TESTER #---------------------------- # -----------------------------# 
#sayac=0
#sayi=input('Sayı: ')
#for i in range(2,int(sayi)):
#      if(int(sayi)%i==0):
#            sayac+=1
#            break
#if(sayac!=0):
#      print("Sayı Asal Değil")
#else:
#      print("Sayı Asal")#
#---------------------------- # -----------------------------# SAYI TAHMİN OYUNU #---------------------------- # -----------------------------# 
#from random import randint
 
#rand=randint(1, 100)
#sayac=0
 
#while True:
#    sayac+=1
#    sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
#    if(sayi==0):
#        print("Oyunu İptal Ettiniz")
#        break
#    elif sayi < rand:
#        print("Daha Yüksek Bir Sayı Girin.")
#        continue
#    elif sayi > rand:
#        print("Daha Düşük Bir Sayı Girin.")
#        continue
#    else:
#        print("Rastele seçilen sayı {0}!".format(rand))
#        print("Tahmin sayınız {0}".format(sayac))

#---------------------------- # -----------------------------#  SAAT #---------------------------- # -----------------------------# 
#import datetime
#import time

#class Saat():

#	def __init__(self):
#		self.zamanAl()	
#		
#	def zamanAl(self):
#		zaman = datetime.datetime.now()
#		
#		self.yil = zaman.year
#		self.ay = zaman.month	
#		self.gun = zaman.day
#		self.saat = zaman.hour
#		self.dakika = zaman.minute
#		self.saniye = zaman.second	
	
#	def yazdir(self):
#
#		while True:
#			print("\rTarih => {}/{}/{} --- Saat => {}:{}:{} ".format(self.gun, self.ay, self.yil, self.saat, self.dakika, self.saniye),end="")
#			time.sleep(1)
#			self.zamanAl()

#if __name__ == "__main__":
#	s = Saat()
#	s.yazdir()


#---------------------------- # -----------------------------#  TAŞ KAGIT MAKAS #---------------------------- # -----------------------------#  
# import random
# import time

# class BasitTasKagitMakasOyunu():
    
#     def __init__(self):
#         self.secim()

#     def secim(self):
#         baslik = "Taş Kağıt Makas Oyunu Oynama"
#         print("*" * len(baslik), baslik, "*" * len(baslik), sep="\n",end="\n")
#         while True:
#             tercih = input("Oyunun açıklaması için 1'e oyuna giriş için 2'ye basınız :")

#             if tercih == "1":
#                 self.oyunAciklamasi()
#             elif tercih =="2":
#                 self.tasKagitMakasOyunu()
#                 break
#             else:
#                 print("Geçersiz bir karaktere bastınız.. İşleminiz İPTAL ediliyor..")
#                 break

#     def oyunAciklamasi(self):
#         print("""Oyunun Açıklaması = >
#     Klasik taş kağıt makas oyunu. 
#     Kullanıcının seçim yaptığı andaki bilgisayarın kullandığıyla kullanıcının seçtiği karşılaştırılıyor. 
#     Oyun, kullanıcı seçim ekranında 1 veya TAŞ, 2 VEYA KAĞIT, ya da 3 VEYA MAKAS dışında 
#     bir veri girene kadar devam ediyor.
#     """)

#     def tasKagitMakasOyunu(self):

#         durumlar=["TAŞ","KAĞIT","MAKAS","1","2","3"]

#         while True:
#             kullanıcı = input("1){}\n2){}\n3){}\nSeçiniz =>".format(*durumlar)).upper()
#             bilgisayar = random.randrange(0,3)
#             sayı = -1

#             if kullanıcı in durumlar:
#                 if kullanıcı == "1" or kullanıcı == "TAŞ":
#                     sayı = 0

#                 elif kullanıcı == "2" or kullanıcı == "KAĞIT":
#                     sayı = 1

#                 elif kullanıcı == "3" or kullanıcı == "MAKAS":
#                     sayı = 2

#                 if sayı == bilgisayar:
#                     print("Berabere, sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))

#                 elif sayı == 0 and bilgisayar == 2:
#                     print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))

#                 elif sayı == 0 and bilgisayar == 1:
#                     print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))

#                 elif sayı == 1 and bilgisayar == 2:
#                     print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

#                 elif sayı == 1 and bilgisayar == 0:
#                     print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))

#                 elif sayı == 2 and bilgisayar == 1:
#                     print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

#                 elif sayı == 2 and bilgisayar == 0:
#                     print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

#                 print()
#             else:
#                 print("Oyun Bitiriliyor :(")
#                 break

# if __name__ == "__main__":
#     BasitTasKagitMakasOyunu()
#     time.sleep(1)
#---------------------------- # -----------------------------# FAİZ HESAPLAMA #---------------------------- # -----------------------------# 
# import time

# #varsayılan olarak yılı hesaplar
# def hesaplama(tarih="yıl",payda=100): 
#     anaPara = float(input("Faize koyacağınız Ana Paranızı giriniz :"))
#     faizOrani = float(input("Faiz Oranını Giriniz :%"))
#     tarihSayisi = float(input("Anaparanın faizde kalacağı {} sayısını giriniz :".format(tarih)))

#     getiri = round(((anaPara * faizOrani * tarihSayisi) / payda),2)
#     sonuc= round((anaPara + getiri),2)

#     print("{} TL, %{} faizle {} {} sonunda \n{} TL faiz getirirken toplamda {} TL paran olur.".format(anaPara, faizOrani, tarihSayisi, tarih, getiri, sonuc))

# def giris():
#     try:
#         baslık="Faiz Hesaplama Programı"
#         print("*"*len(baslık),baslık.upper(),"*"*len(baslık),sep="\n",end="\n\n")

#         tercihYazisi={
#                     "0":"Aşağıdakilerden birini tercih ediniz(Sıra numarasını giriniz) :",
#                     "1":"\n1) Yıllık basit faiz hesaplama",
#                     "2":"\n2) Aylık basit faiz hesaplama",
#                     "3":"\n3) Günlük basit faiz hesaplama"
#                     }
    
#         tercih=input("{}{}{}{}\nTercihiniz :".format(*tercihYazisi.values()))

#         if tercih == "1":
#             hesaplama("yıl", 100)
#         elif tercih == "2":
#             hesaplama("ay", 1200)
#         elif tercih == "3":
#             hesaplama("gün", 36500)
#         else:
#             print("Anlamsız bir tecih numarası girdiniz.")
#     except:
#         print("Anlaşılamayan bir hata oluştu :(\n")

# if __name__ == "__main__":
#     giris()
#     say = 20
#     while say:
#         print("\rProgram Kapatılıyor. Son {} sn...".format(say),end="")
#         time.sleep(1)
#         say -= 1
#---------------------------- # -----------------------------# SORTED AND LAMBDA #---------------------------- # -----------------------------# 
# tuple1=((1,'a'),(4,'c'),(3,'b'),(2,'d'))
# sorted(tuple1,key= lambda x:x[1])
#---------------------------- # -----------------------------# SAYI ADETİ VE LİSTE OLARAK ALINAN SAYILARIN MEDYAN MOD VE TEKRAR BULMA #---------------------------- # -----------------------------# 
# import numpy as np
# from scipy import stats

# size = int(input())
# numbers = list(map(int, input().split()))
# print(np.mean(numbers))
# print(np.median(numbers))
# print(int(stats.mode(numbers)[0]))