import smtplib
import ssl

port = 465  # Puerto de Gmail para SSL
smtp_server = "smtp.gmail.com"
sender_email = "ferretodo.recuperar@gmail.com"  # Dirección de correo electrónico del remitente
password = "28103046Ll."  # Contraseña del correo electrónico del remitente
receiver_email = "inferno2208@gmail.com"  # Dirección de correo electrónico del destinatario
message = "Hola, este es un correo de prueba enviado desde Python."

# Establecer conexión con el servidor de correo
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)