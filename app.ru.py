from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gifts (
            id INTEGER PRIMARY KEY,
            fullname TEXT NOT NULL,
            gift_name TEXT NOT NULL,
            cost INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    ''')

    cursor.execute("DELETE FROM gifts")
    gifts_data = [
        ('Иван Иванович', 'Санки', 2000, 'куплен'),
        ('Ирина Сергеевна', 'Цветы', 3000, 'некуплен'),
        ('Петр Петрович', 'Книга', 1500, 'куплен'),
        ('Светлана Александровна', 'Игрушка', 1200, 'некуплен'),
        ('Олег Владимирович', 'Конструктор', 2500, 'куплен'),
        ('Елена Викторовна', 'Подарочная карта', 5000, 'некуплен'),
        ('Алексей Андреевич', 'Часы', 4000, 'куплен'),
        ('Наталья Сергеевна', 'Парфюм', 3500, 'некуплен'),
        ('Виктор Иванович', 'Кофеварка', 6000, 'куплен'),
        ('Анна Дмитриевна', 'Платок', 800, 'некуплен')
    ]
    cursor.executemany("INSERT INTO gifts (fullname, gift_name, cost, status) VALUES (?, ?, ?, ?)", gifts_data)

    conn.commit()
    conn.close()


init_db()


@app.route('/')
def home():
    conn = sqlite3.connect('gifts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM gifts")
    gifts = cursor.fetchall()
    conn.close()
    return render_template('index.html', gifts=gifts)


if __name__ == '__main__':
    app.run(debug=True)