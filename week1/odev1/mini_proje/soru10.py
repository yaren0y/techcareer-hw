d_yili=int(input("Doğum yılınızı giriniz: "))

age = 2025-d_yili

if age<=12: 
    print("çocuksunuz")
elif 13<age<=17:
    print("ergensiniz")
else:
    print("Yetişkinsiniz")
