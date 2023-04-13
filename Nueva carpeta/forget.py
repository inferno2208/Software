import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from datetime import datetime

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

class Forget_Pass(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Recuperar Contraseña")
        self.geometry(f"{600}x{440}")
        # configure grid layout (4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        self.frame = ctk.CTkFrame(self, width=320, height=360, corner_radius=15)
        self.frame.pack(padx=(40, 40), pady=(40, 40))
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.label_Forget = ctk.CTkLabel(master=self.frame, text="Recuperar contraseña", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_Forget.grid(padx=20, pady=(10, 10))
        self.entry_Email = ctk.CTkEntry(master=self.frame, placeholder_text="Email recuperacion")
        self.entry_Email.grid(row=1, column= 0,padx=20, pady=20)
        self.entry_RepetEmail = ctk.CTkEntry(master=self.frame, placeholder_text="Repetir Email")
        self.entry_RepetEmail.grid(row=2, column= 0,padx=20, pady=20)
        self.button_Code = ctk.CTkButton(master=self.frame, text="Enviar codigo")
        self.button_Code.grid(row=3, column=0, padx=20, pady=20)
        self.entry_Code = ctk.CTkEntry(master=self.frame, placeholder_text="introduce el codigo")
        self.entry_Code.grid(row=4, column= 0,padx=20, pady=20)
        self.button_Pass = ctk.CTkButton(master=self.frame, text="comprobar")
        self.button_Pass.grid(row=5, column=0, padx=20, pady=20)

if __name__ == "__main__":
    forgeting = Forget_Pass()
    forgeting.mainloop()
