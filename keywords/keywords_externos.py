from cgi import print_arguments
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


@keyword(name="Escribir PSWD")
def escribir_pswd(pswd):
    ac.escribir_pass(pswd)


@keyword(name="Click boton login")
def click_boton_login():
    ac.presionar_boton_login()


@keyword(name="Click boton guest")
def click_boton_guest():
    ac.presionar_boton_guest()


@keyword(name="Validar texto de footer")
def validar_texto_footer(texto_esperado):
    ac.validar_footer(texto_esperado)


@keyword(name="Seleccionar Rol")
def seleccion_rol(rol):
    ac.selecciona_rol(rol)


@keyword(name="Establecer Rol")
def establece_rol():
    ac.presionar_boton_establece_rol()