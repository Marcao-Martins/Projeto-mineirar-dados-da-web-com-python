import scrapy
import sqlite3

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    # Função para configurar a conexão com o banco de dados
    def __init__(self):
        self.conn = sqlite3.connect('quotes.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS quotes (quote TEXT)')

    def parse(self, response):
        for quote in response.xpath('//div[@class="quote"]'):
            try:
                quote_text = quote.xpath('./span[@class="text"]/text()').get()
                print(quote_text)
                # Insere a citação no banco de dados
                self.cursor.execute('INSERT INTO quotes (quote) VALUES (?)', (quote_text,))
                self.conn.commit()
            except:
                pass

    # Função para fechar a conexão com o banco de dados ao final do spider
    def close(self, reason):
        self.cursor.close()
        self.conn.close()
