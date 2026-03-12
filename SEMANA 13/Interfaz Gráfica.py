import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos")
ventana.geometry("400x350")


# ----- FUNCIONES -----

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()

    if dato != "":
        lista_datos.insert(tk.END, dato)
        entrada_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato primero")


# Función para limpiar el campo de texto
def limpiar_texto():
    entrada_texto.delete(0, tk.END)


# Función para eliminar elemento seleccionado
def eliminar_seleccion():
    seleccion = lista_datos.curselection()

    if seleccion:
        lista_datos.delete(seleccion)
    else:
        messagebox.showinfo("Información", "Seleccione un elemento de la lista")


# ----- COMPONENTES GUI -----

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto
entrada_texto = tk.Entry(ventana, width=30)
entrada_texto.pack()

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_texto)
boton_limpiar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Botón eliminar seleccionado
boton_eliminar = tk.Button(ventana, text="Eliminar seleccionado", command=eliminar_seleccion)
boton_eliminar.pack()

# Ejecutar la aplicación
ventana.mainloop()