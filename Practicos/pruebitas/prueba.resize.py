import PySimpleGUI as sg
from PIL import Image, ImageTk, ImageOps
import os


# formas de cambiar el formato de una imagen
# Path del proyecto
PATH_PROYECTO = os.path.dirname(os.path.abspath(__file__))
# Definir la interfaz de usuario
layout = [
    [sg.Button("Original", key="-ORIGINAL-")],
    [sg.Button("Resize", key="-RESIZE-")],
    [sg.Button("Thumbnail", key="-THUMBNAIL-")],
    [sg.Button("Fit", key="-FIT-")],
    [sg.Image(key="-IMAGE-", size=(400, 400), background_color="green")],
]

# Crear la ventana
window = sg.Window("Visor de imágenes", layout, finalize=True)

image_original = Image.open(os.path.join(PATH_PROYECTO, "tux.png"))
image_original_tk = ImageTk.Photolmage(image_original)


# Bucle principal
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Salir":
        break
    match event:
        case "-ORIGINAL-":
            window["-IMAGE-"].update(data=image_original_tk)
        case "-RESIZE-":
            image = image_original.resize((400, 400))
            window["-IMAGE-"].update(data=ImageTk.PhotoImage(image))
        # el profesor recomienda este para rezizear la foto memes
        case "-THUMBNAIL-":
            image = image_original.copy()
            image.thumbnail((400, 400))
            window["-IMAGE-"].update(data=ImageTk.PhotoImage(image))
        # el profesor recomienda este para rezizear la foto memes
        case "-FIT-":
            image = ImageOps.fit(image_original, (400, 400))
            window["-IMAGE-"].update(data=ImageTk.PhotoImage(image))
window.close()
