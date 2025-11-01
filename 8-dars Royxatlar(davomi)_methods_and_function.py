"""
25.10.2025
Ro'yxatlar bilan ishlash. Methodlar va function lar bilan ishlash
methods.(.sort())
function (sum(),min(),max(),sorted(),list(),range())
Ro'yxatlardan nusxa olish
Tuple() o'zgarmas ro'yhat

"""


# davlatlar=["Uzbekiston","Braziya","Isponiya","Vatikan","Qozog'iston","Turkiya"]
# mashinalar=list(("BMW","audi","tico","damas","depal s07","onix"))
# sonlar=list((2,5,7,8))

# print(sonlar)
# print(davlatlar)
# print(mashinalar)

# mashinalar.sort("BMW","Matiz","Cobalt")
# print(mashinalar)

# sonlar.sort("6,4,7,-8")
# print(sonlar)

# sonlar=list(range(0,21))
# print(sonlar1)

# sonlar=list(range(-7,30,2))
# print(sonlar2)
# print(len(sonlar2))

# sonlar3=[89,-98,68,-3,-96,67,88,120,157,369,895,1235,2558,-65]
# min=min(sonlar3)
# max=max(sonlar3)

# print(sum(sonlar3))


davlatlar=["Uzbekiston","Braziya","Isponiya","Vatikan","Qozog'iston","Turkiya"]

country=davlatlar

print(davlatlar)
print("davlatlar nomli ro'yxat :",davlatlar)
print("country nomli ro'yxat :",country)
      
country.insert(0,"Singapur")
print(country)

print(country)
print(davlatlar)



toqson=list(range(1,21,2))
print("Asl ko'rinishi:",toqson)
print("1dan 7 gacha:",toqson[0:4])

# Tuple o'zgarmas ro'yhat

ismlar = ["maftuna","sharofat"]                 # oddiy ro'yhat
familyalar = ("madaminova","jumamurotova")             # O'zgarmas ro'yhat (tuple)
print("oddiy ro'yhat:",ismlar)
print("o'zgarmas ro'yhat:",familya)

ismlar.append("ismlar")
print(ismlar)

familyalar.append("familyalar")
print(familyalar)

o_familyalar = list(familyalar)
print(o_familyalar)          # tuple ni listga aylantirib olamiz
#o_familyalar.append("toshboyev")   #endi yangi element qo'sh

familyalar = tuple(o_familyalar)  # list ni yana tuple ga aylantirib olamiz
print(familyalar)







#O'zingizga ma'lum davlatlarning ro'yhatini tuzing va ro'yhatni konsolga chiqaring
davlatlar["Aqsh","O'zbekiston","Xitoy"]
print(davlatlar)

#2 Ro'yxatning uzunligini konsolga chiqaring

print(f "Ro'yhatdagi davlatlar soni :{len(davlatlar)} ga teng")

#3
print(f"davlatlarning tartiblangan ko'rinishi:{sorted(davlatlar)}")

#4
print(f"davlatlarning teskari tartiblangan ko'rinishi: {sorted(davlatlar,reverse = True)}")
#5
davlatlar.reverse()
print(davlatlar)
#6
davlatlar.reverse()
print(davlatlar)
#7
davlatlar.sort()
print(f"Alifbo bo'yicha tartiblangan ro'yhat:{davlatlar}")

davlatlar.sort(reverse=True)
print(f"Alifboga teskari tarzda tartiblangan royhat:{davlatlar}")

#8
juft_sonlar = list(range(120,33,87))
print(juft_sonlar)







