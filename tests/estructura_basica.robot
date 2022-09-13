*** Settings ***
Documentation    Comentario acerca de los tests.
Library    ../keywords/keywords_externos.py

*** Variables ***
${url}    http://www.google.com

*** Test Cases ***
Mi Test 1
    [Documentation]    De que es el test?
    Abrir pagina    ${url}


*** Keywords ***