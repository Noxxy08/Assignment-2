import sqlite3

def main():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS students")
    cursor.execute("""
    CREATE TABLE students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    )
    """)

    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Anaiah", 5))
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Noxxy", 19))
    cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Brian", 23))
    conn.commit()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
if __name__ == "__main__":
    main()
