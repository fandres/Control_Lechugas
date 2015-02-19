# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:18:25 2014

@author: fAnDrEs (fabian.salamanca@openmailbox.org)

Licencia GPL V3
#! /usr/bin/python

"""


import sys    
# Importar modulo Qt
from PyQt4 import QtCore,QtGui
# Importar el código del modulo compilado UI
from controlUi import Ui_Form
# Importamos modulo pinguino & USB
import Pinguino
import usb


#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------
# Crear una clase para nuestra ventana principal
class Principal(QtGui.QFrame):
    def __init__(self):
        QtGui.QFrame.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #Centramos el frame
        self.centrar()
        # Conectamos la senal de click del boton (boton_conectar) con el metodo inicio
        #self.connect(self.ui.boton_conectar, QtCore.SIGNAL("clicked()"), self.inicio)
        
        #Solo debug visual
        self.inicio()
        
    def inicio(self):
        '''
        try :
            pass
        ##self.timer.start(500) #se ejecutará la self.temperatura() cada 500 mili segundos elf.myString # Debug
                
        except usb.USBError as err:
            pass
        '''
        self.SetAlarmaTempSuelo     = 25  
        self.SetAlarmaTempAire      = 30  
        self.SetAlarmahumedadSuelo  = 80  
        self.SetAlarmahumedadAire   = 60  
        
        # Seteo Alarmas
        self.ui.ui_termoTempS.setAlarmLevel(self.SetAlarmaTempSuelo) #Cambia el nivel de alarma [entero]
        self.ui.ui_termoTempA.setAlarmLevel(self.SetAlarmaTempAire) #Cambia el nivel de alarma [entero]
        self.ui.ui_termoHuS.setAlarmLevel(self.SetAlarmahumedadSuelo) #Cambia el nivel de alarma [entero]
        self.ui.ui_termoHuA.setAlarmLevel( self.SetAlarmahumedadAire) #Cambia el nivel de alarma [entero]
        # Si cumple la conexxcion
        self.setDatos()

    

        
        
        """ Metodos para qwtTermo """
        #self.ui.qwt_Thermo.setValue(40) # Asigna valor al elemento qwtThermo
        #self.ui.qwt_Thermo.setPipeWidth(20) # Cambia anchura del pipe(barar termomentro)
        #self.ui.qwt_Thermo.setAlarmLevel(50) #Cambia el nivel de alarma [entero]
        #self.ui.qwt_Thermo.setAlarmColor(QtGui.QColor(0, 177, 0)) # cambia el Color de la ararma
        #print self.ui.qwt_Thermo.alarmEnabled() # retorna True si la alarma esta activa

        # Cambio alarm Brush de alarm
        #brush = QtGui.QBrush(QtGui.QColor(0 , 0, 170))
        #brush.setStyle(QtCore.Qt.SolidPattern)
        #self.ui.qwt_Thermo.setAlarmBrush(brush)
        
        """Metodos QLCDNumber """
        #self.ui.lcdNumber_1.display(60) # Muestra un valor en el LCD
        # Sinal = overFlow
        #print self.ui.lcdNumber_1.value() # Recorta valor de QLCDNumber
        #print self.ui.lcdNumber_1.intValue() # Recorta valor de QLCDNumber en entero
        #self.ui.lcdNumber_1.setDisabled(True)# Desactiva el LCD
        #self.ui.lcdNumber_1.setNumDigits(1) # Numero de digitos que muestra el LCD
        #print self.ui.lcdNumber_1.numDigits()  # Numero de digitos que esta mostrando el LCD
        
        
        #self.connect(self.ui.qwt_Thermo, QtCore.SIGNAL(""))

#-------------------------------------------------------------------------------
    def centrar(self): # Centra el Frame 
            screen = QtGui.QDesktopWidget().screenGeometry() # obtiene resolucion del usuario
            size =  self.geometry() 
            self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
            
#-------------------------------------------------------------------------------
    def setDatos(self): # Adquisición de datos [Comunicación PC -]
        self.dataTemperaturaSuelo= 22
        self.dataTemperaturaAire = 0
        self.dataHumedadSuelo    = 60
        self.dataHumedadAire     = 0
        self.dataNivelTanque     = '1'

        self.determinarPincel()# Determina el COLOR de los QwThermo
        self.actuador() # Determina la accion para el actuador
        
        # Qwt-Thermo
        self.ui.ui_termoTempS.setAlarmBrush(QtGui.QColor(200, 0, 0)) # Color Alarma temperatura - suelo
        self.ui.ui_termoTempS.setValue(self.dataTemperaturaSuelo) # Asigna valor al elemento qwtThermo
        self.ui.ui_termoTempA.setAlarmBrush(QtGui.QColor(200, 0, 0)) # Color Alarma temperatura - Aire
        self.ui.ui_termoTempA.setValue(self.dataTemperaturaAire) # Asigna valor al elemento qwtThermo
        self.ui.ui_termoHuS.setAlarmBrush(QtGui.QColor(200, 0, 0)) # Color Alarma Humedad - suelo
        self.ui.ui_termoHuS.setValue(self.dataHumedadSuelo) # Asigna valor al elemento qwtThermo
        self.ui.ui_termoHuA.setAlarmBrush(QtGui.QColor(200, 0, 0)) # Color Alarma Gumedad - suelo
        self.ui.ui_termoHuA.setValue(self.dataHumedadAire) # Asigna valor al elemento qwtThermo
        # Dislay - QLCDNumber
        self.ui.ui_Display_tempS.display(self.dataTemperaturaSuelo)
        self.ui.ui_Display_tempA.display(self.dataTemperaturaAire)
        self.ui.ui_Display_huS.display(self.dataHumedadSuelo)
        self.ui.ui_Display_huA.display(self.dataHumedadAire)
        
        if (self.dataNivelTanque == '1'): self.ui.ui_nivelTanque.setText("LLENANDO...")
        elif (self.dataNivelTanque == '0'): self.ui.ui_nivelTanque.setText("LLENO")
        else: self.ui.ui_nivelTanque.setText("ERROR")
        
    
    def determinarPincel(self): # Determina el COLOR de los QwThermo
        # [Rojo, Verde, Azul]
        # 0  0   0
        # 0  0   ++
        # 0  ++  0
        # ++ ++  0
        # ++ 0   0
        rojo = 0; verde = 0; azul = 0
        if ((self.dataTemperaturaSuelo > 0) and (self.dataTemperaturaSuelo < self.SetAlarmaTempSuelo)):
            rojo = 0; verde = 0; azul = 192
            pincel = QtGui.QBrush(QtGui.QColor(rojo, verde, azul))
            pincel.setStyle(QtCore.Qt.SolidPattern)
            self.ui.ui_termoTempS.setFillBrush(pincel)
        if (self.dataTemperaturaAire > 0 and self.dataTemperaturaAire < self.SetAlarmaTempAire):
            rojo = 0; verde = 0; azul = 192
            pincel = QtGui.QBrush(QtGui.QColor(rojo, verde, azul))
            pincel.setStyle(QtCore.Qt.SolidPattern)
            self.ui.ui_termoTempA.setFillBrush(pincel)
        if ( self.dataHumedadSuelo > 0 and self.dataHumedadSuelo < 60):
            rojo = 200; verde = 0; azul = 0
            pincel = QtGui.QBrush(QtGui.QColor(rojo, verde, azul))
            pincel.setStyle(QtCore.Qt.SolidPattern)
            self.ui.ui_termoHuS.setFillBrush(pincel)
        if ( self.dataHumedadAire > 0 and self.dataHumedadAire < 50):
            rojo = 200; verde = 0; azul = 0
            pincel = QtGui.QBrush(QtGui.QColor(rojo, verde, azul))
            pincel.setStyle(QtCore.Qt.SolidPattern)
            print "hi"
            self.ui.ui_termoHuA.setFillBrush(pincel)
        else: rojo = 0; verde = 0; azul = 0
        
    def actuador(self):
        pass



#-------------------------------------------------------------------------------
def main():
    # Nuevamente, esto es estándar, será igual en cada
    # aplicación que escribas
    app = QtGui.QApplication(sys.argv)
    # Se crea una instancia de la clase
    ventana=Principal()
    # Se muestra el elemento en pantalla
    ventana.show()
    # Se ejecuta y expera a que termine la aplicación
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()