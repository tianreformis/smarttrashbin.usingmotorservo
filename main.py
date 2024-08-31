#include <Servo.h>
#define SENSOR1 2 //infrared-induktif
#define SENSOR2 3 //infrared-kapasitif
#define SENSOR3 4  //induktif
#define SENSOR4 5 //kapasitif
#define ACTION1 12
#define ACTION2 13

bool value_red1;
bool value_red2;
bool value_induktif;
bool value_kapasitif;

Servo servo1; //servo induktif
Servo servo2; //servo kapasistif

void setup() {  
  Serial.begin(500);

  pinMode(SENSOR1, INPUT);
  pinMode(SENSOR2, INPUT);
  pinMode(SENSOR3, INPUT);
  pinMode(SENSOR4, INPUT);

  servo1.attach(ACTION1);
  servo2.attach(ACTION2); 
}

void loop() {
  

  value_red1 = digitalRead(SENSOR1);  //infrared-induktif
  value_red2 = digitalRead(SENSOR2);  //infrared-kapasitif
  value_induktif = digitalRead(SENSOR3);  //induktif
  value_kapasitif = digitalRead(SENSOR4);  //kapasitif


  if (value_red1 == 0){//deteksi sampah logam
    delay(1000);
    value_induktif = digitalRead(SENSOR3);
    value_red1 = digitalRead(SENSOR1); 

    if(value_induktif == 0){
      delay(1000);
      servo1.write(180);
      Serial.println(" Sampah Logam");
    } else{
      servo1.write(0);
      Serial.println(" Bukan Sampah Logam");
    } 
  } else{
    servo1.write(90); //servo standby
  }

if (value_red2 == 0){ //Sampah Organik/Anorganik
    delay(1000);
    value_kapasitif = digitalRead(SENSOR4);
    value_red2 == digitalRead(SENSOR2);

    if (value_kapasitif == 1){
      servo2.write(180);
      Serial.println(" Sampah Organik");
      } else {
        servo2.write(0);
        Serial.println(" Sampah Anorganik");
      }
    } else{
      servo2.write(90);
    } 
     if (value_red2 == 1 && value_kapasitif == 0 && value_induktif == 1){
    Serial.println("Masukkan  Sampah");
    }
