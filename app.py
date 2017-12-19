#!/usr/bin/python
from flask import Flask, request, url_for, render_template, redirect, json

#from flaskext.mysql import MySQL
from flaskext.mysql import MySQL

from multiprocessing import Process

import logging
import sys
sys.path.insert(0, 'static')
from sendDataOn import LightOn
from sendDataOff import LightOff
from sendData import LightOnIP, LightOffIP, CheckIP, CheckLDR
import threading
import time
import datetime

pill2kill = threading.Event()
workers = []


#class myThread1(threading.Thread):
#    def __init__(self):
#        threading.Thread.__init__(self)
#        self.board = 1
#
#    def mythread1(self, stop):
#        while 1:
#            if stop():
#                print("Exiting thread")
#                break
#            ldrvalue = CheckLDR("192.168.0.111")
#            #conn = mysql.connect()
#            #cur = conn.cursor()
#            #cur.execute("""insert into devices (device_name,device_type,device_ip) values(%s,%s,%s)""", (_name,_typeDD,_ipDD))
#            #conn.commit()
#            f = open('LDRValueFile.txt', 'w')
#            f.write(str(ldrvalue))
#            f.close()
#            print str(ldrvalue)
#            time.sleep(2)
#
#    def run(self):
#        self.mythread1(stop_threads)

def mythread1(self, stop):
    while 1:
        #if stop():
        #    print("Exiting thread")
        #    break
        ldrvalue = CheckLDR("192.168.0.111")
        f = open('LDRValueFile.txt', 'w')
        f.write(str(ldrvalue))
        f.close()
        f2 = open('LDRValueLogger.txt', 'a')
        date1 = datetime.datetime.now()
        f2.write("\n" + str(date1.hour) + ":" + str(date1.minute) + " " + str(date1.day) + "/" + str(date1.month) + "/" + str(date1.year) + "," + str(ldrvalue))
        f2.close()
        print str(ldrvalue)
        time.sleep(60)
    print "Stopping in thread!"



app = Flask(__name__)
#thread1 = myThread1()
#thread1 = threading.Thread(target=mythread1, args=(id, pill2kill))
thread1 = Process(target=mythread1, args=(id, pill2kill))
workers.append(thread1)

#MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'josh'
app.config['MYSQL_DATABASE_PASSWORD'] = 'josh'
app.config['MYSQL_DATABASE_DB'] = 'SmartHomeDevices'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)


@app.route('/')
def profile():
    return render_template("Home.html")

@app.route("/shopping")
def shopping():
    food = ["Cheese", "Tuna", "Beef"]
    return render_template("shopping.html", food=food)

@app.route('/home')
def home():
    return render_template("Home.html")

@app.route('/Homeactivate')
def Homeactivate():
    ipAddresses = CheckIP()
    return render_template("Homesetup.html")
    #return render_template("Homesetup.html", ipAddresses=ipAddresses)

@app.route('/Homesetup', methods=['POST', 'GET'])
def Homesetup():
    # read values for UI boxes
    _name = request.form['deviceName']
    _type = request.form['deviceType']
    _typeDD = request.form['deviceTypeDD']
    _ip = request.form['deviceIp']
    _ipDD = request.form['deviceIpDD']
  
    conn = mysql.connect()
    cur = conn.cursor()
    inDatabase = cur.execute("""SELECT device_name FROM devices WHERE device_name=%s""", (_name))
    if (inDatabase == 1):
      addDB = "Device cannot be added"
      addedToDB = 0
    else:
      addDB = "Device can be added"
      cur.execute("""insert into devices (device_name,device_type,device_ip) values(%s,%s,%s)""", (_name,_typeDD,_ipDD))
      addedToDB = 1
      
    conn.commit()

    return json.dumps(addDB)
    #if (addedToDB == 1):
    #  return redirect(url_for('light', lighton=0))
    #else:
    #  return json.dumps(addDB)

    

@app.route('/light/<lighton>')
def light(lighton): 
    return render_template("LightBulb.html", lighton=lighton)

@app.route('/LDRValue')
def LDRValue():
    #conn = mysql.connect()
    #cur = conn.cursor()
    #LDRvalueNum = cur.execute("""SELECT value FROM ldrvalues WHERE id=1""")
    #conn.commit()
    #LDRvalue = str(LDRValueNum)

    f = open('LDRValueFile.txt', 'r')
    ldrvalue = f.read()
    f.close() 

    return render_template("LDRDisplay.html", LDRvalue=str(ldrvalue))

@app.route('/buttonOn/', methods=['POST'])
def buttonOn():
    LightOn()
    return redirect(url_for('light', lighton=1))
    #return render_template("LightBulb.html")

@app.route('/buttonOff/', methods=['POST'])
def buttonOff():
    LightOff()
    return redirect(url_for('light', lighton=0))
    #return render_template("LightBulb.html")

@app.route('/light')
def light2(): 
    return redirect(url_for('light', lighton=0))


@app.route('/shutdown')
def shutdown():
    for worker in workers:
        worker.terminate()
    return render_template("LDRDisplay.html", LDRvalue="LDR Shut Down")




if __name__ == '__main__':
    thread1.start()
    app.run(host='0.0.0.0', port=9000, debug=False)

