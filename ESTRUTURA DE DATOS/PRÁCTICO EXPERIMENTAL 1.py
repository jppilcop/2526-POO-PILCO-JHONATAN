from tkinter import *
from tkinter import ttk, messagebox

# Lista para almacenar los socios
socios = []


# Clase Socio
class Socio:
    def __init__(self, codigo, nombre, cargo, aporte):
        self.codigo = codigo
        self.nombre = nombre
        self.cargo = cargo
        self.aporte = aporte


# Función para registrar socio
def registrar_socio():
    codigo = txt_codigo.get()
    nombre = txt_nombre.get()
    cargo = txt_cargo.get()
    aporte = txt_aporte.get()

    if codigo == "" or nombre == "" or cargo == "" or aporte == "":
        messagebox.showwarning("Aviso", "Complete todos los campos")
        return

    socio = Socio(codigo, nombre, cargo, float(aporte))
    socios.append(socio)

    tabla.insert("", END, values=(codigo, nombre, cargo, aporte))

    txt_codigo.delete(0, END)
    txt_nombre.delete(0, END)
    txt_cargo.delete(0, END)
    txt_aporte.delete(0, END)

    messagebox.showinfo("Éxito", "Socio registrado correctamente")


# Función para calcular total
def total_aportes():
    total = 0

    for socio in socios:
        total += socio.aporte

    lbl_total.config(text=f"Total aportes: ${total:.2f}")


# Ventana principal
ventana = Tk()
ventana.title("Registro de Aportes")
ventana.geometry("700x500")

# Título
titulo = Label(
    ventana,
    text="REGISTRO DE APORTES DE EMPLEADOS",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Frame de datos
frame_datos = Frame(ventana)
frame_datos.pack()

Label(frame_datos, text="Código").grid(row=0, column=0, padx=5, pady=5)
txt_codigo = Entry(frame_datos)
txt_codigo.grid(row=0, column=1)

Label(frame_datos, text="Nombre").grid(row=1, column=0, padx=5, pady=5)
txt_nombre = Entry(frame_datos)
txt_nombre.grid(row=1, column=1)

Label(frame_datos, text="Cargo").grid(row=2, column=0, padx=5, pady=5)
txt_cargo = Entry(frame_datos)
txt_cargo.grid(row=2, column=1)

Label(frame_datos, text="Aporte").grid(row=3, column=0, padx=5, pady=5)
txt_aporte = Entry(frame_datos)
txt_aporte.grid(row=3, column=1)

# Botón registrar
btn_registrar = Button(
    ventana,
    text="Registrar Socio",
    command=registrar_socio
)
btn_registrar.pack(pady=10)

# Tabla
tabla = ttk.Treeview(
    ventana,
    columns=("Codigo", "Nombre", "Cargo", "Aporte"),
    show="headings"
)

tabla.heading("Codigo", text="Código")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Cargo", text="Cargo")
tabla.heading("Aporte", text="Aporte")

tabla.pack(pady=10)

# Botón total
btn_total = Button(
    ventana,
    text="Calcular Total de Aportes",
    command=total_aportes
)
btn_total.pack(pady=10)

lbl_total = Label(
    ventana,
    text="Total aportes: $0.00",
    font=("Arial", 12, "bold")
)
lbl_total.pack()

ventana.mainloop()