# Imports
import json
import os
import re
import scrapy
from ..items import StarwarsItemPlanet

# Classe principal que define como a api de planets sera 'crawleada'


class PlanetsSpider(scrapy.Spider):
    # informações do crawler
    name = "planets"
    allowed_domains = ["swapi.dev"]
    start_urls = ["https://swapi.dev/api/planets/"]

    # setting para salvar o output em csv e na pasta work
    custom_settings = {
        "FEEDS": {"work/planets.csv": {"format": "csv"}}
    }

    # método callback principal que faz as primeiras requisições
    def parse(self, response):
        # for de 1 a 5 para criar link para ser acessado pelo follow
        for i in range(1, 6):
            link = f"{self.start_urls[0]}{i}/?format=json"
            yield response.follow(link, callback=self.parsePlanets)

    # método que pega os dados da api
    def parsePlanets(self, response):
        # classe responsável por estruturar nosso dados
        items = StarwarsItemPlanet()
        # carrega o json da api
        data = json.loads(response.body)
        # caminho para guardar os dados crus da api
        path = "raw"

        # criação do diretório raw, caso não exista
        if not os.path.exists(path):
            os.makedirs(path)
        # abre o json para salvar o dado cru
        with open("raw/planets.json", "a") as file:
            json.dump(data, file)

        # pega as informações da api pelas labels e transforma em lower case
        # as que não são
        name = data.get("name").lower()
        rotation_period = data.get("rotation_period").lower()
        orbital_period = data.get("orbital_period").lower()
        diameter = data.get("diameter").lower()
        climate = data.get("climate").lower()
        gravity = data.get("gravity").lower()
        terrain = data.get("terrain").lower()
        surface_water = data.get("surface_water").lower()
        population = data.get("population").lower()
        residents = data.get("residents")
        films = data.get("films")
        created = data.get("created").lower()
        edited = data.get("edited").lower()
        url = data.get("url").lower()

        # guarda os dados na estrutura pré definida por items e remove
        # os caracteres especiais
        items["name"] = re.sub(r"[^a-zA-Z0-9 ]+", '', name)
        items["rotation_period"] = re.sub(r"[^a-zA-Z0-9 ]+", '',
                                          rotation_period)
        items["orbital_period"] = re.sub(r"[^a-zA-Z0-9 ]+", '', orbital_period)
        items["diameter"] = re.sub(r"[^a-zA-Z0-9 ]+", '', diameter)
        items["climate"] = re.sub(r"[^a-zA-Z0-9 ]+", '', climate)
        items["gravity"] = re.sub(r"[^a-zA-Z0-9 ]+", '', gravity)
        items["terrain"] = re.sub(r"[^a-zA-Z0-9 ]+", '', terrain)
        items["surface_water"] = re.sub(r"[^a-zA-Z0-9 ]+", '', surface_water)
        items["population"] = re.sub(r"[^a-zA-Z0-9 ]+", '', population)
        items["residents"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', resident)
                              for resident in residents]
        items["films"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', film)
                          for film in films]
        items["created"] = re.sub(r"[^a-zA-Z0-9 ]+", '', created)
        items["edited"] = re.sub(r"[^a-zA-Z0-9 ]+", '', edited)
        items["url"] = re.sub(r"[^a-zA-Z0-9 ]+", '', url)

        # retorna os dados
        yield items
