import sqlite3

conn = sqlite3.connect('ponto.db')

cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE ponto (
        horainicial DATETIMEE NOT NULL,
        horafinal DATETIMEE NULL
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()