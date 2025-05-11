import PySimpleGUI as sg
import cv2
from PIL import Image, ImageTk
import io
import numpy as np

current_image = None
processed_image = None
MAX_DISPLAY_SIZE = (800, 600)

## Layout da interface gráfica
left_col = [
    [sg.Text('Imagem Original')],
    [sg.Image(key='-ORIGINAL-', size=MAX_DISPLAY_SIZE)],
]

right_col = [
    [sg.Text('Imagem Processada')],
    [sg.Image(key='-PROCESSED-', size=MAX_DISPLAY_SIZE)],
]

controls = [
    sg.Button('Upar Imagem'),
    sg.Combo([
        'Escala de Cinza', 
        'Inversão de Cores', 
        'Aumento de Contraste',
        'Desfoque',
        'Nitidez',
        'Detecção de Bordas',
        'Rotação',
        'Redimensionamento'], 
        key='-FILTER-', enable_events=True),
    sg.Button('Aplicar Filtro'),
    sg.Button('Salvar Imagem'),
    sg.Button('Limpar'),
    sg.Text('Parâmetros:'),
    sg.Input(key='-PARAMS-', size=(10,1)),
]

layout = [
    [sg.Column(left_col), sg.Column(right_col)],
    [controls],
]

## Escala de cinza
def apply_grayscale(img, params):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## Inversão de cores
def apply_invert(img, params):
    return cv2.bitwise_not(img)

## Aumento de contraste
def apply_contrast(img, params):
    return cv2.convertScaleAbs(img, alpha=1.5, beta=0)

## Desfoque
def apply_blur(img, params):
    return cv2.GaussianBlur(img, (5, 5), 0)

## Nitidez
def apply_sharpen(img, params):
    return cv2.addWeighted(img, 1.5, cv2.GaussianBlur(img, (0, 0), 3), -0.5, 0)

## Detecção de bordas com Canny
def apply_edge_detection(img, params):
    return cv2.Canny(img, 100, 200)

## Rotação
def apply_rotation(img, params):
    angle = int(params) if params.isdigit() else 90
    num_rotations = angle // 90
    rotation_code = cv2.ROTATE_90_CLOCKWISE
    for _ in range(num_rotations % 4):
        img = cv2.rotate(img, rotation_code)
    return img

## Redimensionamento
def apply_resize(img, params):
    try:
        scale = float(params) if params else 0.5
    except ValueError:
        scale = 0.5
    return cv2.resize(img, (0,0), fx=scale, fy=scale)

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

## Carregar imagem
def load_image(path):
    if not path:
        sg.popup_error('Caminho da imagem não fornecido.')
        return None

    image = cv2.imread(path)
    if image is None:
        sg.popup_error('Erro ao carregar imagem. Verifique se o arquivo é válido.')
        return None

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

## converter numpy array para imagem da lib de interface
def np_to_pysimplegui(img_array):
    if img_array is None:
        return None
    display_img = resize_for_display(img_array)
    if len(display_img.shape) == 2:  # Grayscale
        display_img = cv2.cvtColor(display_img, cv2.COLOR_GRAY2RGB)
    img_pil = Image.fromarray(display_img)
    bio = io.BytesIO()
    img_pil.save(bio, format='PNG')
    return bio.getvalue()

def resize_for_display(img_array):
    if img_array is None:
        return None
        
    height, width = img_array.shape[:2] if len(img_array.shape) == 3 else img_array.shape
    ratio = min(MAX_DISPLAY_SIZE[0]/width, MAX_DISPLAY_SIZE[1]/height)
    new_width = int(width * ratio)
    new_height = int(height * ratio)
    return cv2.resize(img_array, (new_width, new_height))

window = sg.Window('Visualizador de Imagens', layout, resizable=True)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    ## Carregamento (upload) de imagem
    if event == 'Upar Imagem':
        path = sg.popup_get_file('Selecione uma imagem', 
                                file_types=(("Imagens", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff;*.webp"), 
                                ("Todos os arquivos", "*.*")))
        if path:
            current_image = load_image(path)
            if current_image is not None:
                window['-ORIGINAL-'].update(data=np_to_pysimplegui(current_image))
                processed_image = current_image.copy()
                window['-PROCESSED-'].update(data=np_to_pysimplegui(processed_image))
    
    ## Aplica filtro escolhido
    if event == 'Aplicar Filtro' and processed_image is not None:
        selected_filter = values['-FILTER-']
        if selected_filter in FILTERS:
            try:
                new_image = FILTERS[selected_filter](processed_image.copy(), values['-PARAMS-'])
                processed_image = new_image
                window['-PROCESSED-'].update(data=np_to_pysimplegui(processed_image))
                
            except Exception as e:
                sg.popup_error(f'Erro ao aplicar filtro: {str(e)}')
    
    ## Salvar imagem
    if event == 'Salvar Imagem' and processed_image is not None:
        save_path = sg.popup_get_file('Salvar imagem', save_as=True, file_types=(("PNG", "*.png"), ("JPEG", "*.jpg")))
        if save_path:
            if processed_image is not None:
                save_image = Image.fromarray(processed_image)
                if save_image:
                    save_image.save(save_path)
                    sg.popup('Imagem salva com sucesso!')
                else:
                    sg.popup_error('Erro ao converter a imagem para salvar.')
            else:
                sg.popup_error('Imagem processada não encontrada.')

    ## Limpar imagens
    if event == 'Limpar':
        processed_image = current_image.copy() if current_image is not None else None
        window['-ORIGINAL-'].update(data=np_to_pysimplegui(current_image))
        window['-PROCESSED-'].update(data=np_to_pysimplegui(processed_image))
        window['-FILTER-'].update(value='')
        window['-PARAMS-'].update(value='')

window.close()