from datetime import date
from campaña import Campaña
from anuncio import Video


video_demo = Video(1,1,"sin url", "sin url", "instream", 30)
c = Campaña("Campaña 1", date.today(), date.today(), [video_demo])


try:
    nombre = input("Ingrese nuevo nombre de la campaña: ")
    sub_tipo = input("Ingrese nuevo sub tipo del anuncio ")

    c.nombre = nombre
    c.anuncios[0].sub_tipo = sub_tipo

except Exception as e:
    with open("error.log","a+", encoding="utf-8" ) as log:
        log.write(f"Error: {e}")