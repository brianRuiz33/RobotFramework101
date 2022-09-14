import sys, os
#sys.path.append("E:\\Usuarios\\mdrivets\\Documents\\RobotFramework101")
sys.path.append(os.path.join(os.getcwd()))

from robot.api.deco import keyword
from robot.api import logger
from controladores.pantalla_principal import PantallaPrincipal

ppc = PantallaPrincipal()

@keyword(name="Seleccionar Rol")
def seleccion_rol(rol):
    ppc.selecciona_rol(rol)


@keyword(name="Establecer Rol")
def establece_rol():
    ppc.presionar_boton_establece_rol()