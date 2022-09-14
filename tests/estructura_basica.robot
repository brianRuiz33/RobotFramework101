*** Settings ***
Documentation    Comentario acerca de los tests.
Library    ../keywords/keywords_externos.py


*** Variables ***
${url}    http://10.71.46.30/CAisd/pdmweb.exe
${user_id}    65050478
${pswd}    123456
${rol}    Analistas de Nivel 1 CARE


*** Test Cases ***
Mi Test 1
    [Documentation]    Prueba de login en App CA Service Desk Manager
    Abrir pagina    ${url}
    Validar texto de footer    Copyright © 2017 Broadcom. Todos los derechos reservados. El término "Broadcom" se refiere a Broadcom Inc. y a sus subsidarias.
    Escribir user ID    ${user_id}
    Escribir PSWD    ${pswd}
    Click boton login
    #Click boton guest
    Seleccionar Rol    ${rol}
    Establecer Rol


*** Keywords ***