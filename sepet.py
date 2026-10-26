
urunler = {
1:  {"ad": "Elma (1 kg)",       "fiyat": 35.0},
2:  {"ad": "Muz (1 kg)",        "fiyat": 60.0},
3:  {"ad": "Süt (1 L)",         "fiyat": 32.5},
4:  {"ad": "Ekmek",             "fiyat": 15.0},
5:  {"ad": "Yumurta (10'lu)",   "fiyat": 55.0},
6:  {"ad": "Peynir (500 g)",    "fiyat": 120.0},
7:  {"ad": "Zeytin (500 g)",    "fiyat": 95.0},
8:  {"ad": "Domates (1 kg)",    "fiyat": 30.0},
9:  {"ad": "Salatalık (1 kg)",  "fiyat": 25.0},
10: {"ad": "Pirinç (1 kg)",     "fiyat": 70.0},
11: {"ad": "Makarna",           "fiyat": 20.0},
12: {"ad": "Un (2 kg)",         "fiyat": 65.0},
13: {"ad": "Şeker (1 kg)",      "fiyat": 45.0},
14: {"ad": "Çay (1 kg)",        "fiyat": 210.0},
15: {"ad": "Kahve (100 g)",     "fiyat": 150.0},
16: {"ad": "Su (5 L)",          "fiyat": 25.0},
17: {"ad": "Meyve Suyu (1 L)",  "fiyat": 40.0},
18: {"ad": "Çikolata",          "fiyat": 30.0},
19: {"ad": "Bisküvi",           "fiyat": 18.0},
20: {"ad": "Deterjan (3 kg)",   "fiyat": 250.0},
}


sepet = []
while True:
  print()
  print("------ Hangi işlemi yapmak istiyorsunuz -------")
  print("1 - Ürünleri listele")
  print("2 - Sepete ürün ekle")
  print("3 - Sepeti göster")
  print("4 - Çıkış")

  islem = input("Seçiminiz: ")

  if islem == "1":
    print("\n--- Ürün Listesi ---")
    for kod, bilgi in urunler.items():
      print(f"{kod}. {bilgi['ad']} - {bilgi['fiyat']} TL")

  elif islem == "2":
    print("\n--- Ürün Listesi ---")
    for kod, bilgi in urunler.items():
      print(f"{kod}. {bilgi['ad']} - {bilgi['fiyat']} TL")

    # Sürekli ürün ekleme döngüsü (Çıkış için 'q')
    while True:
      giris = input(
          "Sepete eklemek istediğiniz ürünün numarasını girin (Ana menüye dönmek"
          " için 'q'): "
      )

      # Kullanıcı 'q' veya 'Q' basarsa bu döngüden çıkıp ana menüye dönecek
      if giris.lower() == "q":
        print("Ana menüye dönülüyor...")
        break

      try:
        urun_kodu = int(giris)
        if urun_kodu in urunler:
          adet = int(
              input(
                  f"Kaç adet '{urunler[urun_kodu]['ad']}' almak istiyorsunuz?"
                  " "
              )
          )
          if adet > 0:
            sepet.append({"kod": urun_kodu, "adet": adet})
            print(f"Başarıyla eklendi: {adet} adet {urunler[urun_kodu]['ad']}")
          else:
            print("Adet 0'dan büyük olmalıdır!")
        else:
          print("Geçersiz ürün numarası!")
      except ValueError:
        print("Hatalı giriş! Lütfen geçerli bir sayı girin veya 'q' ya basın.")

  elif islem == "3":
    if len(sepet) == 0:
      print("Sepetiniz boş.")
    else:
      print()
      print("--- SEPETİNİZ ---")

      toplam = 0
      for sira, item in enumerate(sepet, start=1):
        urun = urunler[item["kod"]]
        urun_toplam = urun["fiyat"] * item["adet"]
        toplam += urun_toplam
        print(
            f"{sira}. {urun['ad']} - {item['adet']} adet - {urun_toplam} TL"
            f" (Birim: {urun['fiyat']} TL)"
        )

      print("Toplam Tutar:", toplam, "TL")

  elif islem == "4":
    print("Görüşmek üzere!")
    break

  else:
    print("Geçersiz seçim.")