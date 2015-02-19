/*-----------------------------------------------------
Author:  --<fandres>
Date: 2014-04-03
Description: Adquiere informacion de un lm35 y lo envia a host.Pro
Programa Host [Python]: https://github.com/fandres/pyqwt-Temperatura-pinguino/tree/master/session5
                      :
-----------------------------------------------------*/


#include <stdlib.h>   // la necesitaremos para la función "itoa()"

char enviado[64];   // Cadena a ser enviada.
int entero = 0;     // Donde almacenamos temporalmente el valor leido.
int temp1, temp2, temp3;
char caracter[] = "T";
int largo;
// Sensores Temperatura
#define TEMPERATURA_1 13
#define TEMPERATURA_2 14
#define TEMPERATURA_3 15
// Sensores Humedad
#define HUMEDAD_1 16
#define HUMEDAD_2 17
#define HUMEDAD_3 18
// Sensores Nivel Agua
#define NIVELH2O_1 19
#define NIVELH2O_2 20
// Actuadores
#define EECTROBOMBA 21
#define BOMBARIEGO 22
//#define BOMBARIEGO 10


//-------------------------setup()---------------------//
void setup()
{
    // ANALOG - Sensores
    pinMode(TEMPERATURA_1, INPUT);  // pin 13 -> Temperatura 1
    pinMode(TEMPERATURA_2, INPUT);  // pin 14 -> Temperatura 2
    pinMode(TEMPERATURA_3, INPUT);  // pin 15 -> Temperatura 3
    pinMode(HUMEDAD_1, INPUT);      // pin 15 -> Humedad 1
    pinMode(HUMEDAD_2, INPUT);      // pin 16 -> Humedad 2
    pinMode(HUMEDAD_3, INPUT);      // pin 17 -> Humedad 3
    // DIGITAL - Sensores
    pinMode(NIVELH2O_1, INPUT);     // pin 18 -> Nivel Agua 1
    pinMode(NIVELH2O_2, INPUT);     // pin 18 -> Nivel Agua 2
    // DIGITAL - Actuadores
    pinMode(EECTROBOMBA, OUTPUT);     // pin 21-> ElectroBomba
    pinMode(BOMBARIEGO, OUTPUT);      // pin 22-> Bomba Riego  
    //pinMode(VENTILADORES, OUTPUT);      // pin 10-> Ventiladores    
}
//-------------------------loop()---------------------//
void loop()
{
    //    TEMPERATURA     
    temp1 = analogRead(TEMPERATURA_1);    // Leyendo valor de sensor de Temperatura 1
    temp2 = analogRead(TEMPERATURA_2);    // Leyendo valor de sensor de Temperatura 2 
    temp3 = analogRead(TEMPERATURA_3);    // Leyendo valor de sensor de Temperatura 23
    //entero  = (temp1 + temp2 + temp3) / 3;  // Promedio entre las temperaturas
    entero += 1;  // Debug
    itoa(entero,enviado,10);    // Conversión de int a string
    largo = strlen(enviado); 
    if (largo == 1){
        enviado[1] = 'T';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    else if(largo == 2){
        enviado[2] = 'T';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    else if (largo == 3){
        enviado[3] = 'T';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    else if(largo == 4){
        enviado[4] = 'T';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    //if (entero  >= 120) digitalWrite(VENTILADORES, HIGH); // 819 = 80% Humedad
    //else digitalWrite(VENTILADORES, LOW);
    delay(33);
    
    //HUMEDAD
    temp1 = analogRead(HUMEDAD_1);    // Leyendo valor de sensor del Humedad 1
    temp2 = analogRead(HUMEDAD_2);    // Leyendo valor de sensor del Humedad 2 
    temp3 = analogRead(HUMEDAD_3);    // Leyendo valor de sensor del Humedad 3 
    //entero  = (temp1 + temp2+ temp3)/3;  // Promedio de los sensores de humedad
    entero += 1;  // Debug
    itoa(entero,enviado,10);    // Conversión de int a string
    largo = strlen(enviado); 
    if (largo == 1){
        enviado[1] = 'H';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    else if(largo == 2){
        enviado[2] = 'H';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    else if (largo == 3){
        enviado[3] = 'H';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    else if(largo == 4){
        enviado[4] = 'H';       // Formatea el String a enviar 
        BULK.write(enviado, largo+1);    // Enviado los datos al host
    }
    if (entero  >= 819) digitalWrite(BOMBARIEGO, HIGH); // 819 = 80% Humedad
    else digitalWrite(BOMBARIEGO, LOW);
    delay(33);
    
    //NIVEL
    if ((digitalRead(NIVELH2O_1) == 1) && (digitalRead(NIVELH2O_2) == 0)){
        digitalWrite(EECTROBOMBA, HIGH);
        BULK.write("A", 1);// Enviado los datos al host 1
    } 
    else if ((digitalRead(NIVELH2O_1) == 1) && (digitalRead(NIVELH2O_2) == 1)){
        digitalWrite(EECTROBOMBA, LOW);
        BULK.write("B", 1);// Enviado los datos al host 0
    }
    else BULK.write("E", 1);// Enviado los datos al host E
    delay(33);
}
