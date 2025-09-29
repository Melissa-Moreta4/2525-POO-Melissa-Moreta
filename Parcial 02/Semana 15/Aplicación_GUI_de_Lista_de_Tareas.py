#################### Programa: Aplicación GUI de Lista de Tareas ##################

import tkinter as tk
from tkinter import messagebox, font as tkfont
from datetime import datetime

# Funciones
def añadir_tarea(event=None):  # 'event=None' permite llamarla desde un botón o un evento de teclado
    """
    Añade la tarea escrita en el Entry a la lista.
    - Captura el texto, valida que no esté vacío y lo inserta en el Listbox.
    - Asigna un color inicial (no completada).
    - Limpia el campo de entrada.
    """
    tarea = entrada_tarea.get().strip()

    if not tarea:
        messagebox.showwarning(title="Campo vacío", message="Por favor, escribe una tarea.")
        return

    # Formato de la tarea: Tarea | [Pendiente]
    tarea_con_estado = f"{tarea} | [Pendiente]"
    lista_tareas.insert(tk.END, tarea_con_estado)

    # Asignar la etiqueta de color para tareas pendientes
    lista_tareas.itemconfig(tk.END, {'fg': '#c62828'})  # Rojo para pendiente

    entrada_tarea.delete(0, tk.END)

def marcar_completada(event=None):
    """
    Marca la tarea seleccionada como completada o viceversa.
    - Cambia el texto para reflejar el estado '[Completada]' o '[Pendiente]'.
    - Cambia el color de la fuente de la tarea.
    - Permite llamarse con doble clic (event=None).
    """
    try:
        # Obtener el índice de la tarea seleccionada
        indice_seleccionado = lista_tareas.curselection()[0]

        # Obtener el texto actual y el color
        texto_actual = lista_tareas.get(indice_seleccionado)

        if "[Pendiente]" in texto_actual:
            # Marcar como completada
            nuevo_texto = texto_actual.replace("[Pendiente]", "[Completada]")
            nuevo_color = '#2e7d32'  # Verde para completada
        else:
            # Desmarcar (volver a Pendiente)
            nuevo_texto = texto_actual.replace("[Completada]", "[Pendiente]")
            nuevo_color = '#c62828'  # Rojo para pendiente

        # Actualizar la lista
        lista_tareas.delete(indice_seleccionado)
        lista_tareas.insert(indice_seleccionado, nuevo_texto)
        lista_tareas.itemconfig(indice_seleccionado, {'fg': nuevo_color})

    except IndexError:
        messagebox.showwarning(title="Selección requerida", message="Debes seleccionar una tarea para marcarla.")

def eliminar_tarea():
    """
    Elimina la tarea seleccionada de la lista.
    - Pide confirmación al usuario antes de eliminar.
    """
    try:
        indice_seleccionado = lista_tareas.curselection()[0]

        if messagebox.askyesno(title="Confirmar eliminación",
                               message="¿Estás seguro de que quieres eliminar la tarea seleccionada?"):
            lista_tareas.delete(indice_seleccionado)

    except IndexError:
        messagebox.showwarning(title="Selección requerida", message="Debes seleccionar una tarea para eliminar.")

# Ventana Principal
ventana = tk.Tk()
ventana.title("Lista de Tareas (To-Do List)")
ventana.geometry("450x500")
ventana.configure(bg="#f0f0f0")
ventana.resizable(False, False)

# Estilos
fuente_titulo = ("Helvetica", 14, "bold")
fuente_normal = ("Helvetica", 12)
fuente_lista = tkfont.Font(family="Courier", size=12)  # Fuente monoespaciada para mejor alineación en la lista

# Widgets y Contenedores
titulo = tk.Label(ventana, text="Mi Agenda de Tareas", font=fuente_titulo, bg="#f0f0f0", fg="#333")
titulo.pack(pady=15)

# Frame para la entrada de texto y el botón de añadir
frame_input = tk.Frame(ventana, bg="#f0f0f0")
frame_input.pack(pady=5, padx=10, fill='x')

entrada_tarea = tk.Entry(frame_input, font=fuente_normal, width=35)
entrada_tarea.pack(side=tk.LEFT, fill='x', expand=True, padx=(0, 5))

boton_añadir = tk.Button(
    frame_input,
    text="Añadir Tarea",
    font=("Helvetica", 10, "bold"),
    bg="#1e88e5",
    fg="white",
    command=añadir_tarea
)
boton_añadir.pack(side=tk.RIGHT)

# Frame para la lista de tareas
frame_lista = tk.Frame(ventana, bg="#fff")
frame_lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

lista_tareas = tk.Listbox(
    frame_lista,
    font=fuente_lista,
    height=15,
    selectmode=tk.SINGLE,
    bg="white",
    fg="#333",
    borderwidth=1,
    relief="solid"
)
lista_tareas.pack(fill=tk.BOTH, expand=True)

# Frame para los botones de acción
frame_botones = tk.Frame(ventana, bg="#f0f0f0")
frame_botones.pack(pady=10)

boton_completada = tk.Button(
    frame_botones,
    text="Marcar/Desmarcar",
    font=fuente_normal,
    bg="#4caf50",
    fg="white",
    width=18,
    command=marcar_completada
)
boton_completada.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar Tarea",
    font=fuente_normal,
    bg="#f44336",
    fg="white",
    width=18,
    command=eliminar_tarea
)
boton_eliminar.grid(row=0, column=1, padx=5)

# Manejo de Eventos Adicionales (Requisito)

# Evento: Pulsar ENTER en el campo de entrada llama a añadir_tarea
ventana.bind('<Return>', añadir_tarea)
# Evento: Doble clic en la lista de tareas llama a marcar_completada
lista_tareas.bind('<Double-Button-1>', marcar_completada)

ventana.mainloop()
#________________________Fin del Programa________________________________#