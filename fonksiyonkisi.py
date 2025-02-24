import sqlite3 as sql

def insert(ad,soyad,yas):
    conn = sql.connect("kisi.db")
    cursor = conn.cursor()

    add_command = """INSERT INTO KULLANICILAR VALUES {}"""
    data = (ad, soyad, yas)

    cursor.execute(add_command.format(data))

    print(f"{ad, soyad} Eklendi")

    conn.commit()
    conn.close()

insert('Yusuf','Demir',29)



# Veri silme
def delete_name(ad):
    conn = sql.connect("kisi.db")
    cursor = conn.cursor()


    delete_command = """DELETE from KULLANICILAR WHERE ad= '{}' """
    cursor.execute(delete_command.format(ad))

    conn.commit()
    print(f"{ad} Silindi")
    conn.close()

#delete_name('Yusuf')