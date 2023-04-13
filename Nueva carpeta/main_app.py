import tkinter as tk
import tkinter.messagebox
import customtkinter as ctk
from datetime import datetime
from PIL import Image, ImageTk
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")  
class Home(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ferre-Todo")
        self.geometry(f"{1280}x{720}")
    
        # configure grid layout (4x4
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)

        #sidebar 
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Ferre Todo", font=('Century Gothic',40))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame,corner_radius=0, height=40, border_spacing=10, text="Compras", fg_color="transparent", hover_color=("gray70", "gray30"),font=('Century Gothic',16), command=self.button_event_buy)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10,sticky="nsew")
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame,corner_radius=0, height=40, border_spacing=10, text="Clientes",fg_color="transparent", hover_color=("gray70", "gray30"),font=('Century Gothic',16), command=self.button_event_clients)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10,sticky="nsew")
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame,corner_radius=0, height=40, border_spacing=10, text="Productos",fg_color="transparent", hover_color=("gray70", "gray30"),font=('Century Gothic',16), command=self.button_event_products)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")
        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame,corner_radius=0, height=40, border_spacing=10,  text="Reporte",fg_color="transparent", hover_color=("gray70", "gray30"),font=('Century Gothic',16), command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10, sticky="nsew")
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Modo noche:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        #top desing
        self.top_frame = ctk.CTkFrame(self)
        self.top_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.principal_label = ctk.CTkLabel(self.top_frame, text="Bienvenido a Ferre-Todo Programa Administrativo De Ferreteria", font=('Century Gothic',30))
        self.principal_label.grid(row=0, column=0, padx=20, pady=20)
        
        #mainframe
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_label = ctk.CTkLabel(self.main_frame, text="Productos que mas piden",font=('Century Gothic',20))
        self.main_label.grid(row=1, column=1, padx=20, pady=(20, 10))
        self.photo_frame = ctk.CTkFrame(master=self.main_frame)
        self.photo_frame.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        image = Image.open("C:/Users/infer/OneDrive/Escritorio/Nueva carpeta/martillo.png")
        
        nuevo_ancho = 300 # ancho en píxeles
        nuevo_alto = 250 # alto en píxeles

        # Redimensionar la imagen
        image = image.resize((nuevo_ancho, nuevo_alto))
        image = ImageTk.PhotoImage(image)

        # Mostrar imagen en un widget Label
        self.image_label = ctk.CTkLabel(self.photo_frame, image=image, text=" ")
        self.image_label.grid(row=2, column=0, padx=20, pady=(10, 10))

        image = Image.open("C:/Users/infer/OneDrive/Escritorio/Nueva carpeta/tornillo.png")
        nuevo_ancho = 300 # ancho en píxeles
        nuevo_alto = 250 # alto en píxeles

        # Redimensionar la imagen
        image = image.resize((nuevo_ancho, nuevo_alto))
        image = ImageTk.PhotoImage(image)

        # Mostrar imagen en un widget Label
        self.image_label = ctk.CTkLabel(self.photo_frame, image=image, text=" ")
        self.image_label.grid(row=2, column=1, padx=20, pady=(10, 10))

        image = Image.open("C:/Users/infer/OneDrive/Escritorio/Nueva carpeta/destornillador.png")
        nuevo_ancho = 300 # ancho en píxeles
        nuevo_alto = 250 # alto en píxeles

        # Redimensionar la imagen
        image = image.resize((nuevo_ancho, nuevo_alto))
        image = ImageTk.PhotoImage(image)
        

        # Mostrar imagen en un widget Label
        self.image_label = ctk.CTkLabel(self.photo_frame, image=image, text=" ")
        self.image_label.grid(row=2, column=2, padx=20, pady=(10, 10))

        image = Image.open("C:/Users/infer/OneDrive/Escritorio/Nueva carpeta/agua.png")
        nuevo_ancho = 300 # ancho en píxeles
        nuevo_alto = 250 # alto en píxeles

        # Redimensionar la imagen
        image = image.resize((nuevo_ancho, nuevo_alto))
        image = ImageTk.PhotoImage(image)
        

        # Mostrar imagen en un widget Label
        self.image_label = ctk.CTkLabel(self.photo_frame, image=image, text=" ")
        self.image_label.grid(row=2, column=3, padx=20, pady=(10, 10))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
    
    def sidebar_button_event(self):
        print("sidebar_button click")
    def button_event_buy(self):
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.main_label = ctk.CTkLabel(self.main_frame, text="Compras de Productos",font=('Century Gothic',20))
        self.main_label.grid(row=1, column=3, padx=20, pady=(20, 10))
        self.button_buy_ = ctk.CTkButton(self.main_frame,corner_radius=0, height=40, border_spacing=10, text="Compras de Productos", fg_color="transparent", hover_color=("gray70", "gray30"),font=('Century Gothic',16), command=self.button_event_product_sell)
        self.button_buy_.grid(row=2, column=0, padx=20, pady=10)
        self.button_watter = ctk.CTkButton(self.main_frame,corner_radius=0, height=40, border_spacing=10, text="Compras de Agua", fg_color="transparent", hover_color=("gray70", "gray30"),font=('Century Gothic',16), command=self.sidebar_button_event)
        self.button_watter.grid(row=3, column=0, padx=20, pady=10)


    def button_event_product_sell(self):
            self.main_frame.destroy()
            self.main_frame = ctk.CTkFrame(self)
            self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.main_label = ctk.CTkLabel(self.main_frame, text="Ventas de Productos",font=('Century Gothic',20))
            self.main_label.grid(row=1, column=2, padx=20, pady=(20, 10))
            self.label_seletion = ctk.CTkLabel(self.main_frame, text="Selecciona un producto",font=('Century Gothic',16))
            self.label_seletion.grid(row=2, column=1, padx=20, pady=(20, 10))

            # Crear un Listbox
            self.listbox = tk.Listbox(self.main_frame, font=('Century Gothic', 14), bg='darkgrey', fg='white')
            self.listbox.grid(row=3, column=1, padx=20, pady=(20, 10), sticky="nsew")

            # Agregar elementos al Listbox
            self.listbox.insert(tk.END, "Producto 1")
            self.listbox.insert(tk.END, "Producto 2")
            self.listbox.insert(tk.END, "Producto 3")

            # Configurar el Listbox para que se ajuste automáticamente a su contenido
            self.listbox.config(width=0, height=0, selectmode=tk.SINGLE)

            # Crear un Entry para mostrar el elemento seleccionado del Listbox
            self.selected_item = tk.StringVar()
            self.entry = ctk.CTkEntry(self.main_frame, textvariable=self.selected_item, font=('Century Gothic', 14))
            self.entry.grid(row=4, column=1, padx=20, pady=(20, 10), sticky="nsew")

            # Vincular la selección del Listbox con el Entry
            self.listbox.bind('<<ListboxSelect>>', self.seleccionar_elemento)

            def seleccionar_elemento(event):
                seleccion = self.listbox.get(self.listbox.curselection())  # Obtener el elemento seleccionado del Listbox
                self.selected_item.set(seleccion)  # Actualizar el valor del Entry con el elemento seleccionado

                # Limpiar el Listbox
                self.listbox.delete(0, tk.END)
                # Agregar elementos actualizados al Listbox
                self.listbox.insert(tk.END, "Producto 1 (Actualizado)")
                self.listbox.insert(tk.END, "Producto 2 (Actualizado)")
                self.listbox.insert(tk.END, "Producto 3 (Actualizado)")

                # Setear la selección en el Listbox
                self.listbox.selection_clear(0, tk.END)
                self.listbox.selection_set(tk.END)
                self.listbox.activate(tk.END)

            


            
    def button_event_clients(self):
            self.main_frame.destroy()
            self.main_frame = ctk.CTkFrame(self)
            self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.main_label = ctk.CTkLabel(self.main_frame, text="Clientes",font=('Century Gothic',30))
            self.main_label.grid(row=1, column=2, padx=(20, 20), pady=(20, 20))
            self.button_user_agg = ctk.CTkButton(self.main_frame, text="Agregar",font=('Century Gothic', 16), command=self.button_event_agg)
            self.button_user_agg.grid(row=3, column=4, padx=20, pady=10)
            self.button_user_agg.place(x=600, y=350)
            self.button_mod_user = ctk.CTkButton(self.main_frame, text="Modificar",font=('Century Gothic', 16), hover_color="green", command=self.sidebar_button_event)
            self.button_mod_user.grid(row=4, column=4, padx=20, pady=10)
            self.button_mod_user.place(x=600, y=400)
            self.button_delete_user = ctk.CTkButton(self.main_frame, text="Eliminar", font=('Century Gothic', 16), hover_color="red")
            self.button_delete_user.grid(row=4, column=4, padx=10,pady=10)
            self.button_delete_user.place(x=600, y=450)
            self.list_user_frame = ctk.CTkFrame(self.main_frame, width=500, height=400)
            self.list_user_frame.grid(row=2, column=2, padx=(20, 20), pady=(20, 20))
    def button_event_agg(self):
            self.main_frame.destroy()
            self.main_frame = ctk.CTkFrame(self)
            self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
            self.main_label = ctk.CTkLabel(self.main_frame, text="Agregar Cliente",font=('Century Gothic',30))
            self.main_label.grid(row=1, column=3, padx=20, pady=(20, 10))
            self.label_name = ctk.CTkLabel(self.main_frame, text="Nombre del Cliente:", font=('Century Gothic', 16))
            self.label_name.grid(row= 2, column=1, padx=10, pady=10)
            self.entry_user_name = ctk.CTkEntry(self.main_frame, placeholder_text="Nombre", font=('Century Gothic', 16))
            self.entry_user_name.grid(row=2, column=2, padx=10, pady=10)
            self.label_last_name = ctk.CTkLabel(self.main_frame, text="Apellido del Cliente:", font=('Century Gothic', 16))
            self.label_last_name.grid(row=3, column=1, padx=10, pady=10)
            self.entry_user_lastName = ctk.CTkEntry(self.main_frame,placeholder_text="Apellido", font=('Century Gothic', 16))
            self.entry_user_lastName.grid(row=3, column=2, padx=10, pady=10)
            self.label_user_ID = ctk.CTkLabel(self.main_frame, text="Cedula: ", font=('Century Gothic', 16))
            self.label_user_ID.grid(row=2, column=3, padx=30, pady=30)
            self.opcion_menu_ID = ctk.CTkOptionMenu(self.main_frame, values=["V","E","J","P","G"], height=20, width=20)
            self.opcion_menu_ID.grid(row=2,column=3, padx=10, pady=20)
            self.opcion_menu_ID.place(x=550, y=102)
            self.entry_ID = ctk.CTkEntry(self.main_frame, placeholder_text="Num. Documento",font=('Century Gothic', 16))
            self.entry_ID.grid(row=2, column=5, padx=10, pady=10)
            self.entry_ID.place(x=600, y=100)
            self.label_direction = ctk.CTkLabel(self.main_frame, text="Direccion del Cliente: ", font=('Century Gothic', 16))
            self.label_direction.grid(row=4, column=1, padx=10, pady=10)
            self.textbox = ctk.CTkTextbox(self.main_frame, width=30, height=100)
            self.textbox.grid(row=4, column=2, padx=(10, 0), pady=(10, 0), sticky="nsew")
            self.label_phone = ctk.CTkLabel(self.main_frame, text="Teléfonos del Cliente:", font=('Century Gothic', 16))
            self.label_phone.grid(row=3, column=3, padx=10, pady=10)
            self.entry_phone = ctk.CTkEntry(self.main_frame, placeholder_text="Num. De Teléfono", font=('Century Gothic', 16), width=150)
            self.entry_phone.grid(row=3, column=4, padx=10, pady=10)
            self.button_next = ctk.CTkButton(master=self.main_frame, text="Siguiente")
            self.button_next.grid(row=4, column =4, padx=10, pady=10)


    def button_event_products(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.label_products = ctk.CTkLabel(self.main_frame, text="Productos", font=('Century Gothic', 30))
        self.label_products.grid(row=1, column=2, padx=(20, 20), pady=(20, 20))
        self.button_agg_products = ctk.CTkButton(self.main_frame, text="Agregar", font=('Century Gothic', 16), command=self.button_event_agg_products)
        self.button_agg_products.grid(row=2, column=4, padx=10,pady=10)
        self.button_agg_products.place(x=600, y=350)
        self.button_mod_products = ctk.CTkButton(self.main_frame, text="Modificar", font=('Century Gothic', 16), hover_color="green")
        self.button_mod_products.grid(row=3, column=4, padx=10,pady=10)
        self.button_mod_products.place(x=600, y=400)
        self.button_delete_products = ctk.CTkButton(self.main_frame, text="Eliminar", font=('Century Gothic', 16), hover_color="red")
        self.button_delete_products.grid(row=4, column=4, padx=10,pady=10)
        self.button_delete_products.place(x=600, y=450)
        self.list_products_frame = ctk.CTkFrame(self.main_frame, width=500, height=400)
        self.list_products_frame.grid(row=2, column= 2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.list = tk.Listbox(self.list_products_frame)
        self.list(row=0, column=0, padx=10, pady=10)
        
    def button_event_agg_products(self):
        self.main_frame.destroy()
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.label_products = ctk.CTkLabel(self.main_frame, text="Agregar Productos", font=('Century Gothic', 30))
        self.label_products.grid(row=0, column=2, padx=(20, 20), pady=(20, 20))
        self.label_name_products = ctk.CTkLabel(master=self.main_frame, text="Nombre del producto", font=('Century Gothic', 16))
        self.label_name_products.grid(row=1, column=0, padx=20, pady=20)
        self.entry_name_products = ctk.CTkEntry(master=self.main_frame, placeholder_text="producto", font=('Century Gothic', 16))
        self.entry_name_products.grid(row=1, column=1, padx=20, pady=20)
        self.label_code_products = ctk.CTkLabel(master=self.main_frame, text="codigo del producto", font=('Century Gothic', 16))
        self.label_code_products.grid(row=2, column=0, padx=20, pady=20)
        self.entry_code_products = ctk.CTkEntry(master=self.main_frame, placeholder_text="codigo", font=('Century Gothic', 16))
        self.entry_code_products.grid(row=2, column=1, padx=20, pady=20)
        self.label_dolar_products = ctk.CTkLabel(master=self.main_frame, text="precio en $ del producto", font=('Century Gothic', 16))
        self.label_dolar_products.grid(row=3, column=0, padx=20, pady=20)
        self.entry_dolar_products = ctk.CTkEntry(master=self.main_frame, placeholder_text="$$", font=('Century Gothic', 16))
        self.entry_dolar_products.grid(row=3, column=1, padx=20, pady=20)
        self.label_price_products = ctk.CTkLabel(master=self.main_frame, text="precio en bs del producto", font=('Century Gothic', 16))
        self.label_price_products.grid(row=4, column=0, padx=20, pady=20)
        self.entry_price_products = ctk.CTkEntry(master=self.main_frame, placeholder_text="bs", font=('Century Gothic', 16))
        self.entry_price_products.grid(row=4, column=1, padx=20, pady=20)
        self.label_direction = ctk.CTkLabel(self.main_frame, text="Descripción del producto ", font=('Century Gothic', 16))
        self.label_direction.grid(row=1, column=2, padx=10, pady=10)
        self.textbox = ctk.CTkTextbox(self.main_frame, width=200, height=100)
        self.textbox.grid(row=2, column=2, padx=10, pady=10)

        self.button_next_product = ctk.CTkButton(master=self.main_frame, text="siguiente")
        self.button_next_product.grid(row=4, column=4, padx=20, pady=20)


if __name__ == "__main__":
    inicio = Home()
    inicio.mainloop()