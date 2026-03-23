import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas de PAÚL")

        # Lista interna de tareas (texto, estado)
        self.tareas = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.agregar_tarea_evento)

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack()

        self.btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

        # Evento doble clic
        self.listbox.bind("<Double-Button-1>", self.marcar_completada_evento)

    # ---------------------------
    # Funciones principales
    # ---------------------------

    def agregar_tarea(self):
        texto = self.entry.get().strip()
        if texto == "":
            messagebox.showwarning("Aviso", "La tarea no puede estar vacía")
            return

        self.tareas.append((texto, False))
        self.actualizar_lista()
        self.entry.delete(0, tk.END)

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        try:
            index = self.listbox.curselection()[0]
            texto, estado = self.tareas[index]
            self.tareas[index] = (texto, not estado)
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        try:
            index = self.listbox.curselection()[0]
            del self.tareas[index]
            self.actualizar_lista()
        except IndexError:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def actualizar_lista(self):
        self.listbox.delete(0, tk.END)
        for texto, estado in self.tareas:
            if estado:
                self.listbox.insert(tk.END, f"✔ {texto}")
            else:
                self.listbox.insert(tk.END, f"✗ {texto}")

# ---------------------------
# Ejecución de la app
# ---------------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()