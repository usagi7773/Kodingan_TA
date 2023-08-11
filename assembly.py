#!/usr/bin/env python3

#Serial dependency library
import serial
#Camera dependencies library
# import RPi.GPIO as gp
import os
#Request library for POST data
import requests
import datetime
#Library for firebase
import pyrebase
from PIL import Image
from io import BytesIO

#Camera configuration
# gp.setwarnings(False)
# gp.setmode(gp.BOARD)
# 
# gp.setup(7, gp.OUT)
# gp.setup(11, gp.OUT)
# gp.setup(12, gp.OUT)

# Configure Firebase
config = {
    "apiKey": "AIzaSyBFZ02S9AYuX2Prj2--unJe5uccgbGVfD8",
    "authDomain": "smart-toilet-6fc80.firebaseapp.com",
    "databaseURL": "https://smart-toilet-6fc80-default-rtdb.firebaseio.com/",
    "projectId": "smart-toilet-6fc80",
    "storageBucket": "smart-toilet-6fc80.appspot.com",
    "messagingSenderId": "1049544057344",
    "appId": "1:1049544057344:web:b9aa18caaa4400b7fcaee5",
    "measurementId": "G-VMM9GY7PH1",
    "serviceAccount": "serviceAccount.json"
}
# "https://smart-toilet-6fc80-default-rtdb.asia-southeast1.firebasedatabase.app",
firebase = pyrebase.initialize_app(config)
current_time = datetime.datetime.now()

storage = firebase.storage()

auth = firebase.auth()

#POST data to server using request libary
def uploadData(url):
#     current_time = datetime.datetime.now()
#     files = { 
#             "feses" : open("capture_1.jpg", "rb"),
#             "urin"	: open("capture_3.jpg", "rb"),	
#             "time" : current_time
#             }
#     r = requests.post(url, files=files)
    if url == "1":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "2":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "3":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "4":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "5":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "6":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "7":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "8":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "9":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    elif url == "10":
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    else :
        user = auth.sign_in_with_email_and_password("luthfinsz@gmail.com", "1234567890")
    
    uid = user['localId']
    print (uid)
#     storage.child("images/%s/feces/capture_1.jpg" % uid ).put("capture_1.jpg")
    storage.child("images/%s/feces/1_test.jpg" % uid ).put("1_test.jpg")
    
#Function for capture image
def capture(cam):
#     current_time = datetime.datetime.now()
#     cmd = "libcamera-still -o capture_%d.jpg --qt-preview" % cam
    cmd = "libcamera-still -o 1_test.jpg --qt-preview" #use -n to close the preview window
    os.system(cmd)
    
    
#i2c set up for adapter multicamera
def i2cSetCamera():
    print('Start testing the camera A')
    i2c = "i2cset -y 1 0x70 0x00 0x04"
    os.system(i2c)
#     gp.output(7, False)
#     gp.output(11, False)
#     gp.output(12, True)
    capture("urine")
#     print('Start testing the camera B') 
#     i2c = "i2cset -y 1 0x70 0x00 0x05"
#     os.system(i2c)
#     gp.output(7, True)
#     gp.output(11, False)
#     gp.output(12, True)
#     capture(2)
#    print('Start testing the camera C')
#    i2c = "i2cset -y 1 0x70 0x00 0x06"
#    os.system(i2c)
#    gp.output(7, False)
#    gp.output(11, True)
#    gp.output(12, False)
#    capture("urine")
#     print('Start testing the camera D')
#     i2c = "i2cset -y 1 0x70 0x00 0x07"
#     os.system(i2c)
#     gp.output(7, True)
#     gp.output(11, True)
#     gp.output(12, False)
#     capture(4)

if __name__ == '__main__':
    #Serial communication init
    ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=1)
#     ser.write(b'qwertyui')
    ser.reset_input_buffer()

    while True:
        if ser.in_waiting > 0:
            idUser = ser.readline().decode('utf-8').rstrip()
            try: 
                if (int(idUser) >= 1 or int(idUser) <= 10):
                    print(idUser)
                    #Camera init action
                    i2cSetCamera()
                    #Send state to open the servo
                    ser.write(b"off\n")
                    uploadData(idUser)
                    ser.write(b"uploaded\n")
                    ser.flush()
    #                 url = "default"
            except Exception:
                pass

