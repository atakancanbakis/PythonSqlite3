import sqlite3 as sql

def create_table():
    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS USERS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        lastname TEXT NOT NULL,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    ) 
    """)
    
    conn.commit()
    conn.close()


# Kayıt ekleme (boş girişleri ve kullanıcı adı tekrarını önleme)
def insert(name, lastname, username, password):
    if not name or not lastname or not username or not password:
        print("Tüm alanları doldurmalısınız!")
        return False

    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    # Kullanıcı adı daha önce var mı kontrol et
    cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        print("Bu kullanıcı adı zaten kullanılıyor!")
        conn.close()
        return False

    cursor.execute("INSERT INTO USERS (name, lastname, username, password) VALUES (?, ?, ?, ?)", 
                   (name, lastname, username, password))

    conn.commit()
    conn.close()
    return True


# Tüm kullanıcıları listeleme
def print_all():
    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM USERS")
    list_all = cursor.fetchall()

    for i in list_all:
        print(i)

    conn.close()


# Kullanıcı arama
def search_username(username):
    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM USERS WHERE username = ?", (username,))
    user = cursor.fetchone()

    conn.close()
    return user


# Şifre güncelleme
def update_password(username, newPassword):
    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE USERS SET password = ? WHERE username = ?", (newPassword, username))
    conn.commit()
    conn.close()


# Kullanıcı silme
def delete_account(username):
    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM USERS WHERE username = ?", (username,))
    conn.commit()
    conn.close()


# Tablonun tamamını silme
def delete_table():
    conn = sql.connect('kisi.db')
    cursor = conn.cursor()

    cursor.execute("DROP TABLE USERS")

    conn.commit()
    conn.close()
