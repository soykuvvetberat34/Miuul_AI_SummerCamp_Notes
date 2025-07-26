#########################
# Python ile Veri Analizi
#########################

########
# NUMPY
########

import numpy as np
l1 = [1, 3, 5, 7]
l2 = [2, 4, 6, 8]

lst = []
for i in range(0, len(l1)):
    lst.append(l1[i] * l2[i])
print(lst)

arr1 = np.array([1, 3, 5, 7])
arr2 = np.array([2, 4, 6, 8])
arr1 * arr2

# Numpy Arrayleri
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
arr

np.zeros(5)  # 0'lardan oluşan np array
np.ones(5)  # 1'lerden oluşan np array
np.arange(0, 10, 2)  # 0-10 arasında 2'şer artarak oluşan array
np.linspace(0, 1, 5)  # 0 ile 1 arasında 5 sayı
np.random.randint(0, 100, size=5)  # 0-99 arası rastgele 5 sayı
np.random.normal(loc=0, scale=1, size=(2, 3))  # normal dağılıma göre 2x3 matris


# Numpy Attributes
arr1d = np.arange(0, 10, 2)
arr1d
arr1d.shape  # 1 - tek boyutlu array
arr1d.ndim  # boyut bilgisi
arr1d.size  # toplam eleman sayısı

# Randomlığı engellemek için
np.random.seed(42)
arr2d = np.random.normal(loc=0, scale=1, size=(2, 3))
arr2d
arr2d.shape
arr2d.ndim
arr2d.size


################################
# Index Seçimi (Index Selection)
################################
arr1d
arr1d[:3]

arr2d
arr2d[1, 2]  # [satır, sütun]

# NUMPY İÇERİSİNDE TEK TİP VERİ TUTAR!
arr1d
arr1d[3] = 12.2
arr1d

arr2d[1, 2] = 33
arr2d

##################################
# Numpy ile Matematiksel İşlemler
##################################
arr = np.array([1, 2, 3, 4, 5])
arr * 2
np.sum(arr)
np.mean(arr)
np.median(arr)
np.std(arr)

############################
# Numpy ile Koşullu İşlemler
############################
arr > 4
arr[arr > 4]
arr[arr != 4]


#########
# PANDAS
#########

###############
# Pandas Series
###############
import pandas as pd
arr = np.array([1, 2, 3, 4, 5, 6, 7])
ser = pd.Series(arr)
ser
ser.shape
ser.ndim
ser.size
ser.head()
ser.tail()

##################
# Pandas DataFrame
##################
import seaborn as sns
df = sns.load_dataset("tips")
type(df)
df.head()
df.tail()

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)


##################
# Veriye İlk Bakış
##################
df.head()
df.tail()
df.columns
df.shape
df.dtypes
df.size
df.values
type(df.values)  # output = numpy.ndarray => numpy array
df.info()
df.dtypes
df.describe().T
df.isnull().sum()

# Pandas Fonksiyonları
df["total_bill"].head()
df["day"].value_counts()
df["day"].nunique()
df["day"].unique()

# Seçim ve Filtre İşlemleri (loc & iloc)
df["total_bill"] > 10
df[df["total_bill"] > 10].head()

# loc
# df.loc[satır, sütun]
df.loc[0:3, "total_bill"]

# loc ile filtreleme
df.loc[df["total_bill"] > 10].head()
df.loc[df["total_bill"] > 10, "size"].head()
df.loc[df["total_bill"] > 10, ["smoker", "size"]].head()

# iloc
df.iloc[0]
df.iloc[0, 2:4]

###################################
# Gruplama işlemleri (Aggregation)
###################################
# groupby
df.groupby("day")["total_bill"].mean()

df.groupby("day").agg({
    "total_bill": "mean"
})

df.groupby("day").agg({
    "total_bill": ["mean", "sum"],
    "tip": "mean"

})


# pivot table
df.pivot_table(values="total_bill", index="day", aggfunc="mean")
df.pivot_table(
    values=["total_bill", "tip"],
    index="day",
    aggfunc={
        "total_bill": ["mean", "sum"],
        "tip": "mean"
    }
)


##################################################
# KEŞİFÇİ VERİ ANALİZİ (EXPLORATORY DATA ANALYSIS)
##################################################
def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T) # sayısal değişkenlerin dağılım bilgisi


check_df(df)

############################
# Kategorik Değişken Analizi
############################
cat_cols = ['sex', 'smoker', 'day', 'time']
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "day") # 1 değişkene bakmak için

# tüm kategorik sütunlarda döngü
for col in cat_cols:
    cat_summary(df, col)

##########################
# Numerik Değişken Analizi
##########################
num_cols = ['total_bill', 'tip', 'size']
def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(dataframe=df, numerical_col="tip")  # 1 değişkene bakmak için

# tüm sayısal sütunlarda döngü
for col in num_cols:
    num_summary(df, col)

########################
# Hedef Değişken Analizi
########################
TARGET = "total_bill"
# Kategorik değişken ile hedef değişkenin ilişkisi
def target_summary_with_cat(dataframe, target, categorical_col):
    print(pd.DataFrame({"TARGET_MEAN": dataframe.groupby(categorical_col)[target].mean()}), end="\n\n\n")

for col in cat_cols:
    target_summary_with_cat(dataframe=df,
                            target=TARGET,
                            categorical_col=col)



