sepet=[]

while True:
    urunler=input("Sepete eklemek istediğiniz ürünü yazın (Çıkmak için 'q'):")
    if urunler.lower()=="q":
        break
    sepet.append(urunler)
for urunler in sepet:
    print(urunler)