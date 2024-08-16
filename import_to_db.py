import sqlite3

# 创建数据库和表
def create_database(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS directories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            directory TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# 导入数据到数据库
def import_to_db(file_path, db_path):
    create_database(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    with open(file_path, "r") as file:
        for line in file:
            directory = line.strip()
            if directory:  # 忽略空行
                cursor.execute('INSERT INTO directories (directory) VALUES (?)', (directory,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    import_to_db("directories.txt", "directories.db")
