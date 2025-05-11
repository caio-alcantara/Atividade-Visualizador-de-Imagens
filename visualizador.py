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

def apply_grayscale(img, params):
    return img

def apply_invert(img, params):
    return img

def apply_contrast(img, params):
    return img

def apply_blur(img, params):
    return img

def apply_sharpen(img, params):
    return img

def apply_edge_detection(img, params):
    return img

def apply_rotation(img, params):
    return img

def apply_resize(img, params):
    return img

FILTERS = {
    'Escala de Cinza': apply_grayscale,
    'Inversão de Cores': apply_invert,
    'Aumento de Contraste': apply_contrast,
    'Desfoque': apply_blur,
    'Nitidez': apply_sharpen,
    'Detecção de Bordas': apply_edge_detection,
    'Rotação': apply_rotation,
    'Redimensionamento': apply_resize,
}

