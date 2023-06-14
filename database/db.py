import sqlite3


def key_add(data):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute("INSERT INTO api_key(key) VALUES ('{}')".format(data))
    db.commit()
    db.close()


def data_update(total_data, used_data, rest_data, data):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute("UPDATE api_key set total = ?, used = ?, rest = ? where key= ?",
                   (total_data, used_data, rest_data, data))
    db.commit()
    db.close()


def key_delete(data):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute("DELETE from api_key where key=('{}')".format(data))
    db.commit()
    db.close()


def data_get():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    output = cursor.execute("SELECT key, total, used, rest from api_key").fetchall()
    db.close()
    return output


def key_get():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    output = cursor.execute("SELECT key from api_key ORDER BY RANDOM() LIMIT 1;").fetchone()
    db.close()
    return output


def proxy_read():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    output = cursor.execute("SELECT ip from proxy where id = 1;").fetchone()
    db.close()
    return output


def proxy_set(ip):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute("UPDATE proxy  set ip = '{}' where id = 1".format(ip))
    db.commit()
    db.close()
