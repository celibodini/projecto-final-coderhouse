from ejemplo.models import Celulares
Celulares(nombre="S20 FE", marca="Samsung", precio=85000).save()
Celulares(nombre="14 pro max", marca="Iphone", precio=350000).save()
Celulares(nombre="S21 FE", marca="Samsung", precio=120000).save()
Celulares(nombre="A 53", marca="Samsung", precio=60000).save()

from ejemplo_dos.models import Post

Post(titulo="Un post", sub_titulo="un sub post", texto="Un comentario", publicado_el="12/12/2022")

print("Se cargo con éxito los usuarios de pruebas")


