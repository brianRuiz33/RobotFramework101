from ast import Return
from lib2to3.pgen2 import driver
from time import sleep
from configs import cliente
from selenium.webdriver.common.by import By
from controladores import log_controller


class Autenticacion():
    
    # Se obtienen el driver disponible
    driver = cliente.obtener_driver()

    #Elementos de la pagina
    txtbox_usuario = "//input[@id='USERNAME']"
    txtbox_pswd = "//input[@id='PIN']"
    btn_login = "//a[@id='imgBtn0']"
    btn_guestacc = "//span[@class='guest_msg']"
    etiqueta_footer = "//p[@class='copyright_info']"

    def abrir_pagina(self, url):
        self.driver.get(url)

    def escribir_usuario(self, user_id):
        txt_usuario = self.driver.find_element(By.XPATH, self.txtbox_usuario)
        txt_usuario.send_keys(user_id)

        log_controller.log_info(f"Se inserto el user id -> {user_id}")

    def escribir_pass(self, pswd):
        txt_pswd = self.driver.find_element(By.XPATH, self.txtbox_pswd)
        txt_pswd.send_keys(pswd)

        log_controller.log_info(f"Se inserto el pswd -> {pswd}")

    def presionar_boton_login(self):
        btn_login_elements = self.driver.find_element(By.XPATH, self.btn_login)
        btn_login_elements.click()
        sleep(3)

        log_controller.log_info("Se dio click en el boton login")
       
    def presionar_boton_guest(self):
        btn_guestacc_elements = self.driver.find_element(By.XPATH, self.btn_guestacc)
        btn_guestacc_elements.click()

        log_controller.log_info("Se dio click en acceso a invitado")

    def leer_footer(self):
        elemento_footer = self.driver.find_element(By.XPATH,self.etiqueta_footer)
        texto_footer = elemento_footer.text
        return texto_footer

    #Metodos de validacion

    def validar_footer(self, texto_esperado):
        texto_actual = self.leer_footer()
        if texto_actual == texto_esperado:
            log_controller.log_correcto("El texto del footer es el que se esperaba")
        else:
            log_controller.log_incorrecto(f"El texto del footer es {texto_actual} y se esperaba {texto_esperado}")