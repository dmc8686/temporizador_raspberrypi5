#tkinter-22
titulo ='''
###########################################
Este programa controla un rele en el
pin11 GPIO17
Muestra hora real
Pide ingresar minutos por consola
Tiene boton de inicio de temporizador
Tiene boton de apagado de rele

imprime cada vez que pasa un minuto

AUTHOR: diegocarrizo85@gmail.com
###########################################
'''
print(titulo)

import tkinter as tk
import time
from gpiozero import LED

led = LED(17) # corresponde al pin11

#variables globales
minuto_programado = 50
bandera_contando = False
bandera_minuto_mostrado = False
minuto_mostrado = 0
mensaje_mostrado = False

#inicializo el rele apagado
led.off()

#tiempo inicial
tiempo_inicial_segundos = time.time()

print("programa activo esperando orden")
minuto_programado = int(input("Ingrese los minutos a contar: "))

######################################################
#todas las funciones
######################################################
def resetear_tiempo():
    global tiempo_inicial_segundos
    tiempo_inicial_segundos = time.time()
    
def boton_encendido():
    global bandera_contando
    global mensaje_mostrado
    global minuto_programado
    
    mensaje_mostrado = False
    resetear_tiempo()
    print(f"Inicio Contador a {minuto_programado} minutos!")
    hora_de_inicio = time.strftime("%H:%M:%S")
    print(f"Hora de Inicio: {hora_de_inicio}")
    etiqueta_estado.config(text=f"Rele Encendido\n..Inicio Contador a {minuto_programado} minutos..")
    led.on()
    bandera_contando = True

def boton_apagado():
    global bandera_contando
    print("Rele Apagado Manualmente")
    led.off()
    etiqueta_estado.config(text="Rele Apagado\n..Apagado Manualmente..")
    bandera_contando = False

def b_set30():
    global minuto_programado
    minuto_programado = 30
    botonOn.config(text=f">Iniciar Contador a {minuto_programado} minutos<")
    print("Set30\n..Función ejecutada..")
    etiqueta_estado.config(text="Set30\n..Función ejecutada..")

def b_set45():
    global minuto_programado
    minuto_programado = 45
    botonOn.config(text=f">Iniciar Contador a {minuto_programado} minutos<")
    print("Set45\n..Función ejecutada..")
    etiqueta_estado.config(text="Set45\n..Función ejecutada..")

def b_set90():
    global minuto_programado
    minuto_programado = 90
    botonOn.config(text=f">Iniciar Contador a {minuto_programado} minutos<")
    print("Set90\n..Función ejecutada..")
    etiqueta_estado.config(text="Set90\n..Función ejecutada..")
#############################################################################

ventana = tk.Tk()
ventana.title("Rele Temporizado en GPIO 17")
ventana.geometry("810x950+1095+200")#tamano y posicion (aumenté la altura para los nuevos botones)
ventana.configure(bg="lightblue")

etiquetaArriba = tk.Label(ventana,
                          text = "Hora Real",
                          width = 20,
                          height = 2)
etiquetaArriba.config(fg="black",bg="yellow",font=("Arial",50,"bold"))
etiquetaArriba.pack(pady=10)

etiqueta = tk.Label(ventana, text = "Iniciando Reloj..",
                          width = 20,
                          height = 2)
etiqueta.config(fg="blue",bg="yellow",font=("Arial",50,"bold"))
etiqueta.pack(pady=10)

botonOn = tk.Button(ventana,
                    text=f">Iniciar Contador a {minuto_programado} minutos<",
                    width=40,
                    height=1,
                    font=("Arial",20)
                    )
botonOn.config(command=boton_encendido)#indica funcion
botonOn.pack(pady=10)

botonOff = tk.Button(ventana,text=">Apagar Rele y Contador<",
                     width=40,
                     height=1,
                     font=("Arial",20)
                     )
botonOff.config(command=boton_apagado)#indica funcion
botonOff.pack(pady=10)

labelframeestado = tk.LabelFrame(ventana,
                                 text="estado:",
                                 padx=10,
                                 pady=10,
                                 font=("Arial", 16)
                                 )
labelframeestado.pack(pady=5)

etiqueta_estado = tk.Label(labelframeestado,
                           text = "estado..",
                           )
etiqueta_estado.config(fg="black",
                       bg="cyan",
                       font=("Arial",30,"bold")
                       )
etiqueta_estado.pack(pady=10)

# Frame para contener los tres botones horizontales
frame_botones_horizontales = tk.Frame(ventana, bg="lightblue")
frame_botones_horizontales.pack(pady=10)

# Crear los tres botones horizontales
boton_set30 = tk.Button(frame_botones_horizontales,
                             text="Set30",
                             width=15,
                             height=1,
                             font=("Arial", 18))
boton_set30.config(command=b_set30, bg="lightgreen")
boton_set30.pack(side=tk.LEFT, padx=5)

boton_set45 = tk.Button(frame_botones_horizontales,
                             text="Set45",
                             width=15,
                             height=1,
                             font=("Arial", 18))
boton_set45.config(command=b_set45, bg="lightcoral")
boton_set45.pack(side=tk.LEFT, padx=5)

boton_set90 = tk.Button(frame_botones_horizontales,
                             text="Set90",
                             width=15,
                             height=1,
                             font=("Arial", 18))
boton_set90.config(command=b_set90, bg="lightyellow")
boton_set90.pack(side=tk.LEFT, padx=5)

botonCerrar = tk.Button(ventana,text="cerrar",
                        width=40,
                        height=1,
                        font=("Arial",20)
                        )
botonCerrar.config(command=ventana.destroy)#indica funcion
botonCerrar.pack(pady=10)

#llamo a resetear tiempo
resetear_tiempo()

#funcion
def actualizar_tiempo():
    global bandera_contando
    global bandera_minuto_mostrado
    global minuto_mostrado
    global tiempo_inicial_segundos
    global mensaje_mostrado
    
    etiqueta.config(text=time.strftime("%H:%M:%S"))
    #hora_actual = time.strftime("%H")
    #minuto_actual = time.strftime("%M")
    tiempo_actual_segundos = time.time() 
    tiempo_transcurrido_segundos = tiempo_actual_segundos-tiempo_inicial_segundos
    minuto_transcurrido = int(tiempo_transcurrido_segundos // 60)
    
    
    if bandera_contando == True:
        
        if minuto_transcurrido != minuto_mostrado:
            print(f"minuto_transcurrido: {minuto_transcurrido}")
            #
            etiqueta_estado.config(text=f"Rele Encendido\n..minuto_transcurrido: {minuto_transcurrido}..")
            #
            bandera_minuto_mostrado = True
            minuto_mostrado = minuto_transcurrido
        else:
            bandera_minuto_mostrado = False
        
    if (bandera_contando == True) and (minuto_transcurrido >= minuto_programado):
        led.off()
        bandera_contando = False
        if not mensaje_mostrado:#false
            print('rele apagado por tiempo transcurrido')
            etiqueta_estado.config(text=f"Rele Apagado\n..por tiempo transcurrido: {minuto_transcurrido} minutos..")
            mensaje_mostrado = True 
    
    ventana.after(1000,actualizar_tiempo) #esta linea actualiza cada un segundo


actualizar_tiempo()

etiqueta_estado.config(text="Rele Apagado\n..programa activo esperando orden..")

ventana.mainloop()
print("Programa Terminado")