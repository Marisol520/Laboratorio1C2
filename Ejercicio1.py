import tkinter as tk

def mostrar_datos():
    nombre = entrada_nombre.get()
    edad = entrada_edad.get()
    label_resultado.config(text=f"Nombre: {nombre}\nEdad: {edad}")

ventana = tk.Tk()
ventana.title("Datos Personales")
ventana.geometry("300x200")

# campo para nombre
label_nombre = tk.Label(ventana, text="Ingresa tu nombre completo:", font=("Garamond", 12, "bold"))
label_nombre.pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

# Campo para edad
label_edad = tk.Label(ventana, text="Ingresa tu edad:", font=("Garamond", 12, "bold"))
label_edad.pack(pady=5)
entrada_edad = tk.Entry(ventana)
entrada_edad.pack()

# Btn para mostrar las respuestas
boton = tk.Button(ventana, text="Mostrar", command=mostrar_datos)
boton.pack(pady=10)

# mostrar el resultado
label_resultado = tk.Label(ventana, font=("Garamond", 12))
label_resultado.pack()

ventana.mainloop()
