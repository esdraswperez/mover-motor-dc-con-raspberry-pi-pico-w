from machine import Pin
import utime

# Entradas para el módulo Puente H L298N de 2 canales
in1 = Pin(19, Pin.OUT)
in2 = Pin(18, Pin.OUT)

while True:
    """
    Apaga las dos entradas dejando al motor 
    sin movimiento por un segundo
    """
    in1.value(0)
    in2.value(0)
    utime.sleep(1)
    
    """
    Apaga la entrada 1 y enciende la entrada 2 girando el motor
    en una dirección pausando por un segundo
    """
    in1.value(0)
    in2.value(1)
    utime.sleep(1)
    
    """
    Apaga la entrada 2 y enciende la entrada 1 girando el motor
    en dirección contraria pausando por un segundo
    """
    in1.value(1)
    in2.value(0)
    utime.sleep(1)
    
    """
    Espera un segundo antes de realizar el proceso de rotación
    """
    in1.value(1)
    in2.value(1)
    utime.sleep(1)