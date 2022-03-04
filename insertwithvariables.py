import sqlite3

nome = "Origami"
idade = 10
email = "origami@gamil.com"

banco = sqlite3.connect("primeiro_banco.db")
cursor = banco.cursor()

cursor.execute(f'INSERT INTO pessoas VALUES ("{nome}", "{idade}", "{email}")')

banco.commit()

