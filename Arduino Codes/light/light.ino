int lightPin=0;
int ledPin=2;
int val;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ledPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
val=analogRead(lightPin);
Serial.print("Lux=");
Serial.print(val);
Serial.println();
delay(800);
if(val<100)
{Serial.println("Dark");}
else if (val<200)
{Serial.println("less Dark");}
else if (val<300)
{Serial.println("Normal");}
else if (val<400)
{Serial.println("Lit");}
else if (val<500)
{Serial.println("Bright");}
else
{Serial.println("very Bright");}}


