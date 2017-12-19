#!/usr/bin/env python

def LightOn():

  import socket
  import sys
  
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Connect the socke to the port where the server is listening
  server_address = ('192.168.0.107', 80)
  print >>sys.stderr, 'connecting to %s port %s' % server_address
  sock.connect(server_address)
  
  try:
      # Send data
      message= '/gpio/1'
      print >>sys.stderr, 'sending "%s"' % message
      sock.sendall(message)
  
      # Look for the respomse
      amount_received = 0
      amount_expected = len(message)
  
      while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          print >>sys.stderr, 'received "%s"' % data
  
  finally:
      print >>sys.stderr, 'closing socket'
      sock.close()
  
def LightOnIP(ipAddress):

  import socket
  import sys
  
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Connect the socke to the port where the server is listening
  server_address = (ipAddress, 80)
  print >>sys.stderr, 'connecting to %s port %s' % server_address
  sock.connect(server_address)
  
  try:
      # Send data
      message= '/gpio/1'
      print >>sys.stderr, 'sending "%s"' % message
      sock.sendall(message)
  
      # Look for the respomse
      amount_received = 0
      amount_expected = len(message)
  
      while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          print >>sys.stderr, 'received "%s"' % data
  
  finally:
      print >>sys.stderr, 'closing socket'
      sock.close()

def LightOff():
  
  import socket
  import sys
  
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Connect the socke to the port where the server is listening
  server_address = ('192.168.0.107', 80)
  print >>sys.stderr, 'connecting to %s port %s' % server_address
  sock.connect(server_address)
  
  try:
      # Send data
      message= '/gpio/0'
      print >>sys.stderr, 'sending "%s"' % message
      sock.sendall(message)
  
      # Look for the respomse
      amount_received = 0
      amount_expected = len(message)
  
      while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          print >>sys.stderr, 'received "%s"' % data
  
  finally:
      print >>sys.stderr, 'closing socket'
      sock.close()
  
def LightOffIP(ipAddress):
  
  import socket
  import sys
  
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Connect the socke to the port where the server is listening
  server_address = (ipAddress, 80)
  print >>sys.stderr, 'connecting to %s port %s' % server_address
  sock.connect(server_address)
  
  try:
      # Send data
      message= '/gpio/0'
      print >>sys.stderr, 'sending "%s"' % message
      sock.sendall(message)
  
      # Look for the respomse
      amount_received = 0
      amount_expected = len(message)
  
      while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          print >>sys.stderr, 'received "%s"' % data
  
  finally:
      print >>sys.stderr, 'closing socket'
      sock.close()
 
def CheckLDR(ipAddress):
  
  import socket
  import sys
  
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  
  # Connect the socke to the port where the server is listening
  server_address = (ipAddress, 80)
  print >>sys.stderr, 'connecting to %s port %s' % server_address
  sock.connect(server_address)
  
  try:
      # Send data
      message= 'GetLDR'
      print >>sys.stderr, 'sending "%s"' % message
      sock.sendall(message)
  
      # Look for the respomse
      amount_received = 0
      amount_expected = 1
  
      while amount_received < amount_expected:
          data = sock.recv(4)
          amount_received += len(data)
          print >>sys.stderr, 'received "%s"' % data
  
  finally:
      print >>sys.stderr, 'closing socket'
      sock.close()
  return str(data)
  

def CheckIP():
  
  import socket
  import sys

#  ip_address_up = []
#  
#  addr_range = "192.168.0.%d"
#  
#  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#  
#  s.settimeout(2.0)
#  
#  for i in range(1, 254):
#      try:
#          #ip = addr_range % i
#          ip = "192.168.0." + str(i)
#          socket.gethostbyaddr(ip)
#          ip_address_up.append(ip)
#      except socket.herror as ex:
#          pass
#  
#  print ip_address_up
  
  # Create a TCP/IP socket
  #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  addFound = [];
  
  # Connect the socket to the port where the server is listening
  for ipAddress in range(100,120):
    try:
      # Create a TCP/IP socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      sock.settimeout(2.0)
      server_address = ("192.168.0." + str(ipAddress), 80)
      print >>sys.stderr, 'connecting to %s port %s' % server_address
      sock.connect(server_address)
      
      try:
          # Send data
          message= '/gpio/0'
          print >>sys.stderr, 'sending "%s"' % message
          sock.sendall(message)
      
          # Look for the respomse
          amount_received = 0
          amount_expected = len(message)
      
          while amount_received < amount_expected:
              data = sock.recv(16)
              amount_received += len(data)
              print >>sys.stderr, 'received "%s"' % data

          if data == "I'm a Light Bulb":
              addFound.append("192.168.0." + str(ipAddress))
      
      finally:
          print >>sys.stderr, 'closing socket'
          sock.close()
    except socket.error as ex:
        pass


  print addFound
  return addFound
  

