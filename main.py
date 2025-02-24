from kullanicisistemi import *

def print_menu():
    print("""
    1- Giriş Yap
    2- Kaydol
    3- Kapat
    """)

def login_menu(user):
    print(f"""
    {user[1]} {user[2]} ({user[3]})

    1- Bir kullanıcı arama
    2- Tüm kullanıcıları yazdır
    3- Hesabımı Sil
    4- Çıkış yap
    """)

create_table()

while True:
    print_menu()
    secim = input("Seçim: ")

    if secim == "1":
        username = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        search = search_username(username)

        if search is None:
            print("Böyle bir kullanıcı yok.")
            continue

        if password == search[4]:
            while True:
                login_menu(search)
                secim = input("Seçim: ")

                if secim == "1":
                    u = input("Kullanıcı Adı: ")
                    birisi = search_username(u)
                    if birisi is None:
                        print("Kullanıcı Bulunamadı")
                    else:
                        print(f"{birisi[1]} {birisi[2]} ({birisi[3]})")

                elif secim == "2":
                    print_all()

                elif secim == "3":
                    delete_account(username)
                    print("Hesabınız silindi.")
                    break  

                elif secim == "4":
                    break

        else:
            print("Şifre yanlış!")

    elif secim == "2":
        name = input("Adınız: ")
        lastname = input("Soyadınız: ")
        username = input("Kullanıcı Adınız: ")
        password = input("Şifreniz: ")

        if insert(name, lastname, username, password):
            print("Kayıt başarılı!")

    elif secim == "3":
        break
