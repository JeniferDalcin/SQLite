import sqlite3

try:
    banco = sqlite3.connect("primeiro_banco.db")
    cursor = banco.cursor()

    cursor.execute("DELETE FROM pessoas WHERE idade = 27")
    banco.commit()
    banco.close()
    print("The data has been DELETED.")

except sqlite3.Error as error:
    print("Erro ao excluir os dados.", error)


