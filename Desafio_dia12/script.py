import json
from usuario import Usuario
from datetime import datetime


instancias = []
with open("usuarios.txt") as usuarios:
        linea = usuarios.readline()
        while linea:
            try: 
                usuario = json.loads(linea)
                instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
            except Exception as e:
                with open("error.log", "a+") as log:
                     log.seek(0)
                     print(log.read())
                     now = datetime.now()
                     log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] Error: {e}\n")
                     log.seek(0)
                     print(log.read())
            finally:
                linea = usuarios.readline()


for i in instancias:
    print(i)