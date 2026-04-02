import tkinter as tk
from tkinter import messagebox

# Crear ventana principal
root = tk.Tk()
root.title("Gestor Tareas de PAÚL")
root.geometry("400x400")

# Lista para almacenar tareas
tareas = []

# Función para actualizar la lista visual
def actualizar_lista():
    listbox.delete(0, tk.END)
    for tarea, completada in tareas:
        if completada:
            listbox.insert(tk.END, "✔ " + tarea)
        else:
            listbox.insert(tk.END, "✗ " + tarea)

# Función para agregar tarea
def agregar_tarea(event=None):
    texto = entrada.get().strip()
    if texto != "":
        tareas.append((texto, False))
        entrada.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Advertencia", "Ingrese una tarea")

# Función para marcar como completada
def completar_tarea(event=None):
    seleccion = listbox.curselection()
    if not seleccion:
        return

    indice = seleccion[0]
    tarea, estado = tareas[indice]
    tareas[indice] = (tarea, True)
    actualizar_lista()

# Función para eliminar tarea (SOLO con Delete)
def eliminar_tarea(event=None):
    seleccion = listbox.curselection()
    if not seleccion:
        return

    indice = seleccion[0]
    tareas.pop(indice)
    actualizar_lista()

# Función para cerrar
def cerrar(event=None):
    root.destroy()

# Entrada de texto
entrada = tk.Entry(root, width=30)
entrada.pack(pady=10)

# Botones
btn_agregar = tk.Button(root, text="Agregar Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

btn_completar = tk.Button(root, text="Marcar como Completada", command=completar_tarea)
btn_completar.pack(pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# 🔹 Atajos de teclado
root.bind("<Return>", agregar_tarea)     # Enter
root.bind("<c>", completar_tarea)       # tecla C
root.bind("<C>", completar_tarea)
root.bind("<Delete>", eliminar_tarea)   # SOLO Delete
root.bind("<Escape>", cerrar)           # Esc

# Ejecutar aplicación
root.mainloop()