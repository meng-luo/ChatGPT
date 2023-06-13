import sqlite3

# 创建数据库连接
db = sqlite3.connect('data.db')

cursor = db.cursor()

exist = cursor.execute('SELECT name FROM sqlite_master WHERE type="table" AND name = "api_key";').fetchone()

if not exist:
    cursor.execute('''create table api_key (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key varchar not null,
        total FLOAT default 0,
        used FLOAT default  0,
        rest FLOAT default 0);''')
    print('创建表成功')

db.commit()
db.close()