import tkinter as tk
import tkinter.messagebox 
import customtkinter as ctk
from datetime import datetime
import sqlite3
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class Create_User(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Crear Usuario")
        self.geometry(f"{600}x{600}")
        # configure grid layout (4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.frame = ctk.CTkFrame(self, width=320, height=360, corner_radius=15)
        self.frame.pack(padx=(40, 40), pady=(40, 40))
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.label_Agg = ctk.CTkLabel(master=self.frame, text="Crear usuario", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_Agg.grid(padx=20, pady=(10, 10))
        self.opcion_ID = ctk.CTkOptionMenu(self.frame, values=["V","E","J","P","G"])
        self.opcion_ID.grid(row=1,column=0, padx=20, pady=20)
        self.entry_Cedula= ctk.CTkEntry(master=self.frame, placeholder_text="Cedula")
        self.entry_Cedula.grid(row=1, column= 1,padx=20, pady=20)
        self.entry_Nombre = ctk.CTkEntry(master=self.frame, placeholder_text="Nombre")
        self.entry_Nombre.grid(row=2, column= 0,padx=20, pady=20)
        self.entry_Ape = ctk.CTkEntry(master=self.frame, placeholder_text="Apellido")
        self.entry_Ape.grid(row=2, column= 1,padx=20, pady=20)
        self.entry_User= ctk.CTkEntry(master=self.frame, placeholder_text="Usuario")
        self.entry_User.grid(row=3, column= 0,padx=20, pady=20)
        self.entry_Pass = ctk.CTkEntry(master=self.frame, placeholder_text="Contraseña", show="*")
        self.entry_Pass.grid(row=3, column= 1,padx=20, pady=20)
        self.entry_Email= ctk.CTkEntry(master=self.frame, placeholder_text="Email")
        self.entry_Email.grid(row=4, column= 0,padx=20, pady=20)
        self.opcion_Email = ctk.CTkOptionMenu(self.frame, values=["@hotmail.com","@gmail.com","@yahoo.com","@outlook.com",""])
        self.opcion_Email.grid(row=4,column=1, padx=20, pady=20)
        self.opcion_phone = ctk.CTkOptionMenu(self.frame, values=["0424","0414","0412","0416","0426"])
        self.opcion_phone.grid(row=5,column=0, padx=20, pady=20)
        self.entry_Phone = ctk.CTkEntry(master=self.frame, placeholder_text="Telefono")
        self.entry_Phone.grid(row=5, column= 1,padx=20, pady=20)
        self.label_direc = ctk.CTkLabel(master=self.frame, text="Dirección", font=('Century Gothic', 16))
        self.label_direc.grid(row=6, column=0, padx=20, pady=20)
        self.entry_Direc = ctk.CTkEntry(master=self.frame, width=250, height=100)
        self.entry_Direc.grid(row=6, column= 1,padx=20, pady=20)
        self.button_Code = ctk.CTkButton(master=self.frame, text="Crear Cuenta", command=self.agregar_empleado)
        self.button_Code.grid(row=7, column=1, padx=20, pady=20)
    
    def agregar_empleado(self):
        
        # Obtener los valores ingresados por el usuario
        cedula = self.entry_Cedula.get()
        nombre = self.entry_Nombre.get()
        apellido = self.entry_Ape.get()
        usuario = self.entry_User.get()
        password = self.entry_Pass.get()
        e_email = self.entry_Email.get()
        O_email = self.opcion_Email.get()
        e_telefono = self.entry_Phone.get()
        o_telefono = self.opcion_phone.get()
        direccion = self.entry_Direc.get()
        tipo_doc = self.opcion_ID.get() 
        
        telefono = f"{o_telefono}{e_telefono}"
        email = f"{e_email}{O_email}"

        # Validar que se ingresen todos los campos requeridos
        if not cedula or not nombre or not apellido or not usuario or not password or not email or not telefono or not direccion or not tipo_doc:
            tkinter.messagebox.showerror("Error", "Por favor, complete todos los campos")
            return
        # Validar que nombre y apellido no contengan caracteres especiales ni números
        if not nombre.isalpha() or not apellido.isalpha():
            tkinter.messagebox.showerror("Error", "El nombre y apellido deben contener solo letras")
            return

        # Validar que el campo de teléfono contenga solo números
        if not telefono.isdigit():
            tkinter.messagebox.showerror("Error", "El campo de Teléfono debe contener solo números")
            return
        # Validar que el campo de Cedula contenga solo números
        if not cedula.isdigit():
            tkinter.messagebox.showerror("Error", "El campo de Cedula debe contener solo números")
            return
        # Lógica para agregar el empleado a la base de datos
        try:
            # Conectar a la base de datos
            conn = sqlite3.connect("ferretodo.db")
            c = conn.cursor()

            # Insertar el nuevo usuario en la tabla
            c.execute("INSERT INTO empleados (cedula, nombre, apellido, usuario, password, email, telefono, direccion, tipo_doc) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (cedula, nombre, apellido, usuario, password, email, telefono, direccion, tipo_doc))
            conn.commit()

            tkinter.messagebox.showinfo("Éxito", "El usuario se ha creado exitosamente")


            # Cerrar la conexión a la base de datos
            c.close()
            conn.close()
            self.destroy()


        except Exception as e:
            tkinter.messagebox.showerror("Error", f"No se pudo crear el usuario: {e}")



        
if __name__ == "__main__":
    creating = Create_User()
    creating.mainloop()
