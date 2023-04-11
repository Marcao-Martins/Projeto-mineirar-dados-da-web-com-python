import scrapy
import sqlite3

class MyCustomSpider(scrapy.Spider):
    name = 'minha_spider'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        # Use a expressão XPath para obter as frases
        frases = response.xpath("*//div/span[@class='text']/text()").getall()

        # Conecte ao banco de dados e insira as frases na tabela SQL
        conn = sqlite3.connect('exemplo.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS frases (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                frase TEXT
            )
        ''')
        for frase in frases:
            cursor.execute("INSERT INTO frases (frase) VALUES (?)", (frase,))
        conn.commit()
        conn.close()

        # Retorne os itens processados, se necessário
        yield {'frases': frases}
