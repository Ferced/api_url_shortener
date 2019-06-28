import random
class GeneradorUrl:
    def generarUrlAleatoria():
        #GENERA UN CODIGO DE 7 CARACTERES DE BASE64 (ELIGE UNA DE LAS 3 LISTA DE NUMEROS ASCII Y DE ESA ELIJE UNO ALEATORIO) ASI X 7
        url_corta="http://meli.st/"
        lista_ascii_aceptables=[['0','9'],['A','Z'],['a','z']]
        for i in range(7):
            numero_lista_aleatorio=random.randint(0,len(lista_ascii_aceptables)-1)
            numero_ascii=random.randint(ord(lista_ascii_aceptables[numero_lista_aleatorio][0]),ord(lista_ascii_aceptables[numero_lista_aleatorio][1]))
            url_corta+=chr(numero_ascii)
        return url_corta
