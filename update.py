import sqlite3

banco = sqlite3.connect("primeiro_banco.db")
cursor = banco.cursor()

cursor.execute("UPDATE pessoas SET nome = 'Jenifer' WHERE idade = 27")
banco.commit()
