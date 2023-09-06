print("""********
      KULLANICI BİLGİLERİNİ GİRİNİZ!
********""")

syn_kullanıcı_adı="Efekan"
syn_parola="123"

kullanıcı_adı =input("Kullanıcı Adı :")
parola=input("Parola Giriniz :")


if (syn_kullanıcı_adı == "kullanıcı_adı" and syn_parola != "parola"):
    print("Parola Hatalı ...")

elif (syn_kullanıcı_adı != "kullanıcı_adı" and syn_parola == "parola"):    
    print("Kullanıcı Adı Hatalı ...")



else:
    print("Sisteme Başarıyla Giriş Yapıldı...")    