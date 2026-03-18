import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesita instalación: pip install tkcalendar

# Lista para almacenar eventos
eventos = []

# Función para agregar evento
def agregar_evento():
    fecha = date_entry.get()
    hora = entry_hora.get()
    descripcion = entry_desc.get()

    if fecha == "" or hora == "" or descripcion == "":
        messagebox.showwarning("Campos vacíos", "Por favor complete todos los campos")
        return

    # Insertar en TreeView
    tree.insert("", "end", values=(fecha, hora, descripcion))

    # Guardar en lista
    eventos.append((fecha, hora, descripcion))

    # Limpiar campos
    entry_hora.delete(0, tk.END)
    entry_desc.delete(0, tk.END)


# Función para eliminar evento
def eliminar_evento():
    seleccionado = tree.selection()

    if not seleccionado:
        messagebox.showwarning("Selección vacía", "Seleccione un evento para eliminar")
        return

    confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")

    if confirmar:
        for item in seleccionado:
            tree.delete(item)


# Función para salir
def salir():
    root.quit()


# Ventana principal
root = tk.Tk()
root.title("Agenda Personal de Paúl Pilco")
root.geometry("600x400")

# =========================
# FRAME LISTA DE EVENTOS
# =========================
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

# TreeView
tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")

tree.column("Fecha", width=100)
tree.column("Hora", width=80)
tree.column("Descripción", width=250)

tree.pack()

# =========================
# FRAME ENTRADA DE DATOS
# =========================
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Fecha
tk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
date_entry = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
date_entry.grid(row=0, column=1, padx=5, pady=5)

# Hora
tk.Label(frame_entrada, text="Hora (24h):").grid(row=1, column=0, padx=5, pady=5)

frame_hora = tk.Frame(frame_entrada)
frame_hora.grid(row=1, column=1, padx=5, pady=5)

# Spinbox para horas (00–23)
spin_hora = tk.Spinbox(frame_hora, from_=0, to=23, width=5, format="%02.0f")
spin_hora.pack(side=tk.LEFT)

tk.Label(frame_hora, text=":").pack(side=tk.LEFT)

# Spinbox para minutos (00–59)
spin_minuto = tk.Spinbox(frame_hora, from_=0, to=59, width=5, format="%02.0f")
spin_minuto.pack(side=tk.LEFT)

# Descripción
tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entry_desc = tk.Entry(frame_entrada)
entry_desc.grid(row=2, column=1, padx=5, pady=5)

# =========================
# FRAME BOTONES
# =========================
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# Ejecutar aplicación
root.mainloop()