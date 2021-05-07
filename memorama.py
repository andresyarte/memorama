# Andrés Adrian Yarte Villaseñor - A00829535

# En esta actividad creamos un memograma, aprendi mas sobre como utilizar turtle para
# crear figuras y juegos. Tambien como agregar una foto a el programa. No entendia muy bien 
# como funcionaba agregar texto y escoger en donde desplegarlo con la (x,y). Tambien algo
# que vi nuevo aqui fue crear la lista de tiles donde cada palabra dentro de esta tendria 
# un espacio designado. Al agregar el imput del cursor se checa el primer tile con el segundo
# y si es el mismo se muestra parte de la imagen de atras.

# Link a el Video
# https://youtu.be/hMym2EBrwzU

# 7 - Mayo - 2021

from random import *
from turtle import *
from freegames import path

# Return full path fo 'filename' in freegames module 
car = path('car.gif')

# Genera una lista de 0..31 y la replica para formar pares, total de 64 cartas
tiles = list(range(32)) * 2
tiles = 'A-B-C-D-E-F-G-H-I-J-K-L-M-N-O-P-Q-R-S-T-V-W-X-Y-Z-AA-BB-CC-DD-EE-GG-PP'
tiles = tiles.split('-')
tiles = ['Pizza','Sopa','Sandwich','Pasta','Manzana','Pera','Milanesa','Jamón','Platano','HotPocket','Torta','Tomate','Pollo','Ensalada','Esparrago','Sandia','Melon','Huevo','Salchicha','Salsa','Tostada','Quesadilla','Tocino','Cebolla','Jalapeño','Kiwi','Pescado','Camaron','Pulpo','Sushi','Arroz','Edamame'] # nombres
tiles = tiles * 2
print(tiles)
taps = 0
writer = Turtle(visible = False)

#  El estado inicial del juego es que no tenemos carta visible 
state = {'mark': None}
# crea una lista indicando que las 64 cartas eestan ocultas
hide = [True] * 64
ancho = 50 


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('red', 'cyan')
    begin_fill()
    for count in range(4):
        forward(ancho)
        left(90)
    end_fill()

# Igual que en pacman solo que ahora cada cuadro es de ancho 50y son 8 x 8 = 64 celdas 
# retorna el indice correspondiente a (x,y) a una posicion de la carta en la lista
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // ancho + ((y + 200) // ancho) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * ancho - 200, (count // 8) * ancho - 200

def tap(x, y):
    global mark, taps

    #imprime las coordenadas donde se dio click
    print(x,y)

    taps = taps + 1

    "Update mark and hidden tiles based on tap."
    # retorna el indice correspondiente a (x,y) en tiles[spot]
    spot = index(x, y)

    # saca el valor de state - al iniio es none (no hay ninguna carta destapada)
    mark = state['mark']

    ''' si el mark es none o si mark == sopot el usuario dio click en la misma carta al indice sobre el 
        el ucuario dio click o si la carta que ya esta marcada es difernete de la selecionada
    '''
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # el estado ahora cambia a la carta donde el usuario dio click
        state['mark'] = spot
    else:
        # quiere decir que son pares - las hace visible 
        hide[spot] = False
        hide[mark] = False
        # vuelve mark a none - que no tenemos una carta visible
        state['mark'] = None

def draw():
    global mark
    "Draw image and tiles."
    # Limpia toda la ventana
    clear()

    # Mueve el turtle a la posicion 0,0
    goto(0, 0)

    # Carga la imagen del auto en le turtle shape
    shape(car)

    # Stamp a copy of the turtle shape into the canvas at the current turtle position
    # Dibuja el auto, el centro de la imagen(foto) se pone en la coordenada 
    # donde esta la turtle
    stamp()

    # Dibuja las 64 cartas de la memorama (tapando la imagen del auto)
    # inicialmente todas las cartas estan escondidas
    contador = 0
    for count in range(64):
        # Si todavia no esta descubierta la carta su valor sera true
        if hide[count]:
            # calcula su equivalencia en el tablero igual que en pacman
            x, y = xy(count)
            # Dibuja un square en la posición x,y
            square(x, y)
            # dibuja el valor de la casilla
            # write(f'{count}', font=('Arial', 30, 'normal'))
            contador = contador + 1

        # que pasa si hide[count] == False? NO LO DIBUJA

    # Que almacena state?
    #   None - significa que no hay carta visible 
    #   #### - indix de la carta visible
    mark = state['mark']

    # Despliega la carta donde se dio el click siempre y cuando no este visible
    # Si el estado no es None y esa carta no esta descubierta
    if (mark is not None) and (hide[mark] == True):
    #if mark is not None and hide[mark]: (es igual)
        # calcula la posicion x,y de la carta
        x, y = xy(mark)
        # levanta el lapiz
        up()
        # mueve el turtle a la posición x+2, y
        goto(x + 2, y + 20)
        # cambia el color del lapiz
        color('black')
        # despliega en esa posicion x+2, y el numero de la carta oculta
        write(tiles[mark], font=('Arial', 11, 'normal'))
    
    # Verificar si ya logro encontrar todos los pares
    escondidas = hide.count(True)

    print('Sin encontrar = ', escondidas)
    print('Sin encontrar = ', contador)
    if escondidas == 0:
        up()
        goto(-190,100)
        color('white')
        write('GANASTE UN AUTO, FELICIDADES!! \nSON MUY AFORTUNADOS', font=('Arial', 20, 'normal'))
        up()
        goto(-190,50)
        write(f'Hiciste {taps} taps', font=('Arial', 15,'normal'))
        nombres()
        return

    # muestra en la ventan lo dibujado
    update()
    # vuelve a llamar la funcion draw() en 10 seg
    ontimer(draw, 100)

def nombres():
    writer.up()
    writer.goto(-140,170)
    writer.color('black')
    writer.write('Andrés Adrián Yarte Villaseñor', font = ('Arial', 20, 'normal'))
# revolver las cartas de la memorama - 
#shuffle(tiles)
setup(420,420, 0, 0)
addshape(car)
hideturtle()
tracer(False)
# Detectar eventos del mouse
onscreenclick(tap)
draw()
done()