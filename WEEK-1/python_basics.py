##################
# PYTHON TEMELLERİ
##################
print("Hello, AI Era!")

###############################################
# Sayılar (Numbers) ve Karakter Dizileri (Strings)
###############################################

print(33)

type(33.34)
type("Hello, AI Era!")

###################################################
# Atamalar ve Değişkenler (Assignments & Variables)
###################################################
a = 33
print(a)
a * 10

b = "Hello, AI Era!"
b

c = 10
a * c
d = a - c
d

#######################
# VERİ YAPILARINA GİRİŞ
#######################
# Integer (Sayı)
x = 33
type(x)

# Float (Sayı)
y = 33.34
type(y)

# Complex (Sayı)
z = 8j + 18
type(z)

# Strings (Karakter Dizileri)
a = "Hello World"
type(a)

# Boolean
b = True
type(b)

c = 23 < 22
print(c)
type(c)


# Listeler
l = [1, 2, 3, 4, "String", 3.2, False]
type(l)
# Sıralıdır
# Kapsayıcıdır
# Değiştirilebilir

# Dictionary (Sözlük)
d = {"Name": "Jake",
     "Age": [27, 56],
     "Adress": "Downtown"}
type(d)
# Değiştirilebilir
# Kapsayıcı
# Sırasız
# Key değerleri farklı olacak


# Tuple
t = ("Machine Learning", "Data Science")
type(t)
t
# Değiştirilemez
# Kapsayıcı
# Sıralı


# Set
s = {"Python", "Machine Learning", "Data Science", "Python"}
type(s)
print(s)
# Değiştirilebilir
# Sırasız + Eşsiz
# Kapsayıcı

#########################################
# Sayılar (Numbers): int, float, complex
#########################################
x = 8  # int
type(x)

y = 3.2  # float
type(y)

z = 8j + 18  # complex
type(z)

x * 4
y / x
x + y + z

# Tipleri değiştirmek
float(x)
int(y)
int(3.9)
int(z)  # ERROR

calc = x * y / 10
print(calc)
int(calc)


#############################
# Karakter Dizileri (Strings)
#############################

print("Miuul")
print('Miuul')
name = "Miuul"
name = 'Miuul'

# Çok satırlı karakter dizileri
long_str = """Veri Yapıları ve Tipler:
int, float, complex → Sayılar
str → Karakter Dizisi
list, tuple, set, dict → Koleksiyonlar
bool → Mantıksal Değer"""
print(long_str)


# Karakter Dizilerinin Elemanlarına Erişmek
name
name[0]
name[4]

# Karakter Dizilerinde Slice İşlemi
name[0:3]
long_str[2:7]


# String İçerisinde Karakter Sorgulamak
long_str
"Veri" in long_str
"veri" in long_str


###################
# String Metodları
###################
dir(str)
text = "hello, AI Era!"
len(text)  # stringin uzunluğu
text.upper()  # tüm karakterleri büyük harf yapar
text.lower()  # tüm karakterleri küçük harf yapar
text.replace("l", "k")  # karakteri değiştirir

text.upper().replace("L", "K")  # metodlar arka arkaya kullanılabilir!
text.upper().replace("l", "k")

text.split()  # Stringi böler
text.capitalize()


#################
# Listeler (List)
#################
# - Değiştirilebilir
# - Sıralıdır. Index işlemleri yapılabilir.
# - Kapsayıcıdır. Yani birden fazla veri yapısını içerisinde tutabilir.

lst = ["Data Science", 101, True, ["Miuul"]]
len(lst)
lst[0]
lst[2]

#################
# Liste Metodları
#################

lst.append(33.34)  # eleman ekler
print(lst)

lst.pop(1)  # indexe göre eleman siler
lst

lst.insert(0, "AI")  # indexe ekleme yapar
lst

# Her fonksiyon her veri tipinde kullanılmaz!
lst.upper()  # ERROR

##################################################
# FONKSİYONLAR, KOŞULLAR, DÖNGÜLER, COMPREHENSIONS
##################################################

##########################
# Fonksiyonlar (Functions)
##########################

# Elimizdeki değeri 3 ile çarpmak istiyor olalım
5*3
12*3


def multiply_three(number):
    print(number * 3)

multiply_three(5)
multiply_three(12)
multiply_three(number=16)


# Ön tanımlı argümanlar
def hi(word="Selam"):
     print(word, "Miuul!")

hi()
hi(word="Merhaba")


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.
def difference(num1, num2):
     result = num1 - num2
     print(result)

difference(7, 8)
difference(8, 7)

difference(num1=8, num2=7)
difference(num2=8, num1=7)



# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
def difference(num1, num2=4):
     result = num1 - num2
     return result

difference(10)
difference(10, 2)

res = difference(10, 2)
res


# Ne zaman fonksiyon yazarız?
# DRY => Don't Repeat Yourself!

# Örnek: Öğrencilerin vize notlarının %40'ını, final notlarının %60'ını ağırlık olarak alan bir fonksiyon yaz
# Öğrenci1: vize:40, final:70
# Öğrenci2: vize:80, final:20

ogr1 = (40*0.4) + (70*0.6)
ogr2 = (80*0.4) + (20*0.6)
print(ogr1, ogr2)

def note_calculator(vize_notu, final_notu):
     return (vize_notu*0.4) + (final_notu*0.6)

ogr1 = note_calculator(40, 70)
ogr2 = note_calculator(vize_notu=80, final_notu=20)
print(ogr1, ogr2)


#######################
# Koşullar (Conditions)
#######################

3 == 3
3 == 4

# if condition
if 3 == 3:
     print("eşit")


# if-else condition
name = "Furkan"
if name == "Vahit":
     print("İsim Vahit!")
else:
     print("İsim Vahit değil!")


# if-elif-else
name = "Furkan"
if name == "Vahit":
     print("İsim Vahit!")
elif name == "Furkan":
     print("İsim Furkan!")
else:
     print("İsim Furkan veya Vahit değil!")




# Fonksiyonla birleştirelim
def check_name(name):
     if name == "Vahit":
          print("İsim Vahit!")
     elif name == "Furkan":
          print("İsim Furkan!")
     else:
          print("İsim Furkan veya Vahit değil!")

check_name("Elif")
check_name(name="Vahit")



##################
# DÖNGÜLER (LOOPS)
##################
# for loop
bootcamps = ["Data Science", "Data Analytics", "AWS Cloud Engineering"]
bootcamps[0]
bootcamps[1]

for bc in bootcamps:
    print(bc)


for bc in bootcamps:
    print(bc.upper())


notes = [30, 50, 85]
for note in notes:
    print(note)


for note in notes:
    print( int(1.5*(note+10)) )


def extra_notes(note, extra_point):
     new_note = int(1.5*(note+extra_point))
     if new_note > 100:
          new_note = 100

     return new_note

extra_notes(30, 10)
extra_notes(50, 30)


for note in notes:
     print("Eski Not:", note)
     print("Yeni Not:", extra_notes(note, 10))
     print("-------------------")


# while-loop
num = 5
while num < 10:
     print(num)
     num = num + 1  # unutulursa infinite-loop


# Notes örneğinin while ile yazımı
idx = 0
while idx < len(notes):
    note = notes[idx]
    print("Eski Not:", note)
    print("Yeni Not:", extra_notes(note, 10))
    print("-------------------")
    idx += 1