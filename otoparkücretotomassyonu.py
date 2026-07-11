arac_tipi=input("araç tipini giriniz ")
sure=int(input("otoparkta kaldığınız süreyi giriniz saat olarak giriniz:"))
abonelik=input("abonemisiniz:")
ucret=0
if arac_tipi=="binek":
    print("1.kata çıkın-binek araç park yeri")
    ucret=sure*20
elif arac_tipi=="suv":
    print("2. kata çıkın-suv araç park yeri")
    ucret=sure*30
elif arac_tipi=="ticari":
    print("3.kata çıkın-ticari araç park yeri")
    ucret=sure*40
else:
    print("geçersiz araç tipi")
if sure<1:
    print("bir saatten az kaldığınız için ücretiniz 15 tl")
    ucret=15
elif sure>=6:
    print("5 saatten fazla kaldığınız için 25 tl ek ücretiniz var:")
    ucret=ucret+25
if abonelik=="evet":
    ucret=ucret*0.8
elif abonelik=="hayir":
    ucret=ucret
print("odemeniz gereken toplam tutar:",ucret, "TL")
