import sys, os
#sys.path.append("E:\\Usuarios\\mdrivets\\Documents\\RobotFramework101")
sys.path.append(os.path.join(os.getcwd()))

from robot.api.deco import keyword
from robot.api import logger
from controladores.pagina1 import PaginaUno
from controladores.autenticacion import Autenticacion


pc = PaginaUno()
ac = Autenticacion()

@keyword(name="Abrir pagina")
def abrir_pagina(url):
    pc.abrir_pagina(url)



@keyword(name="Escribir user ID")
def escribir_user_id(user_id):
    ac.escribir_usuario(user_id)
   

@keyword(name="Click boton login")
def click_boton_login():
    ac.presionar_boton_login()