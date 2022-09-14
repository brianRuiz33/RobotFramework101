*** Settings ***
Documentation    Tests relacionados con la pantalla principal.
Library    ../keywords/pantalla_principal.py
Library    ../keywords/autenticacion.py



*** Variables ***
${url}    http://10.71.46.30/CAisd/pdmweb.exe
${rol_usuario}    Analista nivel 1

*** Test Cases ***
Cambiar rol de usuario
    [Documentation]    Prueba de pantalla principal
    Entrar validado al sistema
    Seleccionar Rol    ${rol_usuario}
    Establecer Rol
   


*** Keywords ***
Entrar validado al sistema
    Abrir pagina    ${url}
    Escribir user ID    65050478
    Escribir PSWD    ${EMPTY}
    Click boton login
    