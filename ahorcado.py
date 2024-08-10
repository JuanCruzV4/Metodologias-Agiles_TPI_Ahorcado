import random

palabras_facil = [["azucar", "Se le puede agregar a la chocolatada"], ["perro", "Animal doméstico al que le gusta jugar"], ["casa", "Lugar donde vives"], ["mate", "Bebida argentina por excelencia"]]
palabras_intermedio = [["travesia", "Largo viaje o trampolín de experiencias"], ["aventura", "Viaje emocionante y arriesgado"], ["melodia", "Secuencia armoniosa de sonidos"]]
palabras_dificil = [["efimero", "Que dura por un corto periodo de tiempo"], ["magico", "Relacionado con la magia o algo extraordinario"], ["enigma", "Misterio o situación difícil de entender"]]

class Ahorcado():
    def __init__(self):
        self.palabra_vacia = ""
        self.palabra_a_adivinar = ["", ""]
        self.intentos = 7
        self.intentos_restantes = 7
        self.letras_adivinadas = []
        self.letras_usadas = []
        self.palabra_a_mostrar = []
        self.juego_finalizado = False

    def iniciar(self, dificultad=None, palabra=None, pista=None):
        self.intentos = 7
        self.letras_adivinadas = []
        self.juego_finalizado = False
        self.letras_usadas = []
        if palabra is None:
            self.palabra_a_adivinar = self.elegir_palabra(dificultad)
        else:
            self.palabra_a_adivinar[0] = palabra
        self.palabra_a_mostrar = ['_' for _ in self.palabra_a_adivinar[0]]
        self.pista = pista if pista is not None else self.palabra_a_adivinar[1] #self.pista = self.palabra_a_adivinar[1] 
        self.intentos_restantes = 7

    def validar_letra(self, letra):
        if letra in self.palabra_a_adivinar[0]:
            self.letras_adivinadas.append(letra)
            return True
        else:
            return False

    def validar_palabra(self, palabra):
        return palabra == self.palabra_a_adivinar[0]

    def intento(self, letra):
        if letra in self.letras_usadas:
            return False  # La letra ya fue usada, no hacer nada
        self.letras_usadas.append(letra)
        if self.validar_letra(letra):
            self.revelar_letra_correcta(letra)
            return True
        else:
            self.intentos_restantes -= 1
            return False

    def revelar_letra_correcta(self, letra):
        if len(self.palabra_a_adivinar[0]) != len(self.palabra_a_mostrar):
            raise ValueError("La longitud de la palabra a adivinar y la palabra a mostrar no coinciden.")
        for idx, l in enumerate(self.palabra_a_adivinar[0]):
            if l == letra:
                self.palabra_a_mostrar[idx] = letra

    def validar_fin_del_juego(self):
        if self.intentos_restantes == 0 or "".join(self.palabra_a_mostrar) == self.palabra_a_adivinar[0]:
            self.juego_finalizado = True
        return self.juego_finalizado

    def elegir_palabra(self, dificultad):
        if dificultad == 'facil':
            return random.choice(palabras_facil)
        elif dificultad == 'media':
            return random.choice(palabras_intermedio)
        else:
            return random.choice(palabras_dificil)

    def obtener_pista(self):
        return self.pista

    def letras_utilizadas(self, letra):
        if letra in self.letras_adivinadas:
            return True
        else: return False