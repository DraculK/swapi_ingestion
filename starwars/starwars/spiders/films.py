# Imports
import json
import os
import re
import scrapy
from ..items import StarwarsItemFilms

# Classe principal que define como a api de films sera 'crawleada'


class FilmsSpider(scrapy.Spider):
    # informações do crawler
    name = "films"
    allowed_domains = ["swapi.dev"]
    start_urls = ["https://swapi.dev/api/films/"]

    # setting para salvar o output em csv e na pasta work
    custom_settings = {
        "FEEDS": {"work/films.csv": {"format": "csv"}}
    }

    # método callback principal que faz as primeiras requisições
    def parse(self, response):
        # for de 1 a 5 para criar link para ser acessado pelo follow
        for i in range(1, 6):
            link = f"{self.start_urls[0]}{i}/?format=json"
            yield response.follow(link, callback=self.parseFilms)

    # método que pega os dados da api
    def parseFilms(self, response):
        # classe responsável por estruturar nosso dados
        items = StarwarsItemFilms()
        # carrega o json da api
        data = json.loads(response.body)
        # caminho para guardar os dados crus da api
        path = "raw"

        # criação do diretório raw, caso não exista
        if not os.path.exists(path):
            os.makedirs(path)
        # abre o json para salvar o dado cru
        with open("raw/films.json", "a") as file:
            json.dump(data, file)

        # pega as informações da api pelas labels e transforma em lower case
        # as que não são
        title = data.get("title").lower()
        episode_id = data.get("episode_id")
        opening_crawl = data.get("opening_crawl").lower()
        director = data.get("director").lower()
        producer = data.get("producer").lower()
        release_date = data.get("release_date").lower()
        characters = data.get("characters")
        planets = data.get("planets")
        starships = data.get("starships")
        vehicles = data.get("vehicles")
        species = data.get("species")
        created = data.get("created").lower()
        edited = data.get("edited").lower()
        url = data.get("url").lower()

        # guarda os dados na estrutura pré definida por items e remove
        # os caracteres especiais
        items["title"] = re.sub(r"[^a-zA-Z0-9 ]+", '', title)
        items["episode_id"] = episode_id
        items["opening_crawl"] = re.sub(r"[^a-zA-Z0-9 ]+", '', opening_crawl)
        items["director"] = re.sub(r"[^a-zA-Z0-9 ]+", '', director)
        items["producer"] = re.sub(r"[^a-zA-Z0-9 ]+", '', producer)
        items["release_date"] = re.sub(r"[^a-zA-Z0-9 ]+", '', release_date)
        items["characters"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', character)
                               for character in characters]
        items["planets"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', planet)
                            for planet in planets]
        items["starships"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', starship)
                              for starship in starships]
        items["vehicles"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', vehicle)
                             for vehicle in vehicles]
        items["species"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', specie)
                            for specie in species]
        items["created"] = re.sub(r"[^a-zA-Z0-9 ]+", '', created)
        items["edited"] = re.sub(r"[^a-zA-Z0-9 ]+", '', edited)
        items["url"] = re.sub(r"[^a-zA-Z0-9 ]+", '', url)

        # retorna os dados
        yield items
