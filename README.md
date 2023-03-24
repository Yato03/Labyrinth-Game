# Labyrinth-Game

## Descripción
Juego simple de puzzles donde controlas una bola roja y tu objetivo es llegar al cuadrado azul.

## Instalación

- Primero clona el repositorio
```bash
$ git clone https://github.com/Yato03/Labyrinth-Game.git
```
- Instala pygame
```bash
$ pip install pygame
```
**Cuidado!!: debes de tener python3 instalado -> https://www.python.org/downloads/**
- Por ultimo, ejecuta main.py
```bash
$ python main.py
```
También puede ser tu caso:
```
$ python3 main.py
```
## Añade niveles
Puedes crear tus propios niveles creando un archivo de texto en la carpeta levels. Para ello deberás de tener las siguientes consideraciones:
- El archivo se deberá de llamar ```levels[n].txt``` donde **n** es el número del nivel. Cada nivel saldrá en orden desde el 1 hasta el máximo número de niveles.
- El archivo está divido en 4 líneas:
  - En la línea **1** se indican las coordenadas donde hay un ***obstáculos vertical*** justo a la derecha.
  - En la línea **2** se indican las coordenadas donde hay un ***obstáculos horizontal*** justo abajo.
  - En la línea **3** se indica primero la coordenada donde aparece el ***jugador*** y luego la coordenada del ***objetivo***
  - En la línea **4** se indica el número de casillas que tendrá el tablero
  
 ```Cuidado!!: las coordenadas están invertidas. La primera es la _y_ y luego la _x_```
- Por último deberás de cambiar en el archivo main.py la variable _num_levels_ que se encuentra en la línea **22** al número de niveles actuales que tenga el juego.


## Imágenes

### Level 1
![level1](https://github.com/Yato03/Labyrinth-Game/blob/main/img/level1.PNG)

### End
![end](https://github.com/Yato03/Labyrinth-Game/blob/main/img/end.PNG)
