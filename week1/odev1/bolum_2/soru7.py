urun_fiyat = float(input("fiyat: "))
oran = float(input("İndirim oranı(%): "))

ind_fiyat = (urun_fiyat*((100-oran)/100))

print("İndirimli fiyat :", ind_fiyat)