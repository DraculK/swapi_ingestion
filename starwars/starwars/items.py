# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Classes que definem as estruturas da spiders utilizadas


class StarwarsItemPerson(scrapy.Item):
    name = scrapy.Field()
    height = scrapy.Field()
    mass = scrapy.Field()
    hair_color = scrapy.Field()
    skin_color = scrapy.Field()
    eye_color = scrapy.Field()
    birth_year = scrapy.Field()
    gender = scrapy.Field()
    homeworld = scrapy.Field()
    films = scrapy.Field()
    species = scrapy.Field()
    vehicles = scrapy.Field()
    starships = scrapy.Field()
    created = scrapy.Field()
    edited = scrapy.Field()
    url = scrapy.Field()


class StarwarsItemPlanet(scrapy.Item):
    name = scrapy.Field()
    rotation_period = scrapy.Field()
    orbital_period = scrapy.Field()
    diameter = scrapy.Field()
    climate = scrapy.Field()
    gravity = scrapy.Field()
    terrain = scrapy.Field()
    surface_water = scrapy.Field()
    population = scrapy.Field()
    residents = scrapy.Field()
    films = scrapy.Field()
    created = scrapy.Field()
    edited = scrapy.Field()
    url = scrapy.Field()


class StarwarsItemFilms(scrapy.Item):
    title = scrapy.Field()
    episode_id = scrapy.Field()
    opening_crawl = scrapy.Field()
    director = scrapy.Field()
    producer = scrapy.Field()
    release_date = scrapy.Field()
    characters = scrapy.Field()
    planets = scrapy.Field()
    starships = scrapy.Field()
    vehicles = scrapy.Field()
    species = scrapy.Field()
    created = scrapy.Field()
    edited = scrapy.Field()
    url = scrapy.Field()
