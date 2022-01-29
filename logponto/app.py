import sqlite3

conn = sqlite3.connect('ponto.db')

cursor = conn.cursor()
# inserindo dados na tabela
cursor.execute("""
INSERT INTO ponto (horainicial, horafinal)
VALUES (date('now'), null)
""")

# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()