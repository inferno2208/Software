import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
import sqlite3
import smtplib
from email.mime.text import MIMEText
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
        self.button_Code = ctk.CTkButton(master=self.frame, text="Enviar codigo", command=self.send_code)
        self.button_Code.grid(row=3, column=0, padx=20, pady=20)
        self.entry_Code = ctk.CTkEntry(master=self.frame, placeholder_text="introduce el codigo")
        self.entry_Code.grid(row=4, column= 0,padx=20, pady=20)
        self.button_Pass = ctk.CTkButton(master=self.frame, text="comprobar")
        self.button_Pass.grid(row=5, column=0, padx=20, pady=20)

    def send_code(self):
        email = self.entry_Email.get()

        # Verificar si el correo electrónico ingresado está en la base de datos
        conn = sqlite3.connect('ferretodo.db')  # Reemplaza 'tu_base_de_datos.db' con el nombre de tu base de datos
        c = conn.cursor()
        c.execute("SELECT email FROM empleados WHERE email=?", (email,))
        result = c.fetchone()
        conn.close()

        if result:
           # Generar un código aleatorio (puedes personalizarlo según tus necesidades)
            import random
            code = str(random.randint(100000, 999999))

            # Configurar los detalles del correo electrónico
            sender_email = "ferretodo.recuperar@gmail.com"  # Dirección de correo electrónico del remitente
            sender_password = "28103046Ll."  # Contraseña del remitente
            receiver_email = email  # Dirección de correo electrónico del destinatario
            subject = "Código de recuperación de contraseña"  # Asunto del correo electrónico
            message = f"Tu código de recuperación de contraseña es: {code}"  # Cuerpo del correo electrónico

            try:
                # Crear un objeto MIMEText para el mensaje del correo electrónico
                msg = MIMEText(message)
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg['Subject'] = subject

                # Iniciar una conexión SMTP y enviar el correo electrónico
                with smtplib.SMTP_SSL('smtp.gmail.com', 587) as server:
                    server.login(sender_email, sender_password)
                    server.sendmail(sender_email, receiver_email, msg.as_string())

                # Almacenar el código generado para su verificación posterior
                self.generated_code = code

                tkinter.messagebox.showinfo("Código enviado", "Se ha enviado un código de recuperación a tu correo electrónico.")
            except Exception as e:
                tkinter.messagebox.showerror("Error", f"No se pudo enviar el código por correo electrónico: {e}")


        else:
            tkinter.messagebox.showerror("Correo electrónico no válido", "El correo electrónico ingresado no está registrado en la base de datos.")

    # ...

if __name__ == "__main__":
    forgeting = Forget_Pass()
    forgeting.mainloop()
