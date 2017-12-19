/*This sketch is to turn ON/OFF relay shield which is connected to an etension
 * cord
 * for Christmas tree lights or whatever I want to turn on/off remotely
 */

#include <ESP8266WiFi.h>
#define lightPin 0 // Initialise Analogue Pin


//  CONNECT TO WLAN
const char* ssid = "NOWTV659CD";//*****************************
const char* password = "PVQRWBCDPV";//****************

//  CREATE WEBSERVER
WiFiServer server(80);

int read1 = 0;
int read2 = 0;
int read3 = 0;
int readVal = 0;
int lightOn = 0;

void setup() {

  Serial.begin(115200);          //IN CASE I WANT TO USE ONBOARD LED
  delay(10);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  IPAddress ip(192, 168, 0, 111);
  IPAddress gateway(192, 168, 0, 1);
  IPAddress subnet(255, 255, 255, 0);
  WiFi.config(ip, gateway, subnet);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

  // Start the server
  server.begin();
  Serial.println("Server started");

  // Print the IP address
  Serial.print("Use this URL to connect: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");

}

void loop() {
  // Check if a client has connected
  WiFiClient client = server.available();
  if (!client) {
    return;
  }

  // Wait until the client sends some data
  Serial.println("new client");
  while (!client.available()) {
    delay(1);
  }

  // Read the first line of the request
  String request = client.readStringUntil('\r');
  Serial.println(request);
  client.flush();

  if (request.indexOf("GetLDR") != -1) {
    read1 = (analogRead(lightPin)); // Write the value.
    delay(10);
    read2 = (analogRead(lightPin)); // Write the value.
    delay(10);
    read3 = (analogRead(lightPin)); // Write the value.
    readVal = (read1 + read2 + read3)/3;
  }

  client.println(readVal);
  
  //Serial.println(readVal); // Write the value.
  //delay(20);

  // Check client
//  WiFiClient client = server.available();
//  if (client) {
//    Serial.println("new client");
//    boolean currentLineIsBlank = true;
//    while (client.connected()) {
//      if (client.available()){
//        char c = client.read();
//        Serial.write(c);
//        if (c == '\n' && currentLineIsBlank) {
//          // Return the response
//          client.println("HTTP/1.1 200 OK");
//          client.println("Content-Type: text/html");
//          client.println("Connection: close"); //  do not forget this one
//          client.println("Refresh: 5");
//          client.println();
//          client.println("<!DOCTYPE HTML>");
//          client.println("<html>");
//          client.print("Sensor reading is: ");
//          client.print(readVal);
//          client.println("<br />");
//          //if ((lightOn == 0) & (readVal < 500)){
//          if (readVal < 500){
//            lightOn = 1;
//            Serial.println(readVal); // Write the value.
//            Serial.println("The Lights Need Turning On!"); // Write the value.
//            client.print("The Lights Need Turning On!");
//            client.println("<br />");
//          }
//          //if ((lightOn == 1) & (readVal > 1000)){
//          if (readVal > 500){
//            lightOn = 0;
//            Serial.println(readVal); // Write the value.
//            Serial.println("The Lights Need Turning Off!"); // Write the value.
//            client.print("The Lights Need Turning Off!");
//            client.println("<br />");
//          }
//          
//          client.println("</html>");
//          break;
//        }
//        if (c == '\n') {
//          // you're starting a new line
//          currentLineIsBlank = true;
//        } 
//        else if (c != '\r') {
//          // you've gotten a character on the current line
//          currentLineIsBlank = false;
//        }
//      }
//    }
//    delay(1);
//    client.stop();
//    Serial.println("client disconnected");
//  }
  
}

