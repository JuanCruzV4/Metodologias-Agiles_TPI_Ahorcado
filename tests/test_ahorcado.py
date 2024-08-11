from ahorcado import *

def test_letra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar[0] = "hamaca"
    assert juego.validar_letra("a") == True
    
def test_letra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "hamaca"
    assert juego.validar_letra("e") == False
    
def test_palabra_correcta():
    juego = Ahorcado()
    juego.palabra_a_adivinar[0] = "hamaca"
    assert juego.validar_palabra("hamaca") == True
    
def test_palabra_incorrecta():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "hamaca"
    assert juego.validar_palabra("calesita") == False
    


def test_iniciar_jugada():
    juego = Ahorcado()
    assert juego.intentos == 7
    assert juego.intentos_restantes == 7
    assert juego.letras_adivinadas == []


def test_intento_pass():
    juego = Ahorcado()
    juego.iniciar(palabra="esponja") 
    assert juego.intento("e") == True
    assert juego.letras_adivinadas == ["e"]
    assert juego.intentos_restantes == 7
    
def test_intento_fail():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "esponja"
    assert juego.intento("z") == False
    assert juego.letras_adivinadas == []
    assert juego.intentos_restantes == 6


def test_letras_utili():
    juego = Ahorcado()
    juego.letras_adivinadas.append("a")
    assert juego.letras_utilizadas("a") == True



def test_estado_del_juego():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "perro"
    juego.validar_letra('p')
    juego.validar_letra('e')
    assert juego.validar_fin_del_juego() == False

def test_juego_terminado_ganador():
    juego = Ahorcado()
    juego.iniciar(palabra="perro") 
    juego.intento("p")
    juego.intento("e")
    juego.intento("r")
    juego.intento("r")
    juego.intento("o")
    assert juego.validar_fin_del_juego() == True

def test_juego_terminado_perdedor():
    juego = Ahorcado()
    juego.palabra_a_adivinar = "gato"
    juego.intento("q")
    juego.intento("w")
    juego.intento("y") 
    juego.intento("m")
    juego.intento("z")
    juego.intento("x")
    juego.intento("i")
    assert juego.validar_fin_del_juego() == True

def test_elegir_palabra_facil():
    juego = Ahorcado()
    palabra = juego.elegir_palabra(dificultad='facil')
    assert palabra in palabras_facil  

def test_elegir_palabra_media():
    juego = Ahorcado()
    palabra = juego.elegir_palabra(dificultad='media')
    assert palabra in palabras_intermedio  

def test_elegir_palabra_dificil():
    juego = Ahorcado()
    palabra = juego.elegir_palabra(dificultad='dificil')
    assert palabra in palabras_dificil 

def test_elegir_palabra_otra_dificultad():
    juego = Ahorcado()
    palabra = juego.elegir_palabra(dificultad='otra')
    assert palabra in palabras_dificil  

def test_iniciar_con_dificultad():
    juego = Ahorcado()
    juego.iniciar(dificultad='facil')
    assert juego.palabra_a_adivinar in palabras_facil  
    assert len(juego.palabra_a_mostrar) == len(juego.palabra_a_adivinar[0])  
    assert juego.intentos_restantes == 7  
    assert not juego.juego_finalizado  

def test_iniciar_con_palabra_directa():
    juego = Ahorcado()
    palabra = "mate"
    pista = "Bebida argentina por excelencia"
    juego.iniciar(palabra=palabra, pista=pista)
    assert juego.palabra_a_adivinar[0] == palabra 
    assert juego.obtener_pista() == pista  
    assert len(juego.palabra_a_mostrar) == len(palabra) 
    assert juego.intentos_restantes == 7  
    assert not juego.juego_finalizado  

def test_obtener_pista():
    juego = Ahorcado()
    pista = "Bebida argentina por excelencia"
    juego.iniciar(palabra="mate", pista=pista)
    assert juego.obtener_pista() == pista  

def test_letras_utilizadas():
    juego = Ahorcado()
    juego.iniciar(palabra="casa")
    juego.intento("a")  
    assert juego.letras_utilizadas("a") == True  
    assert juego.letras_utilizadas("c") == False  




    