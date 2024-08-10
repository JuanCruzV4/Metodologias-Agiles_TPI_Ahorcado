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
    