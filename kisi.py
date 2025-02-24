import sqlite3 as sql

conn = sql.connect("kisi.db")

print("Bağlantı Gerçekleştirildi")

#sql komut icin
cursor = conn.cursor()
print("cursor oluşturuldu")

cursor.execute(""" CREATE TABLE IF NOT EXISTS KULLANICILAR(
               ad text,
               soyad text,
               yas integer
      
               )
""")

add_commend = """ INSERT INTO KULLANICILAR VALUES {} """
data1= ('Ahmet','Ak',24)

#cursor.execute(add_commend.format(data1))


#guncelleme islemi

#cursor.execute(""" UPDATE KULLANICILAR SET yas = 28 WHERE ad= 'Yusuf' AND soyad = 'Demir' """)
print("Güncelleme Başarılı")



#tablodaki verileri yazdırma islemi
cursor.execute(""" SELECT rowid, * from  KULLANICILAR """)
#list1 = cursor.fetchall() 

"""
for kisi in list1:
    print(kisi)
"""


list2 = cursor.fetchmany(2)


conn.commit()

#bagalanti kapama
conn.close()