arac_hizi=int(input("aracın kaç km hız ile gittiğini belirtiniz:"))
if arac_hizi<=50:
    print("ihlalyok")
elif arac_hizi > 50 and arac_hizi <= 100:
    print("hız sınırını yüzde 100 e kadar aştığınız için 1000 tl ceza ödeyeceksiniz")
elif arac_hizi>100:
    print("hız sınırını belirlenen orandan fazla aştığınız için ehliyetinize 6 ay el konulacak")