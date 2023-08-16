import PIL.Image
import PIL.ImageTk
import PIL.ImageOps
import PIL.ImageDraw

IMAGE_SIZE = 400, 400

# Crea una imagen nueva (se puede especificar también el color de fondo]
collage = PIL.Image.new("RGB", IMAGE_SIZE)

# Cargo unas imagenes para el ejemplo
lagos = [
    PIL.Image.open(archivo)
    for archivo in ("huechulafquen. jpg", "lacar.jpg", "lacar2.jpg")
]
# devuelve el tamaño de la imagen
lagos[0].size

# para posicionar imagenes  en una caja de 400x400 debemos tener en cuenta que
# siempre se toma como punto cardinal 0,0 el extremo superior izq de la caja.
# de manera tal que si queremos poner dos imagenes en una caja dividida a la
# mitad verticalmente, ambas imagenes primero deberiamos cambiarle el formato
# a 200,400# y luego pegarlas en las coordendas  0,0 oara la primer imagen y
# 200,0 para la segunta.  (X,Y) ANCHO Y ALTO

# 1- armamos la imagen que debemos pegar en funcion de la caja que elegimos.
# en la clase se usa de ejemplo un layout que tiene 3 imagenes, 1 de 200,400
# en el lado derecho, una subdivisiom vertical a la mitad, y la segunda
# parte es una subdivision horizontal a la mitad (apto para dos fotos de
# 200,200).

huechu = PIL.ImageOps.fit(lagos(0), (200, 400))
# 2- agregamos la imagen al collage)
collage.paste(huechu, (0, 0))
# 3- repetimos pasos para las otras 2 imagenes
lacar = PIL.ImageOps.fit(lagos[1], (200, 200))
collage.paste(lacar, (200, 0))
lacar2 = PIL.ImageOps.fit(lagos[2], (200, 200))
collage.paste(lacar2, (200, 200))

# 4- Ponemos titulo a la imagen tiene una tipografia y tamaño por defecto,
# con fill nos cambia el color lo podemos poner como HEXA o la palabra en
# ingles. Tener en cuenta que cuando escribimos el usuario esta modificando
# la imagen original lo cual no esta bueno, ya que si pone un texto y luego
# lo cambia, se superpone lo escrito, para ello tenemos que trabajar con
# copias de la imagen.
collageC = collage.copy()
draw = PIL.ImageDraw.Draw(collageC)
# HACER UN PATH A LA FUENTE ROBOTO BOLD
fuente = PIL.ImageFont.truetype("fuentes/Neucha-Regular.ttf", 80)
draw.text((10, 382), "Lagos y montanas", fill="red", font=fuente)

# guardado de imagenes
collageC.save("img/collage.jpg")
# para que no de fallo siempre es mejor converir la imagen resultante a RGB
# para asegurarnos que no se rompa
collageC.convert(mode="RGB").save("img/collage.jpg")
PIL.Image.open("img/collage.jpg")


# para ver las imagenes debemos cargar del archivo CSV todas las imagenes
# que tenemos tageadas a una lista de diccionario (para usar como clave el
# nombre y despripcion ), con el nombre del archivo podemos
