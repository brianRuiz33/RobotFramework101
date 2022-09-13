from robot.api.deco import keyword
from robot.api import logger
from controladores.pagina1 import PaginaUno


pc = PaginaUno()

@keyword(name="Abrir pagina")
def abrir_pagina(url):
    pc.abrir_pagina(url)
