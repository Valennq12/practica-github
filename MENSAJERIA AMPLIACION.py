'''En una aplicación de mensajería, se desea implementar un sistema de notificaciones utilizando 
Programación Orientada a Objetos (POO). Para ello, realiza lo siguiente:

Crea una clase base Notificacion con identificador y un nombre de usuario
Crea dos clases derivadas:
Email: Representa una notificación por correo electrónico.
SMS: Representa una notificación por mensaje de texto.
Cada clase derivada debe implementar su propio método enviar_mensaje() de la siguiente manera:
En Email, el método debe recibir como parámetros el asunto y la dirección de email del destinatario e 
imprimir un mensaje indicando a quién se
En SMS, el método debe recibir como parámetro el número de teléfono del destinatario.
Ambos recibirán también el contenido del mensaje y imprimirán una cadena similar a 
"Enviando email con asunto xxxx a xxxxxx " o "Enviando SMS al numero XXXXX"
Crea objetos de ambas clases y prueba el sistema de notificaciones, asegurándote de que el método enviar_mensaje() 
funcione correctamente en cada caso.'''






'''Amplía el ejercicio anterior con los siguientes puntos:

-  Añade dos atributos de clase en las clases Email y SMS para llevar 
la cuenta del número total de correos electrónicos y mensajes SMS enviados. 
Cada vez que se llame al método enviar_mensaje(), el contador correspondiente deberá incrementarse. 

- Convierte la clase notificación en abstracta y añade un método mostrar_info() 
que cada clase derivada debe implementar mostrando el identificador, usuario y el número de
correos o sms enviados según corresponda.

- Define una clase estática SmartPhone cuyos atributos sean el nombre y apellidos del titular, 
el número de teléfono y una lista de notificaciones enviadas. Deberá tener dos funciones enviar_email() 
y enviar_sms() que pidan la información necesaria previa a invocar a la función enviar_mensaje() correspondiente.
 También deben guardar los mensajes en la lista.

Añade una función principal al que ofrezca de manera continuada al usuario enviar notificaciones y 
dependiendo del tipo de notificación elegido por el usuario mande un sms o un email. 

Al final del programa, se deben imprimir un resumen de los SMS y los Emails enviados, mostrando un listado de 
los mismos y la cantidad de cada uno de ellos.

Razona donde ubicas estas funciones y de qué tipo pueden ser.'''
#ESTO ES UN CAMBIO PARA LA PRACTICA 
#ESTE COMENTARIO HA SIDO HECHO POR AARON
from abc import ABC, abstractmethod

class Notificacion(ABC) : 
    def __init__(self, id, nombre):
        self.id = id
        self.nombre_usuario = nombre
        

    @abstractmethod
    def mostrar_info(self) :
        pass

    def __str__(self):
        return self.id +self.nombre_usuario

    @abstractmethod
    def mostrar_info(self) :
        pass

class Email(Notificacion) :
    contador_emails = 0

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def enviar_mensaje(self, dir_destinatario, asunto, contenido) :
        Email.contador_emails += 1
        mensaje = f'Enviando email con asunto: {asunto} a {dir_destinatario}...\n Contenido: {contenido}'
        SmartPhone.notificaciones_enviadas.append(mensaje)
        return mensaje
    
    def __str__(self):
        return super().__str__() + self.contador_emails 

    def mostrar_info(self) :
        return f'\nIdentificador: {self.id}\nNombre: {self.nombre_usuario}\nCorreos enviados: {self.contador_emails}'

class Sms(Notificacion) :
    contador_sms = 0

    def __init__(self, id, nombre):
        super().__init__(id, nombre)

    def enviar_mensaje(self, telefono, contenido) :
        Sms.contador_sms += 1
        mensaje = f'Enviando SMS al numero {telefono}...\n Contenido: {contenido}'
        SmartPhone.notificaciones_enviadas.append(mensaje)
        return mensaje
    
    def __str__(self):
        return super().__str__() + self.contador_sms

    def mostrar_info(self) :
        return f'\nIdentificador: {self.id}\nNombre: {self.nombre_usuario}\nSms enviados: {self.contador_sms}'
    
#- Define una clase estática SmartPhone cuyos atributos sean el nombre y apellidos del titular, 
#el número de teléfono y una lista de notificaciones enviadas. Deberá tener dos funciones enviar_email() 
#y enviar_sms() que pidan la información necesaria previa a invocar a la función enviar_mensaje() correspondiente.
#También deben guardar los mensajes en la lista.

class SmartPhone:
    nombre = 'Usuario'
    Apellidos = 'apellidos'
    telefono = '000000000'
    notificaciones_enviadas = []
    

    @staticmethod
    def enviar_Email() :
        nombre = input('Nombre: ')
        id_email = len(SmartPhone.notificaciones_enviadas) + 1
        destinatario = input('E-mail destinatario: ')
        asunto = input('Asunto: ')
        contenido = input('Contenido: ')
        email = Email(id_email, nombre)
        mensaje = email.enviar_mensaje(destinatario, asunto, contenido)
        SmartPhone.notificaciones_enviadas.append(mensaje)
        print('Email enviado.')

    @staticmethod
    def enviar_Sms() :
        nombre = input('Nombre: ')
        id_sms = len(SmartPhone.notificaciones_enviadas) + 1
        telefono = input('Número de teléfono: ')
        contenido = input('Mensaje: ')
        sms = Sms(id_sms, nombre)
        mensaje = sms.enviar_mensaje(telefono, contenido)
        SmartPhone.notificaciones_enviadas.append(mensaje)
        print('SMS enviado.')



def main() :
    
# Añade una función principal al que ofrezca de manera continuada al usuario enviar notificaciones y 
# dependiendo del tipo de notificación elegido por el usuario mande un sms o un email. 
    validacion = True
    while validacion:
        menu = ['Enviar e-mail', 'Enviar SMS', 'SALIR']
        for indice, elemento in enumerate(menu, start=1):
            print(f'{indice}. {elemento}.')
        respuesta = int(input('Acción: '))
        match respuesta:
            case 1:
                SmartPhone.enviar_Email()
            case 2:
                SmartPhone.enviar_Sms()
            case 3:
                print('Saliendo...')
                validacion = False
            case _:
                print('Opción no válida.')

    # Mostrar resumen de notificaciones enviadas.
    print('\n<<<Resumen de notificaciones enviadas>>>')
    email_info = Email(0, "").mostrar_info()
    sms_info = Sms(0, "").mostrar_info()
    print(email_info)
    print(sms_info)
    print('\n<<<Listado de notificaciones>>>')
    for notificacion in SmartPhone.notificaciones_enviadas:
        print(notificacion)

# Al final del programa, se deben imprimir un resumen de los SMS y los Emails enviados, mostrando un listado de 
# los mismos y la cantidad de cada uno de ellos.

main()



