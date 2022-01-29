import sqlite3

conn = sqlite3.connect('ponto.db')

cursor = conn.cursor()

cursor.execute("""
SELECT * FROM ponto;
""")

print(cursor.fetchall())
for linha in cursor.fetchall():
    print(linha)

#print('Dados inseridos com sucesso.')

conn.close()