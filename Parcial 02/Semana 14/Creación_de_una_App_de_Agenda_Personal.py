#============Programa: Creación de una Aplicación de Agenda Personal=============

import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry

def agregar_evento():
    """ Agrega un nuevo evento a la lista (TreeView) de la agenda.
    - Captura la fecha, hora y descripción de los campos de entrada.
    - Valida que la descripción no esté vacía.
    - Inserta el evento en el TreeView.
    - Limpia los campos de entrada."""
    fecha = cal.get_date()
    hora = entrada_hora.get().strip()
    descripcion = entrada_descripcion.get().strip()

    if not descripcion:
        messagebox.showwarning(title="Campo vacío", message="La descripción del evento no puede estar vacía.")
        return

    # Validar formato de hora (opcional, pero buena práctica)
    if not hora:
        hora = "Sin hora"

    # Insertar el evento en el TreeView
    agenda_tree.insert("", tk.END, values=(fecha, hora, descripcion))

    # Limpiar los campos después de agregar
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)

def eliminar_evento():
    """
    Elimina los eventos seleccionados del TreeView.
    - Pide confirmación antes de eliminar.
    - Elimina uno o varios elementos seleccionados.
    """
    seleccionado = agenda_tree.selection()
    if not seleccionado:
        messagebox.showwarning(title="No seleccionado", message="Selecciona un evento para eliminar.")
        return

    if messagebox.askyesno(title="Confirmar eliminación",
                           message="¿Estás seguro de que quieres eliminar los eventos seleccionados?"):
        for item in seleccionado:
            agenda_tree.delete(item)

def salir_app():
    """
    Cierra la aplicación.
    - Pide confirmación antes de salir.
    """
    if messagebox.askyesno(title="Salir", message="¿Estás seguro de que quieres salir?"):
        ventana.destroy()

#____________Ventana Principal_______________

ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("600x500")
ventana.configure(bg="#e8f0f2")
ventana.resizable(False, False)

style = ttk.Style()
style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
style.configure("Treeview", font=("Helvetica", 10))

fuente_titulo = ("Helvetica", 16, "bold")
fuente_normal = ("Helvetica", 12)

#_____________Widgets y Contenedores________________

# Frame principal para los campos de entrada
frame_input = tk.Frame(ventana, bg="#e8f0f2")
frame_input.pack(pady=10)

etiqueta_titulo = tk.Label(frame_input, text="Agenda Personal", font=fuente_titulo, bg="#e8f0f2", fg="#222")
etiqueta_titulo.grid(row=0, columnspan=2, pady=10)

etiqueta_fecha = tk.Label(frame_input, text="Fecha:", font=fuente_normal, bg="#e8f0f2")
etiqueta_fecha.grid(row=1, column=0, padx=5, pady=5, sticky="w")
cal = DateEntry(frame_input, width=20, background="darkblue", foreground="white", borderwidth=2, font=fuente_normal)
cal.grid(row=1, column=1, padx=5, pady=5)

etiqueta_hora = tk.Label(frame_input, text="Hora:", font=fuente_normal, bg="#e8f0f2")
etiqueta_hora.grid(row=2, column=0, padx=5, pady=5, sticky="w")
entrada_hora = tk.Entry(frame_input, font=fuente_normal, width=23)
entrada_hora.grid(row=2, column=1, padx=5, pady=5)

etiqueta_descripcion = tk.Label(frame_input, text="Descripción:", font=fuente_normal, bg="#e8f0f2")
etiqueta_descripcion.grid(row=3, column=0, padx=5, pady=5, sticky="w")
entrada_descripcion = tk.Entry(frame_input, font=fuente_normal, width=23)
entrada_descripcion.grid(row=3, column=1, padx=5, pady=5)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#e8f0f2")
frame_botones.pack(pady=10)

boton_agregar = tk.Button(
    frame_botones,
    text="Agregar Evento",
    font=fuente_normal,
    bg="#4caf50",
    fg="white",
    command=agregar_evento
)
boton_agregar.grid(row=0, column=0, padx=5)

boton_eliminar = tk.Button(
    frame_botones,
    text="Eliminar Evento",
    font=fuente_normal,
    bg="#f44336",
    fg="white",
    command=eliminar_evento
)
boton_eliminar.grid(row=0, column=1, padx=5)

boton_salir = tk.Button(
    frame_botones,
    text="Salir",
    font=fuente_normal,
    bg="#555",
    fg="white",
    command=salir_app
)
boton_salir.grid(row=0, column=2, padx=5)

# Frame y Treeview para la lista de eventos
frame_lista = tk.Frame(ventana, bg="#e8f0f2")
frame_lista.pack(pady=10, fill=tk.BOTH, expand=True)

columnas = ("fecha", "hora", "descripcion")
agenda_tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")
agenda_tree.heading("fecha", text="Fecha")
agenda_tree.heading("hora", text="Hora")
agenda_tree.heading("descripcion", text="Descripción")

agenda_tree.column("fecha", width=100, anchor="center")
agenda_tree.column("hora", width=80, anchor="center")
agenda_tree.column("descripcion", width=300)

agenda_tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
#Ejecutar App

ventana.mainloop()
#____________________Fin del Programa___________________________