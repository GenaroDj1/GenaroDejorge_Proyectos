import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import yagmail

#Se le pidio a chat gpt que integre las listas a la funcion de yagmail, se corrobora si realmente funciona.
import yagmail
import random

def generar_mensajes():
    asuntos_correo = [
        "Consulta importante",
        "Solicitud de colaboración",
        "Actualización sobre el proyecto",
        "Recordatorio de reunión",
        "Invitación a evento",
        "Agradecimiento por tu participación",
        "Oferta especial para ti",
        "Información importante a compartir",
        "Mensaje de seguimiento",
        "Saludos cordiales y actualización"
    ]

    cuerpos_correo = [
        "Espero que este mensaje te encuentre bien. Quería discutir contigo...",
        "Te escribo para solicitarte tu colaboración en un proyecto que estamos...",
        "Quería mantenerte informado sobre el progreso del proyecto. Hemos logrado...",
        "Solo un recordatorio amistoso sobre nuestra reunión programada para...",
        "Nos complace invitarte a nuestro próximo evento. Será una excelente oportunidad...",
        "Quería expresar nuestro agradecimiento por tu valiosa participación en...",
        "¡Tenemos una oferta especial para ti! No querrás perdértela...",
        "Hay información importante que necesito compartir contigo. Por favor, toma un momento...",
        "Solo un breve mensaje de seguimiento para asegurarme de que recibiste...",
        "Saludos cordiales. Solo quería ponerte al día sobre nuestras últimas actividades..."
    ]

    saludos_despedidas = [
        "Saludos cordiales,",
        "Atentamente,",
        "Mis mejores deseos,",
        "Cordialmente,",
        "Un abrazo,",
        "Hasta luego,",
        "Que tengas un gran día,",
        "Saludos afectuosos,",
        "Con gratitud,",
        "Nos vemos pronto,"
    ]

    return (
        random.choice(asuntos_correo),
        random.choice(cuerpos_correo),
        random.choice(saludos_despedidas)
    )

def enviar_mail(mail, password, destinatario):
    try:
        # Generar mensajes aleatorios
        asunto, cuerpo, saludo_despedida = generar_mensajes()

        # Inicializar el objeto yagmail.SMTP
        yag = yagmail.SMTP(user=mail, password=password)

        # Construir el mensaje
        mensaje = f"{saludo_despedida}\n\n{cuerpo}\n\n{asunto}"

        # Enviar el correo electrónico
        yag.send(
            to=destinatario,
            subject=asunto,
            contents=mensaje
        )

        # Cerrar la conexión
        yag.close()

        print(f"Correo electrónico enviado con éxito a {destinatario}.")
        return True

    except Exception as e:
        print(f"Error al enviar el correo electrónico a {destinatario}: {e}")
        return False

# Ejemplo de uso
mail_emisor = mail
contraseña_emisor = password
destinatarios_correo = ['sabrina.sanches@bue.edu.ar','gdejoge22@gmail.com']

for destinatario in destinatarios_correo:
    enviar_mail(mail_emisor, contraseña_emisor, destinatario)