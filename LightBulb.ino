/*This sketch is to turn ON/OFF relay shield which is connected to an etension
 * cord
 * for Christmas tree lights or whatever I want to turn on/off remotely
 */

#include <ESP8266WiFi.h>
#define relayPin 5//  Initialize D1 aka GPIO-5 as an output on the WeMOS board


//  CONNECT TO WLAN
const char* ssid = "NOWTV659CD";//*****************************
const char* password = "PVQRWBCDPV";//****************

int ledPin = 2; // assign pin 2 for LED (GPIO2);
int value;
//  CREATE WEBSERVER
WiFiServer server(80);


void setup() {
//  pinMode(LED_BUILTIN, OUTPUT);  // Initialize the LED_BUILTIN pin as an output

  pinMode(relayPin, OUTPUT);     // Initialize the D1 aka GPIO5 as an output



  Serial.begin(115200);          //IN CASE I WANT TO USE ONBOARD LED
  delay(10);


  pinMode(ledPin, OUTPUT);
  digitalWrite(ledPin, LOW);

  // Connect to WiFi network
  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  IPAddress ip(192, 168, 0, 107);
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

  int value = LOW;

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

  // Match the request

  //int value = LOW;
  if (request.indexOf("/LED=ON") != -1) {
    //digitalWrite(ledPin, LOW);
    digitalWrite(relayPin, HIGH);   // Turn the RELAY on (Note the Relay is active high
    value = HIGH;
  }
  if (request.indexOf("/LED=OFF") != -1) {
    //digitalWrite(ledPin, HIGH);
    digitalWrite(relayPin, LOW);   // Turn the RELAY on (Note the Relay is active high
    value = LOW;
  }
  if (request.indexOf("/gpio/1") != -1) {
    //digitalWrite(ledPin, LOW);
    digitalWrite(relayPin, HIGH);   // Turn the RELAY on (Note the Relay is active high
    value = HIGH;
  }
  if (request.indexOf("/gpio/0") != -1) {
    //digitalWrite(ledPin, HIGH);
    digitalWrite(relayPin, LOW);   // Turn the RELAY on (Note the Relay is active high
    value = LOW;
  }  

  // Set ledPin according to the request
  digitalWrite(ledPin, value);


  // Return the response
  //client.println("HTTP/1.1 200 OK");
  client.println("I'm a Light Bulb!");
  
  client.println("Content-Type: text/html");
  client.println(""); //  do not forget this one
  client.println("<!DOCTYPE HTML>");
  client.println("<html>");

  client.println("Hello Hal.  Nice weather we're having!<br>");
  client.println("What can I do for you today?<br>");
  client.println("By the way, your tree lights are ");


  if (value == LOW) {
    client.print("<b>On.");
  } else {
    client.print("<b>Off.");
  }
  client.println("<center><HR><BR>");
  client.println("<a href=\"/LED=ON\"><button>ON<\button></a><br><br>");

  client.println("<a href=\"/LED=OFF\"><button>OFF<\button></a><br>");
  client.println("</html>");

  delay(1);
  Serial.println("Client disconnected");
  Serial.println("");

}
