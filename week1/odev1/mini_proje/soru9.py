urun_1 = float(input("1. ürün fiyatı : "))
urun_2 = float(input("2. ürün fiyatı : "))
urun_3 = float(input("3. ürün fiyatı : "))

toplam = urun_1 + urun_2 + urun_3

if toplam>200: 
    son_fiyat=(toplam*((100-10)/100))
    print("son fiyat:", son_fiyat)
else: 
    son_fiyat=toplam
    print("son fiyat:", son_fiyat)