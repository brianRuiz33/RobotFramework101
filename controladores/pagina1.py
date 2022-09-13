from configs import cliente

class PaginaUno():

    driver = cliente.obtener_driver()

    def abrir_pagina(self, url):
        self.driver.get(url)