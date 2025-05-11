import PySimpleGUI as sg
import cv2
from PIL import Image, ImageTk
import io
import numpy as np

## Layout da interface gráfica
left_col = [
    [sg.Text('Imagem Original')],
    [sg.Image(key='-ORIGINAL-')],
]

right_col = [
    [sg.Text('Imagem Processada')],
    [sg.Image(key='-PROCESSED-')],
]

controls = [
    sg.Button('Upar Imagem'),
    sg.Combo([
        'Escala de Cinza', 
        'Inversão de Cores', 
        'Aumento de Contraste',
        'Desfoque',
        'Nitidez',
        'Detecção de Bordas (Canny)',
        'Rotação',
        'Redimensionamento'], 
        key='-FILTER-', enable_events=True),
    sg.Button('Aplicar Filtro'),
    sg.Button('Salvar Imagem'),
    sg.Text('Parâmetros:'),
    sg.Input(key='-PARAMS-', size=(10,1)),
]

layout = [
    [sg.Column(left_col), sg.Column(right_col)],
    [controls],
]
