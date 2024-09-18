import tkinter as tk

def mostrar_mascotas():
    # Obtener los datos
    mascota1_nombre = entrada_mascota1_nombre.get()
    mascota1_tipo = entrada_mascota1_tipo.get()
    mascota1_edad = entrada_mascota1_edad.get()

    mascota2_nombre = entrada_mascota2_nombre.get()
    mascota2_tipo = entrada_mascota2_tipo.get()
    mascota2_edad = entrada_mascota2_edad.get()

    mascota3_nombre = entrada_mascota3_nombre.get()
    mascota3_tipo = entrada_mascota3_tipo.get()
    mascota3_edad = entrada_mascota3_edad.get()

    # Mostrar los datos en la etiqueta de resultado
    label_resultado.config(
        text=f"Animal 1: {mascota1_nombre}, {mascota1_tipo}, {mascota1_edad} años\n"
             f"Animal 2: {mascota2_nombre}, {mascota2_tipo}, {mascota2_edad} años\n"
             f"Animal 3: {mascota3_nombre}, {mascota3_tipo}, {mascota3_edad} años"
    )

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Datos de Animales")
ventana.geometry("300x300")

def crear_entrada(ventana, texto_label):
    frame = tk.Frame(ventana)
    frame.pack(pady=5, anchor='w', fill=tk.X)

    label = tk.Label(frame, text=texto_label, font=("Garamond", 12, "bold"))
    label.pack(side=tk.LEFT, padx=5)

    entrada = tk.Entry(frame, width=15)
    entrada.pack(side=tk.LEFT, padx=5)
    
    return entrada

# Ingresar datos para el animal 1
label_mascota1 = tk.Label(ventana, text="Datos de la Mascota 1", font=("Garamond", 12, "bold"))
label_mascota1.pack(pady=5, anchor='w')

entrada_mascota1_nombre = crear_entrada(ventana, "Nombre")
entrada_mascota1_tipo = crear_entrada(ventana, "Tipo")
entrada_mascota1_edad = crear_entrada(ventana, "Edad")

# Ingresar datos para el animal 2
label_mascota2 = tk.Label(ventana, text="Datos de la Mascota 2", font=("Garamond", 12, "bold"))
label_mascota2.pack(pady=5, anchor='w')

entrada_mascota2_nombre = crear_entrada(ventana, "Nombre")
entrada_mascota2_tipo = crear_entrada(ventana, "Tipo")
entrada_mascota2_edad = crear_entrada(ventana, "Edad")

# Ingresar datos para el animal 3
label_mascota3 = tk.Label(ventana, text="Datos de la Mascota 3", font=("Garamond", 12, "bold"))
label_mascota3.pack(pady=5, anchor='w')

entrada_mascota3_nombre = crear_entrada(ventana, "Nombre")
entrada_mascota3_tipo = crear_entrada(ventana, "Tipo")
entrada_mascota3_edad = crear_entrada(ventana, "Edad")

# Botón para mostrar dats
boton = tk.Button(ventana, text="Mostrar", command=mostrar_mascotas)
boton.pack(pady=10, anchor='w')

# Etiqueta para mostrar el resultdo
label_resultado = tk.Label(ventana, font=("Garamond", 12))
label_resultado.pack(pady=10, anchor='w')

ventana.mainloop()
