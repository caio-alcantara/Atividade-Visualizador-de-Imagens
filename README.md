## Visão Geral

Este projeto implementa um **Visualizador de Imagens** em Python, com interface gráfica construída sobre a biblioteca **PySimpleGUI**. O usuário pode:

- Carregar uma imagem através de um diálogo de arquivo.
- Aplicar filtros (escala de cinza, inversão de cores, contraste, desfoque, nitidez, detecção de bordas).
- Aplicar transformações (rotação, redimensionamento).
- Visualizar lado a lado a imagem original e a imagem processada.
- Salvar o resultado em um novo arquivo.
- Reverter para a versão limpa a qualquer momento.

---

## Pré-requisitos

- Python 3.7+  
- Bibliotecas:
  - `PySimpleGUI`
  - `opencv-python`
  - `Pillow`
  - `numpy`

## Como rodar o projeto

Possuindo uma versão do Python3 instalado, clone o repositório e navegue até o diretório raíz. Na raíz, será necessário criar um ambiente virtual e instalar as bibliotecas com:

```bash
python3 -m venv venv
```


Em ambiente Ubuntu/Debian:
```bash
source venv/bin/activate
```

Em ambiente Windows:
```bash
./venv/Scripts/activate
```

Após isso, instale as bibliotecas com:

```bash
pip install -r requirements.txt
```

Com isso feito, basta rodar o arquivo python para iniciar o projeto:

```bash
python3 visualizador.py
```


## Interface Gráfica
Botões principais

* Upar Imagem: abre diálogo para seleção de arquivo de imagem.
* Aplicar Filtro: aplica o filtro ou transformação selecionado.
* Salvar Imagem: salva a imagem processada em disco.
* Limpar: reverte para a imagem original carregada.
* Combo de Filtros/Transformações
* Escala de Cinza
* Inversão de Cores
* Aumento de Contraste
* Desfoque
* Nitidez
* Detecção de Bordas
* Rotação (use o campo “Parâmetros” para ângulo em graus)
* Redimensionamento (use “Parâmetros” para fator de escala, ex.: 0.5)
* Campo Parâmetros:
    * Usado para receber valores numéricos de rotação (graus) ou escala.

## Descrição dos filtros

| Nome                 | Chamada                          | Descrição                                  |
|----------------------|----------------------------------|--------------------------------------------|
| Escala de Cinza      | `apply_grayscale(img, _)`        | Converte para tons de cinza                |
| Inversão de Cores    | `apply_invert(img, _)`           | Inverte valores de cor                     |
| Aumento de Contraste | `apply_contrast(img, _)`         | Ajusta `alpha=1.5`, `beta=0`               |
| Desfoque             | `apply_blur(img, _)`             | Aplica Gaussian Blur (5×5)                 |
| Nitidez              | `apply_sharpen(img, _)`          | Realça contornos usando mistura            |
| Detecção de Bordas   | `apply_edge_detection(img, _)`   | Canny (100, 200)                           |
| Rotação              | `apply_rotation(img, params)`    | Rotaciona em múltiplos de 90° (padrão 90)  |
| Redimensionamento    | `apply_resize(img, params)`      | Redimensiona por fator (ex.: `0.5` = 50%)  |
