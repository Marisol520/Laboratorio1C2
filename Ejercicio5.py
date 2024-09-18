import tkinter as tk
from tkinter import font, messagebox
import re  # Para validaciones

def validar_datos():
    # Validar correo
    correo = entradas[6].get()
    if not re.match(r"[^@]+@[^@]+\.[^@]+", correo):
        messagebox.showerror("Error", "Asegurate de poner @ al correo.")
        return False
    
    # Validar edad
    edad = entradas[2].get()
    if not edad.isdigit() or int(edad) <= 0:
        messagebox.showerror("Error", "Por favor ingrese una edad mayor a 0.")
        return False
    
    # Validar contacto (solo números)
    contacto = entradas[5].get()
    if not contacto.isdigit():
        messagebox.showerror("Error", "El numero de telefono debe tener solo numeros.")
        return False
    
    return True

def mostrar_datos():
    if validar_datos():
        # Limpiar el frame derecho antes de mostrar nuevos datos
        for widget in frame_derecha.winfo_children():
            widget.destroy()

        for i, pregunta in enumerate(preguntas):
            label_bold = tk.Label(frame_derecha, text=f"{pregunta}:", font=bold_font, bg="#f2f2f2", anchor="w")
            label_normal = tk.Label(frame_derecha, text=entradas[i].get(), font=normal_font, bg="#f2f2f2", anchor="w")
            
            # Colocar las etiquetas y datos en el frame derecho
            label_bold.grid(row=i, column=0, padx=10, pady=5, sticky="e")
            label_normal.grid(row=i, column=1, padx=10, pady=5, sticky="w")

#Crear ventana principal
ventana = tk.Tk()
ventana.title("Datos Personales")
ventana.geometry("800x400")
ventana.configure(bg="#f2f2f2")

# Fuente personalizada 'Garamond'
bold_font = font.Font(family="Garamond", size=12, weight="bold")
normal_font = font.Font(family="Garamond", size=12)

entradas = []  # Lista para almacenar los campos de entrada

# Lista de preguntas
preguntas = [
    "Nombre", "Apellido", "Edad", "Fecha de nacimiento", "Lugar de residencia",
    "Contacto", "Correo electrónico", "Estado civil", "Profesión", "Hobbies"
]

# Crear marco principal para organizar la izquierda y derecha
frame_principal = tk.Frame(ventana, bg="#f2f2f2")
frame_principal.pack(padx=20, pady=20, fill="both", expand=True)

# Marco para la columna izquierda (formularios)
frame_izquierda = tk.Frame(frame_principal, bg="#f2f2f2")
frame_izquierda.grid(row=0, column=0, padx=20, pady=20)

# Marco para la columna derecha (resultados)
frame_derecha = tk.Frame(frame_principal, bg="#f2f2f2", bd=2, relief="groove")
frame_derecha.grid(row=0, column=1, padx=20, pady=20)

# Crear etiquetas y campos de entrada en la columna izquierda
for i, pregunta in enumerate(preguntas):
    label = tk.Label(frame_izquierda, text=f"{pregunta}:", font=bold_font, bg="#f2f2f2", anchor="w")
    entrada = tk.Entry(frame_izquierda, width=30, font=normal_font)  # Aplicar la fuente a los campos de entrada
    
    # Colocar las etiquetas y entradas en una cuadrícula
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entrada.grid(row=i, column=1, padx=10, pady=5, sticky="w")
    
    entradas.append(entrada)

# Botón para mostrar los datos, alineado abajo a la izquierda
boton = tk.Button(frame_izquierda, text="Enviar", command=mostrar_datos, width=20, bg="#1369B1", fg="black", font=("Garamond", 12, "bold"))
boton.grid(row=len(preguntas), column=0, columnspan=2, pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()