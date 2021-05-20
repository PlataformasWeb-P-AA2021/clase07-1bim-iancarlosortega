from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_tablas import Club
from genera_tablas import Jugador

import json

# se importa información del archivo configuracion
from configuracion import cadena_base_datos

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)


Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de clubes

archivo_clubs = open("data/datos_clubs.txt", "r", encoding="utf-8")

clubs = archivo_clubs.readlines()

# leer el archivo de jugadores

archivo_jugadores = open("data/datos_jugadores.txt", "r", encoding="utf-8")

jugadores = archivo_jugadores.readlines()

#Se crea objetos de tipo Club

for club in clubs:
    club_array = club.split('\n');
    club_array = club_array[0].split(';');
    c = Club(nombre=club_array[0], deporte=club_array[1], fundacion=club_array[2])
    session.add(c)

# Obtener todos los registros de la entidad Club
consulta_clubs = session.query(Club).all()

#Se crea objetos de tipo Jugador

for jugador in jugadores:
    jugador_array = jugador.split('\n');
    jugador_array = jugador_array[0].split(';');


    # Se asigna el id del club de acuerdo al jugador
    for club in consulta_clubs:
        if(jugador_array[0] == club.nombre):
            id_club = club.id

    j = Jugador(nombre=jugador_array[3], dorsal=jugador_array[2], posicion=jugador_array[1], club_id=id_club)
    session.add(j)

# confirmar transacciones

session.commit()
