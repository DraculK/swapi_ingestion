# Como executar:  
Acesse o diretório principal e execute o comando `scrapy crawl planets`, `scrapy crawl films` ou `scrapy crawl people` de acordo com quais dados deseja ver o resultado.  

Na pasta `starwars/raw/`, encontram-se os jsons sem modificações, assim como eles são encontrados na swapi.  

Já na pasta `starwars/work/`, encontram-se os dados modificados, todos com lower case e sem caracteres especiais.  

Em `starwars/starwars/spiders` estão os arquivos `people.py`, `planets.py` e `films.py`, que são os arquivos nos quais os dados são acessados e crawleados.

Em `starwars/starwars/items.py` estão as classes nas quais as estruturas dos crawlers são definidas, usa-se esse arquivo para garantir que os dados ficaram nos campos corretos durante a conversão para CSV.  

Todos os arquivos estão de acordo com o style guide PEP8.
