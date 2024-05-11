import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, task TEXT, status TEXT)")
        self.conn.commit()

    def insert(self, task, status):
        self.cur.execute("INSERT INTO todo VALUES (NULL, ?, ?)", (task, status))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM todo")
        rows = self.cur.fetchall()
        return rows

    def search(self, task="", status=""):
        self.cur.execute("SELECT * FROM todo WHERE task=? OR status=?", (task, status))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM todo WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, task, status):
        self.cur.execute("UPDATE todo SET task=?, status=? WHERE id=?", (task, status, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()