import tkinter as tk
from tkinter import ttk

# Función para simular la carga de archivos
def cargar_archivos():
    # Aquí puedes colocar la lógica real de carga de archivos
    # o cualquier otro proceso que quieras simular
    for i in range(1, 101):
        # Actualizar la barra de progreso
        progress_bar['value'] = i
        window.update_idletasks()
        # Simular un retraso de tiempo para que se vea la animación
        window.after(50)

# Crear la ventana principal
window = tk.Tk()
window.title("Pantalla de carga")

# Crear una imagen personalizada para el fondo de la pantalla de carga
# Puedes cambiar la ruta de la imagen a la ruta de tu propia imagen


# Crear la barra de progreso personalizada
style = ttk.Style()
style.configure("TProgressbar",
                thickness=50,
                troughcolor='gray',
                background='green',
                )

progress_bar = ttk.Progressbar(window, style="TProgressbar", mode='determinate', length=200)
progress_bar.place(relx=0.5, rely=0.7, anchor='center')

# Crear el botón para iniciar la carga de archivos
btn_cargar = ttk.Button(window, text="Cargar archivos", command=cargar_archivos)
btn_cargar.place(relx=0.5, rely=0.8, anchor='center')

# Iniciar el bucle principal de la ventana
window.mainloop()