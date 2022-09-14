*** Settings ***
Documentation    Tests relacionados con la pantalla principal.
Library    ../keywords/pantalla_principal.py
Library    ../keywords/autenticacion.py



*** Variables ***
${url}    http://10.71.46.30/CAisd/pdmweb.exe
${rol_usuario}    Analistas de nivel 1 NOC

*** Test Cases ***
Crear ticket de incidente como Analista NOC
    [Documentation]    Prueba de pantalla principal
    Entrar validado al sistema como analista NOC
    

Crear ticket de incidente como Analista CARE
    [Documentation]    Prueba de pantalla principal
    Entrar validado al sistema como analista CARE


*** Keywords ***
Entrar validado al sistema como analista NOC
    Abrir pagina    ${url}
    Escribir user ID    65063283
    Escribir PSWD    ${EMPTY}
    Click boton login
    Seleccionar Rol    Analistas de nivel 1 NOC
    Establecer Rol
    Crear Nuevo Incidente

Entrar validado al sistema como analista CARE
    Abrir pagina    ${url}
    Escribir user ID    65034718
    Escribir PSWD    ${EMPTY}
    Click boton login
    Seleccionar Rol    Analistas de nivel 1 CARE
    Establecer Rol
    Crear Nuevo Incidente
    Cliente id    BANAMEX IWAN
