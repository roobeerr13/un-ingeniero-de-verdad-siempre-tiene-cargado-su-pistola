# main.py
import gradio as gr
from caballo.caballos import resolver_caballo
from reina.reinas import resolver_reinas
from torre_de_hanoi.hanoi import resolver_torre_de_hanoi
from utils.visualization import plot_board, plot_queens

# Función para el Salto del Caballo
def gradio_caballos(start_x, start_y, board_size):
    try:
        start_x = int(start_x)
        start_y = int(start_y)
        board_size = int(board_size)
        if start_x < 0 or start_y < 0 or board_size <= 0:
            return "Por favor, ingresa valores válidos (números positivos).", None
        texto, tablero = resolver_caballo(n=board_size, start_x=start_x, start_y=start_y)
        if tablero is None:
            return texto, None
        fig = plot_board(tablero, "Tablero del Salto del Caballo")
        return texto, fig
    except ValueError:
        return "Error: Ingresa números enteros válidos.", None

# Función para las N Reinas
def gradio_reinas(n, max_soluciones_mostrar):
    try:
        n = int(n)
        max_soluciones_mostrar = int(max_soluciones_mostrar)
        if n <= 0 or max_soluciones_mostrar <= 0:
            return "Por favor, ingresa valores positivos para el número de reinas y el máximo de soluciones a mostrar.", None
        texto, tablero = resolver_reinas(n=n, max_soluciones_mostrar=max_soluciones_mostrar)
        if tablero is None:
            return texto, None
        fig = plot_queens(tablero, "Tablero de N Reinas (Primera Solución)")
        return texto, fig
    except ValueError:
        return "Error: Ingresa números enteros válidos.", None

# Función para las Torres de Hanoi
def gradio_hanoi(n):
    try:
        n = int(n)
        if n <= 0:
            return "Por favor, ingresa un número positivo de discos."
        texto = resolver_torre_de_hanoi(n=n)
        return texto
    except ValueError:
        return "Error: Ingresa un número entero válido."

# Crear las interfaces individuales para cada pestaña
caballos_interface = gr.Interface(
    fn=gradio_caballos,
    inputs=[
        gr.Number(label="Coordenada X inicial", value=0),
        gr.Number(label="Coordenada Y inicial", value=0),
        gr.Number(label="Tamaño del tablero", value=5),
    ],
    outputs=[
        gr.Textbox(label="Resultado"),
        gr.Image(label="Tablero")
    ],
    title="Problema del Salto del Caballo"
)

reinas_interface = gr.Interface(
    fn=gradio_reinas,
    inputs=[
        gr.Number(label="Número de Reinas (N)", value=4),
        gr.Number(label="Máximo de soluciones a mostrar", value=3),
    ],
    outputs=[
        gr.Textbox(label="Resultado"),
        gr.Image(label="Tablero (Primera Solución)")
    ],
    title="Problema de las N Reinas"
)

hanoi_interface = gr.Interface(
    fn=gradio_hanoi,
    inputs=gr.Number(label="Número de discos", value=3),
    outputs=gr.Textbox(label="Pasos"),
    title="Torres de Hanoi"
)

# Combinar todas las interfaces en una interfaz con pestañas
tabbed_interface = gr.TabbedInterface(
    interface_list=[
        caballos_interface,
        reinas_interface,
        hanoi_interface
    ],
    tab_names=[
        "Salto del Caballo",
        "N Reinas",
        "Torres de Hanoi"
    ],
    title="Solucionador de Problemas Clásicos"
)

# Lanzar la interfaz
if __name__ == "__main__":
    tabbed_interface.launch()