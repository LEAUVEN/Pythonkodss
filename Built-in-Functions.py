1)Abs(num)
Abs fonksiyonu ile içerisine girilen değerin gerçek değerini getiriyor.
Örneğin : number=*20
number=abs(number)
print(number) >>>> 20 
integer,floating ve complex sayılarda çalışıyor.
Complex örneği (Magnitude alıyor)
complex=(3-4j) 
print(abs(complex))>>>>5.0 >>>>>> (3^2+4^2)^(1/2)
2)any(iterable)
Any fonksiyonu ile değerlerin arasında gezerek true olup olmadıklarına bakılır. 
Eger en az 1 tanesi true ise any foksiyonu true değerini verir eğer hiç true yok ise false çıktısı verir
listem=['True', 'False', 'True']
result=any(listem)
print(result) >>>>> True 
Condition	                                    Return Value
All values are true	                            True
All values are false	                        False
One value is true (others are false)	        True
One value is false (others are true)	        True
Empty Iterable	                                False
Icerikteki değerler 0,false veya boş ise döngü false değeri verir. 

True since 1,3 and 4 (at least one) is true
l = [1, 3, 4, 0]
False since both are False
l = [0, False] >> False verir iken eğer l=['0',False] yapsaydık 0 string bir ifade içinde olacağı için True verirdi.

True since 5 is true
l = [0, False, 5]

False since iterable is empty
l = []
Dictionary için kullanımına bakalım:
keys kısımları boş veya false ise false değeri çıkartır:
d = {0: 'False', False: 0} >>>> False ,
d = {0: 'False', 1: 'False'} >>>>>True verir çünkü 1 sayısı true'dur.
d = {'0': 'False', False: 0}>>>>>>> True verir çünkü '0' string'i true'dur.