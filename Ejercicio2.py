import tkinter as tk

def mostrar_clave():
    clave = entrada_clave.get()
    label_resultado.config(text=f"Clave: {'*' * len(clave)}")

ventana = tk.Tk()
ventana.title("Clave")
ventana.geometry("300x200")

# Etiqueta y campo para la clave
label_clave = tk.Label(ventana, text="Ingresa tu clave:", font=("Garamond", 12, "bold"))
label_clave.pack(pady=5)
entrada_clave = tk.Entry(ventana, show="*")
entrada_clave.pack()

# Btn para mostrar la clave
boton = tk.Button(ventana, text="Mostrar", command=mostrar_clave)
boton.pack(pady=10)

# mostrar el resultado
label_resultado = tk.Label(ventana, font=("Arial", 12))
label_resultado.pack()

ventana.mainloop()
