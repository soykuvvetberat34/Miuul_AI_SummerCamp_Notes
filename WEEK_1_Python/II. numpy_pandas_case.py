###############################
# Numpy & Pandas - Ödev Soruları
###############################

import numpy as np
import pandas as pd
import seaborn as sns

###############################
# Soru 1:
# 1D ve 2D array'ler oluşturun.
# Bu array’lerin boyut, eleman sayısı ve şekil bilgilerini yazdırın.
arr1d=np.arange(10,20)#1D
arr2d=np.random.randint(1,100,size=(3,4))#2D

print("1d:",arr1d.ndim,arr1d.size,arr1d.shape)
print("2d:",arr2d.ndim,arr2d.size,arr2d.shape)



###############################
# Soru 2:
# 5 elemanlı rastgele sayılardan oluşan bir array oluşturun.
# Elemanların ortalamasını, standart sapmasını ve medyanını bulun.
liste=np.random.randint(5,50,size=5)
print(f"array:{liste}\nmean: {np.mean(liste)}\nstandard sapma:{np.std(liste)}\nmedyan:{np.median(liste)}")





###############################
# Soru 3:
# 0 ile 1 arasında 10 eşit aralıklı sayı üretin.
# Bu sayılardan 0.5'ten büyük olanları filtreleyip yazdırın.
liste2=np.linspace(0,1,10)#0 ile 1 arasını 10 eşit parçaya böler
filtered=liste2[liste2>0.5]#tek satırda for
np.set_printoptions(precision=2)#noktadan sonra sadece 2 adım gösterir
#veya
#print(f"{liste2[2]:.2f}")
print("orijinal liste ",liste2)
print("Filtrelenmiş liste ",filtered)



###############################
# Soru 4:
# Pandas Series kullanarak öğrencilerin yaşlarını tutan bir seri oluşturun.
# Yaş ortalamasını ve en küçük yaşı bulun.
age_series=pd.Series([19,22,21,20,23,18])
print("en küçük yaş:",age_series.min())
print("Ortalama yaş:",age_series.mean())


###############################
# Soru 5:
# seaborn içerisinden "diamonds" veri setini alın.
# Sadece "carat" ve "price" sütunlarını içeren ilk 5 satırı yazdırın.

df=sns.load_dataset("diamonds")
print(df[["carat","price"]].head())

"""
df[["carat", "price"]] Çift köşeli parantez
Bu birden fazla sütun seçmek içindir, örneğin 'carat' ve 'price'. Sonuç bir DataFrame olur.

df["carat"]  Tek köşeli parantez
Bu sadece tek bir sütunu (örneğin 'carat') seçer ve sonuç bir Series olur.

df["carat"]  Tek sütun (Series)
df[["carat"]]  Tek sütun ama DataFrame formatında
df[["carat", "price"]] Çoklu sütun (DataFrame)

"""


###############################
# Soru 6:
# Fiyatı 15.000’den fazla olan kaç elmas var?
print(f"Fİyatı 15k dan fazla olan elmas sayısı:\n{df[df["price"]>15000].shape[0]}")

"""
df[df["price"] > 15000]
Bu, sadece price > 15000 olan satırları seçer.

.shape[0]
.shape, bir pandas DataFrame'in (satır sayısı, sütun sayısı) bilgisini verir.
.shape[0], bunun ilk kısmı, yani satır sayısını (kaç elmas olduğunu) verir.

shape bir tuple’dır (örneğin: (53940, 10)),
shape[0] ifadesi de bu tuple’ın ilk elemanını yani satır sayısını verir.
"""


###############################
# Soru 7:
# “cut” sütunundaki her bir kesim tipi için ortalama fiyatı(price) hesaplayın.
find=df.groupby("cut")["price"].mean()
print(find)

"""
df.groupby("cut")
df veri çerçevesindeki verileri "cut" sütunundaki değere göre gruplar.
Örneğin "Ideal", "Premium", "Good" gibi kesim türleri varsa, her biri bir grup olur.

"""


###############################
# Soru 8:
# pivot_table kullanarak her “cut” tipi için hem ortalama “carat” hem de “price” değerlerini gösterin.
pivot_table=df.pivot_table(
    values=["carat","price"],#dönmesi istenen değerler
    index="cut",#carat ve price değerleri bu değere göre seçielecek
    aggfunc="mean"#değerlere bu işlem uygulanacak
)
print(pivot_table)


###############################
# Soru 9:
# “color” sütununda kaç farklı renk olduğunu bulun. Her bir rengin kaç kez geçtiğini de yazdırın.
print(f"Farklı renk sayısı: {df["color"].nunique()} her rengin tekrar sayısı: {df["color"].value_counts()}")


###############################
# Soru 10:
# “cut” ve “clarity” kombinasyonlarına göre ortalama fiyatları hesaplayın.
grouped=df.groupby(["cut","clarity"])["price"].mean()
print(grouped)

#clarity ve cut bazında ortalama price döner