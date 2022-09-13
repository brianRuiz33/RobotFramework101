import sys, os
#sys.path.append("E:\\Usuarios\\mdrivets\\Documents\\RobotFramework101")
sys.path.append(os.path.join(os.getcwd()))
from robot.api.deco import keyword
from robot.api import logger
from controladores.pagina1 import PaginaUno


pc = PaginaUno()

@keyword(name="Abrir pagina")
def abrir_pagina(url):
    pc.abrir_pagina(url)
