import os
import sqlite3
from flask import Flask, render_template

# from .db_session import SqlAlchemyBase

app = Flask(__name__)


connect = sqlite3.connect('tg_bot.sqlite', check_same_thread=False)
cur = connect.cursor()



@app.route('/')
@app.route('/Главная.html')
@app.route('/templates/Главная.html')
def gl():
    return render_template('index.html')


@app.route('/templates/Телеграм-бот.html')
@app.route('/Телеграм-бот.html')
def bot():
    return render_template('Телеграм-бот.html')


@app.route('/templates/Таблица-рейтинга.html')
@app.route('/Таблица-рейтинга.html')
def bot456():
    cur.execute('SELECT name, balls FROM users ORDER BY balls DESC')
    rows = cur.fetchall()
    rows = list(rows)
    return render_template('Таблица-рейтинга.html', rows=rows)


if __name__ == '__main__':
    app.run()
