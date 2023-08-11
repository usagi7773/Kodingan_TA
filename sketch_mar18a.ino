//Library fingerprint dependency
#include <Adafruit_Fingerprint.h>
String servoState;

#include <Servo.h>
Servo myServo;

#if (defined(__AVR__) || defined(ESP8266)) && !defined(__AVR_ATmega2560__)
// For UNO and others without hardware serial, we must use software serial...
// pin #2 is IN from sensor (PURPLE wire)
// pin #3 is OUT from arduino  (WHITE wire)
// Set up the serial port to use softwareserial..
SoftwareSerial mySerial(2, 3);

#else
// On Leonardo/M0/etc, others with hardware serial, use hardware serial!
// #0 is green wire, #1 is white
#define mySerial Serial1

#endif

Adafruit_Fingerprint finger = Adafruit_Fingerprint(&mySerial);



//Assign the correspondenceidUser to raspberry pi
void getUrl(int idUser){
  switch(idUser){
    case 1: Serial.println("1"); break;
    case 2: Serial.println("2"); break;
    case 3: Serial.println("3"); break;
    case 4: Serial.println("4"); break;
    case 5: Serial.println("5"); break;
    case 6: Serial.println("6"); break;
    case 7: Serial.println("7"); break;
    case 8: Serial.println("8"); break;
    case 9: Serial.println("9"); break;
    case 10: Serial.println("10"); break;
    default: Serial.println("10"); break;
    
  }

}

//Servo flushing
void serFlush() {
//  digitalWrite(13, HIGH);
//  delay(1000);
//  digitalWrite(13, LOW);
//  delay(1000);
//  digitalWrite(13, HIGH);
//  delay(1000);
//  digitalWrite(13, LOW);
//  delay(1000);
//  digitalWrite(13, HIGH);
//  delay(1000);
//  digitalWrite(13, LOW);
  myServo.write(0);
  delay(1000); // Wait for 1 second
  myServo.write(180);
  delay(1000);
  myServo.write(0);
}

void setup()
{
  myServo.attach(5);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
  while (!Serial);  // For Yun/Leo/Micro/Zero/...
  delay(100);


  // set the data rate for the sensor serial port
  finger.begin(57600);
  delay(5);
  if (finger.verifyPassword()) {
//    Serial.println("Found fingerprint sensor!");
  } else {
//    Serial.println("Did not find fingerprint sensor :(");
    while (1) { delay(1); }
  }

  finger.getParameters();
  finger.getTemplateCount();

  if (finger.templateCount == 0) {

  }
  else {

  }
}

void loop()   //run over and over again
{
  // Read signal state from raspy
  getFingerprintID();
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  servoState = Serial.readStringUntil('\n');
  Serial.println(servoState);
  servoState.trim();
  if (servoState.equals("off")) {
    Serial.flush();
    serFlush();
  }
  if(servoState.equals("uploaded")){
    digitalWrite(11, HIGH);
    delay(2000);
    digitalWrite(11, LOW);
  }
  delay(200); //don't ned to run this at full speed.
}

uint8_t getFingerprintID() {
  
  uint8_t p = finger.getImage();
  p = finger.image2Tz();

  // OK converted!
  p = finger.fingerSearch();
  if (p == FINGERPRINT_OK) {
//    Serial.println("Found a print match!");
  } else if (p == FINGERPRINT_PACKETRECIEVEERR) {
//    Serial.println("Communication error");
    return p;
  } else if (p == FINGERPRINT_NOTFOUND) {
//    Serial.println("Did not find a match");
    return p;
  } else {
//    Serial.println("Unknown error");
    return p;
  }

  // found a match!
  getUrl(finger.fingerID);
  digitalWrite(12, HIGH);
  delay(2000);
  digitalWrite(12, LOW);
  return finger.fingerID;
}

// returns -1 if failed, otherwise returns ID #
int getFingerprintIDez() {
  uint8_t p = finger.getImage();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.image2Tz();
  if (p != FINGERPRINT_OK)  return -1;

  p = finger.fingerFastSearch();
  if (p != FINGERPRINT_OK)  return -1;

  return finger.fingerID;
}
