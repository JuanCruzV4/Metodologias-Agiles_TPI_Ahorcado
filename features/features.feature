Feature: Juego de Ahorcado

  Scenario: Elegir dificultad fácil
      Given launch chrome browser
      When  Ingreso a la pagina del juego
      Then  el usuario elige la dificultad "facil"
      And el numero de intentos debe ser 7

  Scenario: Validar letra correcta
      Given un juego de Ahorcado con la palabra "aventura", "Viaje emocionante y arriesgado"
      When valido la letra "a"
      Then la letra es correcta
      And el numero de intentos restantes debe ser 7
      And la letra "a" esta en la lista de letras usadas

  Scenario: Validar letra incorrecta
      Given un juego de Ahorcado con la palabra "efimero", "Que dura por un corto periodo de tiempo" para validar letra incorrecta
      When valido la letra "z" incorrecta
      Then la letra es incorrecta
      And el numero de intentos debe ser 6 
      And la letra "z" esta en letras usadas

  Scenario: Ganar Juego
      Given un juego del Ahorcado con la palabra "magico", "Relacionado con la magia o algo extraordinario"
      When valido las letras "a" "m" "g" "i" "c" "o"
      Then gano la partida

 



