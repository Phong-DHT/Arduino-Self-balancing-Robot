#include <SoftwareSerial.h>
 
#define TX_PIN      7
#define RX_PIN      6
 
SoftwareSerial bluetooth(RX_PIN, TX_PIN);
int baudRate[] = {300, 1200, 2400, 4800, 9600, 19200, 38400, 57600, 115200};
const int trig = 13;     // chân trig của HC-SR04
const int echo = 12; 
int data = 0; 
char userInput;

void setup() {
  Serial.begin(9600);
  pinMode(trig,OUTPUT);   // chân trig sẽ phát tín hiệu
  pinMode(echo,INPUT);    // chân echo sẽ nhận tín hiệu
  while (!Serial) {}
  
  Serial.println("Configuring, please wait...");
  
  for (int i = 0 ; i < 9 ; i++) {
     bluetooth.begin(baudRate[i]);
     String cmd = "AT+BAUD4";
     bluetooth.print(cmd);
     bluetooth.flush();
     delay(100);
  }
  
  bluetooth.begin(9600);
  Serial.println("Config done");
  while (!bluetooth) {}
  
  Serial.println("Enter AT commands:");
}
 
void loop() {
  unsigned long duration; // biến đo thời gian
  int distance;           // biến lưu khoảng cách
  
  /* Phát xung từ chân trig */
  digitalWrite(trig,0);   // tắt chân trig
  delayMicroseconds(2);
  digitalWrite(trig,1);   // phát xung từ chân trig
  delayMicroseconds(5);   // xung có độ dài 5 microSeconds
  digitalWrite(trig,0);   // tắt chân trig
    
  /* Tính toán thời gian */
  // Đo độ rộng xung HIGH ở chân echo. 
  duration = pulseIn(echo,HIGH);  
  // Tính khoảng cách đến vật.
  distance = int(duration/2/29.412);
    
  /* In kết quả ra Serial Monitor */
  Serial.print(distance);
  Serial.println("cm");
  delay(200);
  //if (bluetooth.available()) {
  //  Serial.write(bluetooth.read());
  //}
  if (Serial.available()) {
    userInput = bluetooth.read();
    if(userInput == 'g'){
      data = distance;
      bluetooth.println(data);
    }
  }
}