import tkinter as tk
from tkinter import messagebox

def agregar_dato():  # usage new *
    dato = entrada_dato.get().strip()
    """ Agrega el dato ingresado en el Entry a la Lista.
       - Verifica que no esté vacío.
       - Valida que sea un número (entero o decimal). """
    if not dato:
        messagebox.showwarning(title="Campo vacío", message="Por favor ingresa un número.")
        return

    try:
        valor = float(dato)
        if valor.is_integer():
            lista_datos.insert(tk.END, str(int(valor)))
        else:
            lista_datos.insert(tk.END, str(valor))
        entrada_dato.delete(first:= 0, tk.END)
    except ValueError:
        messagebox.showerror(title="Error de entrada", message="Por favor ingresa un número válido.")

def limpiar_seleccion_o_todo():  # usage new *
    """ Limpia la información de la lista o el campo de texto.
    - Si hay elementos seleccionados, se eliminan.
    - Si no hay selección, se borra toda la lista. """
    entrada_dato.delete(0, tk.END)

    seleccion = lista_datos.curselection()
    if seleccion:
        for i in reversed(seleccion):
            lista_datos.delete(i)
    else:
        lista_datos.delete(0, tk.END)

################# Ventana Principal ############################

ventana = tk.Tk()
ventana.title("Creación de una Aplicación GUI Básica")
ventana.geometry("450x400")
ventana.configure(bg="#e8f0f2")
ventana.resizable(width=False, height=False)

################## Estilos ###########################

fuente_titulo = ("Helvetica", 16, "bold")
fuente_normal = ("Helvetica", 12)

################### Widgets ###########################

titulo = tk.Label(
    ventana,
    text="Gestión de Datos Numéricos",
    font=fuente_titulo,
    bg="#e8f0f2",
    fg="green"
)
titulo.pack(pady=15)

frame_input = tk.Frame(ventana, bg="#e8f0f2")
frame_input.pack(pady=10)

etiqueta = tk.Label(frame_input, text="Dato numérico:", font=fuente_normal, bg="#e8f0f2")
etiqueta.grid(row=0, column=0, padx=5, pady=5)

entrada_dato = tk.Entry(frame_input, width=25, font=fuente_normal)
entrada_dato.grid(row=0, column=1, padx=5)

frame_botones = tk.Frame(ventana, bg="#e8f0f2")
frame_botones.pack(pady=10)

boton_agregar = tk.Button(
    frame_botones,
    text="Agregar",
    font=fuente_normal,
    bg="#d98719",
    fg="white",
    width=12,
    command=agregar_dato
)
boton_agregar.grid(row=0, column=0, padx=10)

boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    font=fuente_normal,
    bg="#856363",
    fg="white",
    width=12,
    command=limpiar_seleccion_o_todo
)
boton_limpiar.grid(row=0, column=1, padx=10)

etiqueta_lista = tk.Label(
    ventana,
    text="Datos Ingresados:",
    font=fuente_normal,
    bg="#70db93",
    fg="#222",
)
etiqueta_lista.pack(pady=10)

lista_datos = tk.Listbox(
    ventana,
    width=35,
    height=10,
    font=fuente_normal,
    bg="yellow",
    fg="#000",
    selectmode=tk.MULTIPLE
)
lista_datos.pack(pady=5)

# Ejecutar App

ventana.mainloop()

########### Fin del Programa #############