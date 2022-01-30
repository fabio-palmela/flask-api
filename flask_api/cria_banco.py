import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = """
    CREATE TABLE IF NOT EXISTS hoteis(
        hotel_id int PRIMARY KEY, 
        nome text, 
        estrelas real,
        diaria real,
        cidade text
    )
"""
cursor.execute(cria_tabela)

cria_hotel = """
    INSERT INTO hoteis(hotel_id, nome, estrelas ,diaria, cidade)
    VALUES(1, 'Alpha Hotel', 4.3, 345.56, 'Rio de Janeiro')
"""
cursor.execute(cria_hotel)

connection.commit()
connection.close()