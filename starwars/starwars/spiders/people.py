# Imports
import json
import os
import re
import scrapy
from ..items import StarwarsItemPerson

# Classe principal que define como a api de people sera 'crawleada'


class PeopleSpider(scrapy.Spider):
    # informações do crawler
    name = "people"
    allowed_domains = ["swapi.dev"]
    start_urls = ["https://swapi.dev/api/people/"]

    # setting para salvar o output em csv e na pasta work
    custom_settings = {
        "FEEDS": {"work/people.csv": {"format": "csv"}}
    }

    # método callback principal que faz as primeiras requisições
    def parse(self, response):
        # for de 1 a 5 para criar link para ser acessado pelo follow
        for i in range(1, 6):
            link = f"{self.start_urls[0]}{i}/?format=json"
            yield response.follow(link, callback=self.parsePeople)

    # método que pega os dados da api
    def parsePeople(self, response):
        # classe responsável por estruturar nosso dados
        items = StarwarsItemPerson()
        # carrega o json da api
        data = json.loads(response.body)
        # caminho para guardar os dados crus da api
        path = "raw"

        # criação do diretório raw, caso não exista
        if not os.path.exists(path):
            os.makedirs(path)
        # abre o json para salvar o dado cru
        with open("raw/people.json", "a") as file:
            json.dump(data, file)

        # pega as informações da api pelas labels e transforma em lower case
        # as que não são
        name = data.get("name").lower()
        height = data.get("height").lower()
        mass = data.get("mass").lower()
        hair_color = data.get("hair_color").lower()
        skin_color = data.get("skin_color").lower()
        eye_color = data.get("eye_color").lower()
        birth_year = data.get("birth_year").lower()
        gender = data.get("gender").lower()
        homeworld = data.get("homeworld").lower()
        films = data.get("films")
        species = data.get("species")
        vehicles = data.get("vehicles")
        starships = data.get("starships")
        created = data.get("created").lower()
        edited = data.get("edited").lower()
        url = data.get("url").lower()

        # guarda os dados na estrutura pré definida por items e remove
        # os caracteres especiais
        items["name"] = re.sub(r"[^a-zA-Z0-9 ]+", '', name)
        items["height"] = re.sub(r"[^a-zA-Z0-9 ]+", '', height)
        items["mass"] = re.sub(r"[^a-zA-Z0-9 ]+", '', mass)
        items["hair_color"] = re.sub(r"[^a-zA-Z0-9 ]+", '', hair_color)
        items["skin_color"] = re.sub(r"[^a-zA-Z0-9 ]+", '', skin_color)
        items["eye_color"] = re.sub(r"[^a-zA-Z0-9 ]+", '', eye_color)
        items["birth_year"] = re.sub(r"[^a-zA-Z0-9 ]+", '', birth_year)
        items["gender"] = re.sub(r"[^a-zA-Z0-9 ]+", '', gender)
        items["homeworld"] = re.sub(r"[^a-zA-Z0-9 ]+", '', homeworld)
        items["films"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', film)
                          for film in films]
        items["species"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', specie)
                            for specie in species]
        items["vehicles"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', vehicle)
                             for vehicle in vehicles]
        items["starships"] = [re.sub(r"[^a-zA-Z0-9 ]+", '', starship)
                              for starship in starships]
        items["created"] = re.sub(r"[^a-zA-Z0-9 ]+", '', created)
        items["edited"] = re.sub(r"[^a-zA-Z0-9 ]+", '', edited)
        items["url"] = re.sub(r"[^a-zA-Z0-9 ]+", '', url)

        # retorna os dados
        yield items
