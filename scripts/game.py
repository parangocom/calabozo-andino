#Proyecto juego

import os
import sys
import pygame as pg
from pygame import mixer
pg.init()

#Cargar sonidos
# Music is optional: the audio file is not distributed with this repository
# (see media/audio/README.md). If it is missing, the game runs without sound.
AUDIO_PATH=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "media", "audio", "calabozo_theme.wav")
try:
    calabozo_track=pg.mixer.Sound(AUDIO_PATH)
    calabozo_track.set_volume(.2)
except (pg.error, FileNotFoundError):
    calabozo_track=None
    print("(No se encontro la musica: el juego continua sin sonido.)")

def Instrucciones():
    # Menu inicial y controles
    print('''
    ______________________________
    CALABOZO ANDINO - Juego de rol
        
        Te tiraron al calabozo, debes escapar o enfrentar los peligros que están en tu camino. 
        Puedes navegar el espacio o recoger objetos que te ayudaran en el camino. 
        Para moverte debes escribir «ir», espacio y precisar la dirección : «norte», «sur», «este», «oeste».
        Para recoger objetos debes escribir «recoger», un espacio y precisar el objeto que quieres recoger. 
    ______________________________
    UN JUEGO DE PABLO ARANGO
    ''')

def estatus():
    print("______________________________")
    print(f"Sala actual: {sala_actual}.")
    print(f"Inventario: {inventario}.")

    if "objeto" in salas[sala_actual] and salas[sala_actual]["objeto"]:
        objeto_sala=salas[sala_actual]["objeto"]
        print(f"Puedes ver el objeto {objeto_sala}.")
    
    print("______________________________")

DIRECCIONES=("norte","sur","este","oeste")
inventario=[] 
sala_actual="El Calabozo"
salas={
    "El Calabozo" :{
        "norte": "El Pasillo",
        "objeto" : "machete"
    },
    "El Pasillo" : {
        "sur": "El Calabozo",
        "oeste": "La Torre",
        "este": "La Capilla",
        "objeto" : "aguardiente"
    },
    "La Capilla" : {
        "oeste": "El Pasillo"
    },
    "La Torre" : {
        "este": "El Pasillo",
        "sur":"El Monte",
        "objeto":"llave"
    },
    "El Monte" : {
        "norte" : "La Torre",
        "enemigo" : "Patasola"   
    }
}

Instrucciones()
if calabozo_track:
    calabozo_track.play()
#Acciones de navegacion 
while True:
    estatus()
    movimiento=input(">")
    movimiento=movimiento.split(" ", 1)
    os.system("cls" if os.name=="nt" else "clear")
    if movimiento[0]=="ir":
        if len(movimiento)<2:
            print("Debes precisar la dirección: norte, sur, este u oeste.")
        elif movimiento[1] in DIRECCIONES and movimiento[1] in salas[sala_actual]:
            sala_actual=salas[sala_actual][movimiento[1]]
            print(f"Estás en {sala_actual}.")
        else: print(f"{movimiento[1]} es inaccesible desde donde estás.")
#Acciones de inventario        
    if movimiento[0] =="recoger":
        if len(movimiento)<2:
            print("Debes precisar el objeto que quieres recoger.")
        elif salas[sala_actual].get("objeto") and movimiento[1] ==salas[sala_actual]["objeto"]:
            print(f"Tienes el objeto {movimiento[1]}.")
            inventario.append(movimiento[1])
            salas[sala_actual]["objeto"]=""
        else: print(f"No hay {movimiento[1]} aquí.")
#Condicion de victoria 1 : Escapar
    if sala_actual=="La Capilla" and "llave" in inventario and "aguardiente" in inventario:
     print("¡Escapaste del calabozo con la llave y el aguardiente!")
     print("¡Victoria!")
     break
    #Condicion de victoria 2 : Matar la Patasola
    if "enemigo" in salas[sala_actual] and salas[sala_actual]["enemigo"]=="Patasola": 
      if "machete" in inventario:
            print("La Patasola se acerca...")
            print("¡De un machetazo le tajas la cabeza!")
            print("¡Victoria!")
            break
      else : print("Te perdiste en el monte sin armas para defenderte y la Patasola te encontró...") 
      print("¡Derrota!")
      break 