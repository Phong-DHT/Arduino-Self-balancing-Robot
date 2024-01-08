#include <TimerOne.h>
#include <SimpleKalmanFilter.h>
#include <SoftwareSerial.h>
#include <MPU6050_tockn.h>
#include <Wire.h>

#define TX_PIN 6
#define RX_PIN 5
#define enB 3
#define enA 11
#define in1 10
#define in2 9
#define in3 8
#define in4 7

SoftwareSerial bluetooth(RX_PIN, TX_PIN);
SimpleKalmanFilter locnhieu(2,2,0.01);
MPU6050 mpu6050(Wire);

//////---------------------------ANGLE--------------------------//////
float angle, angle_output, total_angle_input, last_angle, e_angle, setpoint = 0;
float Kp_a = 70; //60
float Ki_a = 700; //600
float Kd_a = 9; //6
//////----------------------------------------------------------//////


//////---------------------------POSITION-----------------------//////
float pos, pos_output, total_pos_input, last_pos, pos_setpoint, e_pos;
float Kp_p = 1;
float Ki_p = 10;
float Kd_p = 0.001;
float xung;
//////----------------------------------------------------------//////

float total_output;
float T = 0.01;




unsigned long prevTime = millis();
char userInput = 'n';

/*void Demxung(){
  if(digitalRead(4) == LOW) xung++;
  else xung--;
}*/

void right(){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(enB,255);
  analogWrite(enA,255);
}

void left(){
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(enB,255);
  analogWrite(enA,255);
}

void back(){
  digitalWrite(in1,HIGH);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,HIGH);
  analogWrite(enB,abs(total_output));
  analogWrite(enA,abs(total_output));
}

void go(){
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  digitalWrite(in3,HIGH);
  digitalWrite(in4,LOW);
  analogWrite(enB,abs(total_output));
  analogWrite(enA,abs(total_output));
}

void stop(){
  digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
  digitalWrite(in3,LOW);
  digitalWrite(in4,LOW);
  analogWrite(enB,0);
  analogWrite(enA,0);
}

void control(){
  if (userInput != 'n'){
    if (userInput == 'f'){
      forward();
    }
    else if(userInput == 's'){
      setpoint = 0;
    }
    else if(userInput == 'b'){
      setpoint = -1.5;
    }
    else if(userInput == 'l'){
      left();
    }
    else if(userInput == 'r'){
      right();
    }
    userInput = 'n';
  }
}

void PID(){
  
  //////---------------------------ANGLE--------------------------//////
  angle = locnhieu.updateEstimate(mpu6050.getAngleY());
  //Serial.println(angle);
  angle = setpoint - angle + e_angle;
  total_angle_input += angle;
  total_angle_input = constrain(total_angle_input, -350, 350);
  angle_output = angle*Kp_a + Ki_a*total_angle_input*T + Kd_a*(angle - last_angle) / T;
  last_angle = angle;
  //////----------------------------------------------------------//////

 /* //////---------------------------POSITION-----------------------//////
  pos = xung*360 / 514.8;
  pos = constrain(pos, -360, 360);
  e_pos = pos_setpoint - pos;
  total_pos_input += e_pos;
  total_pos_input = constrain(total_pos_input, -255, 255);
  pos_output = e_pos*Kp_p + Ki_p*total_pos_input*T + Kd_p*(e_pos - last_pos) / T;
  last_pos = e_pos;
  //////----------------------------------------------------------//////
*/

  total_output = angle_output;
  //Serial.println(total_output);

  //////---------------------------CONTROL-----------------------//////
  if(total_output > 0){
    total_output = constrain(total_output, 0, 255);
    go();
  }
  else if(total_output < 0){
    total_output = constrain(total_output, -255, 0);
    back();
  }
  else stop();
  //////---------------------------------------------------------//////
  control();
}

void setup(){
  TCCR2B = TCCR2B & B11111000 | B00000001;
  Serial.begin(115200);
  bluetooth.begin(9600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
  for(int i=7;i<12;i++) pinMode(i,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(2,INPUT_PULLUP);
  pinMode(4,INPUT_PULLUP);

  //pos = 0; xung = 0; last_pos = 0; total_pos_input = 0; pos_setpoint = 0;
  last_angle = 0; total_angle_input = 0; e_angle = -5;

  //attachInterrupt(0, Demxung, FALLING);
  Timer1.initialize(10000);
  Timer1.attachInterrupt(PID);
}

void loop(){
  mpu6050.update();
  unsigned long currentTime = millis();
  if (currentTime - prevTime > 50){
      bluetooth.println(-angle);
      userInput = bluetooth.read();
      prevTime = currentTime;
  }
}
