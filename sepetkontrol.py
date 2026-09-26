uyelik=input("premium üyeliğiniz varmı:")
sepet=int(input("sepet tutarınızı giriniz:"))
if uyelik =="evet" and sepet >= 500:
  sepet=sepet*(0.8)
  print(f"ödenecek tutar {sepet}")
elif uyelik == "evet" and sepet < 500:
  sepet=sepet*(0.9)
  print(f"ödenecek tutar {sepet}")
elif uyelik =="hayır" and sepet >= 500:
  sepet=sepet*(0.95)
  print(f"ödenecek tutar {sepet}")
elif uyelik =="hayır" and sepet < 500:
  print(f"ödenecek tutar {sepet}")
else:
  print("istenen bilgileri düzgün girdiğinize emin olun (not:üyelik kısmına sadece evet veya hayır yazın)")