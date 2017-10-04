int sensorPin = A0;  
int sensorValue = 0; 
float percent=0; 
char input;
#define N 31
int i;

void setup() {
  Serial.begin(9600);
}

void loop() {
  printValuesToSerial();
  /*if (Serial.available()) {
    input = Serial.read();
    if (input=='5') {
      printValuesToSerial();
    }
    Serial.println(-1);
  }*/
}

int convertToPercent(int value)
{
  int percentValue = 0;
  percentValue = map(value, 1023, 465, 0, 100);
  return percentValue;
}

void printValuesToSerial()
{
  for (i=0; i<N; i++) {
    sensorValue = analogRead(sensorPin);
    percent = convertToPercent(sensorValue);
    Serial.println(percent);
  }
}

