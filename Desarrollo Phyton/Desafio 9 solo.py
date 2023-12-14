import yagmail
#from google.colab import userdata

usuario_contraseña= '/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python/desafio9/Credenciales.txt'
#ruta donde tengo mi archivo .txt con mail y pass

with open(usuario_contraseña, 'r') as archivo:
    mail= archivo.readline().strip()
    contraseña= archivo.readline().strip()

print("Mail:", mail)
print("Contraseña:", contraseña) 
#devuelve el mail y pass del archivo .txt

ruta_archivo = "/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python/desafio9/Copia de Credenciales.txt"
#ruta_archivo= "/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python/desafio9/Credenciales2.txt"
def usuario_contraseña(ruta_archivo):
  with open(ruta_archivo, 'r') as archivo:
    mail = archivo.readline().strip()
    contraseña = archivo.readline().strip()
    return mail, contraseña

print("Mail:", mail)
print("Contraseña:", contraseña)
#lo mismo pero con un def

#from google.colab import userdata

#mail = userdata.get('mail')
#password = userdata.get('password')

#print(mail)
#print(password)
#me sirve en el colab para las password y mail asignadas en la llavecita

def enviar_mail(mail, password, asunto, mensaje, destinatarios):
    try:
        yag = yagmail.SMTP(user=mail, password=password)

        contenido = [mensaje_correo, archivo_adjunto]
        yag.send(destinatarios_correo, asunto_correo, contenido)
        yag.close()

        print("Correo electrónico enviado con éxito.")
        return True

    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")
        return False

asunto_correo = f'Prueba para desafio 9 de Genaro de jorge'
mensaje_correo = '''<h1>Test de prueba de desafio 9</h1>
                  <p>TEST EN MAYUSC PARA VER COMO SE IMPRIME EN EL EMAIL,
                  GRACIAS POR LO QUE NOS ENSEÑAN PROFE LA VERDAD QUE ES RE COPADO ME ENCANTA PROGRAMAR ESTOS CODIGOS
                  SON GENIALES!!!!</p>'''
destinatarios_correo = ['sabrina.sanches@bue.edu.ar', 'gdejorge22@gmail.com']
archivo_adjunto= "/content/drive/MyDrive/Curso_python_Lonely/proyecto_dsd_python/desafio9/gracias.jpg"

#enviar_mail(mail, password, asunto_correo, mensaje_correo, destinatarios_correo)

#envia un correo electronico, la password es del colab para usarla en vs hacer un settings.ini