from sqlite3 import connect
class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        self.conn = connect(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.conn.close()
        else:
            self.conn.commit()
            self.conn.close()

# Using the conetxt manager
with DataBase('test.db') as my_db:
    cursor = my_db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

