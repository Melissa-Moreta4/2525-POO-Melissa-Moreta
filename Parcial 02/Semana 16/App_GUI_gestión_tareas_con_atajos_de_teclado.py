#--- Programa: Aplicación GUI de Lista de Tareas con Fecha Límite y Atajos ---#

import tkinter as tk
from tkinter import messagebox, font as tkfont
from tkcalendar import DateEntry  # Importar tkcalendar

#-------------------------------------Funciones----------------------------------#
def añadir_tarea(event=None):
    """ Añade la tarea con su fecha límite a la lista. Se llama con botón o Enter. """
    tarea = entrada_tarea.get().strip()
    fecha_limite = cal_fecha_limite.get()  # Obtener la fecha del DateEntry

    if not tarea:
        messagebox.showwarning(title="Campo vacío", message="Por favor, escribe una tarea.")
        return

    # Formato de la tarea: [Fecha Límite] Tarea | [Pendiente]
    tarea_con_estado = f"[{fecha_limite}] {tarea} | [Pendiente]"
    lista_tareas.insert(tk.END, tarea_con_estado)

    # Asignar color rojo para tarea pendiente
    lista_tareas.itemconfig(tk.END, {'fg': '#c62828'})

    entrada_tarea.delete(0, tk.END)

def marcar_completada(event=None):
    """ Marca la tarea seleccionada como completada o viceversa.
    Se llama con botón o tecla 'C'. """
    try:
        # La comprobación de selección es crucial para el manejo de atajos de teclado
        if not lista_tareas.curselection():
            if not event or (event and event.keysym != 'c'):
                messagebox.showwarning(title="Selección requerida",
                                       message="Debes seleccionar una tarea para marcarla.")
            return

        indice_seleccionado = lista_tareas.curselection()[0]
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
        pass  # Manejado por la comprobación inicial

def eliminar_tarea(event=None):
    """ Elimina la tarea seleccionada de la lista. Se llama con botón o teclas 'Delete'/'D'. """
    try:
        if not lista_tareas.curselection():
            if not event or (event and event.keysym in ('d', 'Delete')):
                return
            else:
                messagebox.showwarning(title="Selección requerida",
                                       message="Debes seleccionar una tarea para eliminar.")
                return

        indice_seleccionado = lista_tareas.curselection()[0]

        if messagebox.askyesno(title="Confirmar eliminación",
                               message="¿Estás seguro de que quieres eliminar la tarea seleccionada?"):
            lista_tareas.delete(indice_seleccionado)

    except IndexError:
        pass

def cerrar_aplicacion(event=None):
    """ Cierra la aplicación. Se llama con tecla 'Escape'. """
    if messagebox.askyesno(title="Salir", message="¿Estás seguro de que quieres cerrar la aplicación?"):
        ventana.destroy()

#---------------------------Ventana Principal------------------------------#
ventana = tk.Tk()
ventana.title("Tareas con Fecha Límite y Atajos")
ventana.geometry("480x550")
ventana.configure(bg="#f0f0f0")
ventana.resizable(False, False)

# Estilos
fuente_titulo = ("Helvetica", 14, "bold")
fuente_normal = ("Helvetica", 12)
fuente_lista = tkfont.Font(family="Courier", size=10)  # Reducido un poco para caber la fecha

# Título
titulo = tk.Label(ventana, text="Gestor de Tareas con Deadline", font=fuente_titulo, bg="#f0f0f0", fg="#333")
titulo.pack(pady=10)

# Frame para la entrada de texto
frame_input = tk.Frame(ventana, bg="#f0f0f0")
frame_input.pack(pady=5, padx=10, fill='x')

# Campo Tarea
etiqueta_tarea = tk.Label(frame_input, text="Tarea:", font=fuente_normal, bg="#f0f0f0")
etiqueta_tarea.grid(row=0, column=0, padx=(0, 5), pady=5, sticky='w')
entrada_tarea = tk.Entry(frame_input, font=fuente_normal, width=30)
entrada_tarea.grid(row=0, column=1, padx=(0, 5), pady=5, sticky='ew')

# Campo Fecha Límite (DateEntry)
etiqueta_fecha = tk.Label(frame_input, text="Fecha Límite:", font=fuente_normal, bg="#f0f0f0")
etiqueta_fecha.grid(row=1, column=0, padx=(0, 5), pady=5, sticky='w')
cal_fecha_limite = DateEntry(frame_input, width=15, background="darkblue", foreground="white", borderwidth=2,
                             font=fuente_normal, date_pattern='dd/mm/yyyy')
cal_fecha_limite.grid(row=1, column=1, padx=(0, 5), pady=5, sticky='w')

# Frame para los botones de acción principales
frame_botones_add = tk.Frame(ventana, bg="#f0f0f0")
frame_botones_add.pack(pady=(0, 10))

boton_añadir = tk.Button(
    frame_botones_add,
    text="Añadir (Enter)",
    font=("Helvetica", 10, "bold"),
    bg="#1e88e5",
    fg="white",
    width=35,
    command=añadir_tarea
)
boton_añadir.pack(side=tk.LEFT)

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

# Frame para los botones de acción secundarios (Completar/Eliminar)
frame_botones_actions = tk.Frame(ventana, bg="#f0f0f0")
frame_botones_actions.pack(pady=10)

boton_completada = tk.Button(
    frame_botones_actions,
    text="Completar (C)",
    font=fuente_normal,
    bg="#4caf50",
    fg="white",
    width=18,
    command=marcar_completada
)
boton_completada.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(
    frame_botones_actions,
    text="Eliminar (Del/D)",
    font=fuente_normal,
    bg="#f44336",
    fg="white",
    width=18,
    command=eliminar_tarea
)
boton_eliminar.grid(row=0, column=1, padx=5)

#------------------------------Manejo de Atajos de Teclado------------------------------#
# Atajo: Enter para Añadir Tarea (global, pero el foco suele estar en Entry)
ventana.bind('<Return>', añadir_tarea)

# Atajo: C para Marcar/Desmarcar Tarea
ventana.bind('c', marcar_completada)
ventana.bind('C', marcar_completada)

# Atajo: Delete o D para Eliminar Tarea
ventana.bind('<Delete>', eliminar_tarea)
ventana.bind('d', eliminar_tarea)
ventana.bind('D', eliminar_tarea)

# Atajo: Escape para Cerrar Aplicación
ventana.bind('<Escape>', cerrar_aplicacion)

ventana.mainloop()
#-----------------------------Fin de Programa--------------------------------#