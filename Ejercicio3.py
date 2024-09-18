import tkinter as tk

def mostrar_datos():
    cedula = entrada_cedula.get()
    nombre = entrada_nombre.get()
    label_resultado.config(text=f"Cédula: {cedula}\nNombre: {nombre}")

ventana = tk.Tk()
ventana.title("Datos Personales")
ventana.geometry("300x200")

# Etiqueta y campo para cédula
label_cedula = tk.Label(ventana, text="Ingresa tu número de cédula:", font=("Garamond", 12, "bold"))
label_cedula.pack(pady=5)
entrada_cedula = tk.Entry(ventana)
entrada_cedula.pack()

# Etiqueta y campo para nombre
label_nombre = tk.Label(ventana, text="Ingresa tu nombre completo:", font=("Garamond", 12, "bold"))
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Botón para mostrar datos
boton = tk.Button(ventana, text="Mostrar", command=mostrar_datos)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, font=("Garamond", 12))
label_resultado.pack()

ventana.mainloop()
