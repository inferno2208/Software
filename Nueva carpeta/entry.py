import tkinter as tk
import sqlite3
import tkinter.messagebox
import customtkinter as ctk
from datetime import datetime
from main_app import Home
from createAccount import Create_User
from forget import Forget_Pass
from tkinter import messagebox


ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  

class Login_enter(ctk.CTk): 
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry(f"{600}x{440}")

         # configure grid layout (4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.frame = ctk.CTkFrame(self, width=320, height=360, corner_radius=15)
        self.frame.pack(padx=(40, 40), pady=(40, 40))
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.login = ctk.CTkLabel(master=self.frame, text="Inicio de sesión", font=ctk.CTkFont(size=20, weight="bold"))
        self.login.grid(padx=20, pady=(10, 10))
        self.user = ctk.CTkEntry(master=self.frame, placeholder_text="Usuario")
        self.user.grid(padx=(20, 0), pady=(10, 20))
        self.password = ctk.CTkEntry(master=self.frame, placeholder_text="contraseña", show="*")
        self.password.grid(padx=(20, 0), pady=(10, 20))
        
        self.button = ctk.CTkButton(master=self.frame, text="Siguiente", command=self.button_event)
        self.button.grid(padx=20, pady=10)
        self.button_forget = ctk.CTkButton(master=self.frame, text="Olvidé Contraseña", command=self.button_event_forget)
        self.button_forget.grid(padx=20, pady=10)

        #self.checkbox = ctk.CTkCheckBox(master=self.frame, text="Recordar Usuario")
        #self.checkbox.grid(pady=20, padx=10)

        self.button_agg = ctk.CTkButton(master=self.frame, text="Crear cuenta", command=self.button_event_create)
        self.button_agg.grid(padx=20, pady=20)
        self.appearance_mode = ctk.CTkOptionMenu(master=self.frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode.grid(padx=20, pady=(10, 10))
        


    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    def button_event(self):
        user = self.user.get()
        password = self.password.get()

        # Conectar a la base de datos
        conn = sqlite3.connect("ferretodo.db")
        c = conn.cursor()

        # Consulta SQL para buscar el usuario y contraseña en la tabla empleados
        c.execute("SELECT * FROM empleados WHERE usuario=? AND password=?", (user, password))
        result = c.fetchone()  # Obtener la primera fila de resultado

        # Cerrar la conexión a la base de datos
        conn.close()

        if result:
            # Si se encuentra una coincidencia, permitir el acceso al sistema
            self.progressbar = ctk.CTkProgressBar(self.frame)
            self.progressbar.grid(padx=(20, 10), pady=(10, 10))
            self.progressbar.configure(mode="indeterminnate")
            self.progressbar.start()
            self.destroy()
            main_app = Home()
            main_app.mainloop()
        else:
            # Si no se encuentra una coincidencia, mostrar mensaje de error
            tkinter.messagebox.showerror("Error", "Usuario o contraseña incorrectos")


    def button_event_forget(self):
        self.destroy()
        forget = Forget_Pass()
        forget.mainloop()
    
    def button_event_create(self):
        
        createAccount = Create_User()
        createAccount.mainloop()

if __name__ == "__main__":
    enter = Login_enter()
    enter.mainloop()