#####################################
# Python Temelleri - Ödev Scripti
#####################################
import numpy as np
# Soru 1:
# Bir integer, bir float ve bir complex sayı tanımlayın.
# Bu sayıların türlerini yazdırın ve aralarında 1-2 işlem yapın.
a=complex(3,4)
b=3
c=5.6
d=b+c
e=a+b
f=a+c


# Soru 2:
# İsminizi içeren bir string değişkeni oluşturun.
# Bu stringin ilk ve son karakterini yazdırın. Ayrıca tüm harfleri büyük yaparak ekrana yazdırın.

name="Berat"
len_name=len(name)
output=f"1-{name[0]} son- {name[len_name-1]}"


# Soru 3:
# Aşağıdaki string içinde "veri" kelimesi geçiyor mu kontrol edin.
# Ardından bu stringi boşluklardan bölerek liste haline getirin.

sentence = "Veri bilimi yapay zeka ile birleştiğinde güçlü sonuçlar doğurabilir."
def search(text):
    text_list=[]
    for s in text.lower().split():
        text_list.append(s)
        if s=="veri":
            print("veri içeriyor")
        else:
            pass
    print(text_list)
        
    

print(search(sentence))

# Soru 4:
# İçerisinde 3 farklı türde veri bulunan bir liste oluşturun.
# Listenin uzunluğunu, ilk ve son elemanını yazdırın.
# Ardından bu listeye yeni bir eleman ekleyin ve ikinci elemanı silin.
liste=[3,4,5,4.4,5.3,"berat",4]
list_len=len(liste)
print(f"liste ilk eleman- {liste[0]} liste son eleman- {liste[list_len-1]}")
liste.pop(0)
del liste[list_len-2]



# Soru 5:
# 2 parametre alan bir fonksiyon yazın. Bu fonksiyon, aldığı iki sayının ortalamasını dönsün.
def sum(a,b):
    return np.mean(a+b)
print(sum(3,4))



# Soru 6:
# Kullanıcının yaşına göre mesaj yazdıran bir fonksiyon yazın:
# 18'den küçükse "Çok gençsin!", 18-40 arasıysa "Harika bir yaştasın!", 40'tan büyükse "Deneyim önemli!" mesajını yazdırsın.
age=input("Yaş gir:")
def returnMessage(age):
    if int(age)<=18:
        print("Çok gençsin")
    elif 18<int(age)<=40:
        print("harika bir yaştasın")
    else:
        print("Deneyim önemli!")


returnMessage(age)

# Soru 7:
# İçerisinde sayılar olan bir liste içindeki sayıları dolaşarak 2 katını ekrana yazdırın (for döngüsü ile).
liste_int=[10,24,5,6,23,65]
for i in liste_int:
    print(i*2)

print("\n")
# Soru 8:
# 1'den başlayarak 20 dahil olacak şekilde çift sayıları yazdırın (while döngüsü ile).
n=1
while(n!=21):
    if n%2==0:
        print(n)
    n+=1


# Soru 9:
# Bir çalışanın haftalık maaşını hesaplayan bir fonksiyon yazın.
# Saatlik ücreti ve haftalık toplam çalışma saati parametre olarak alınsın.
# Haftada 40 saatten fazla çalıştıysa, fazla saatler için %50 zamlı ücret ödensin (mesai).
# Örnek: 45 saat çalışan biri için 5 saatlik mesai uygulanmalı.

def salary_calculator(payment_hour,total_time_week):
    if int(total_time_week)<=40:
        print(f"Maaşın:{total_time_week*payment_hour}")
    else:
        extra_salary_time=total_time_week-40
        salary=40*payment_hour+(extra_salary_time*(1.5*payment_hour))
        print("Maaşınız:",salary)
salary_calculator(15,45)

