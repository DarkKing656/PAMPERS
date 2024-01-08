import serial
import time
import os

class Connection:
    def __init__(self):
        self.ser = serial.Serial('COM3', 9600)

    def control_device(self, mode):
        while True:
            os.system('cls||clear')  
            if mode == "on":
                self.ser.write(b'1')
            elif mode == "off":
                self.ser.write(b'0')
            elif mode == "servo":
                self.ser.write(b'2')
            else:
                break

try:
    connection = Connection()
    mode = input("\non\noff\nservo\n:")
    connection.control_device(mode)
except Exception as e:
    print("Ошибка:", e)
finally:
    connection.ser.close()
    os.system('cls||clear')
#пустой конструктор класса
class Connection:
    def __init__(self):
        self.ser = None

    def connect(self, port, baudrate):
        self.ser = serial.Serial(port, baudrate)
    
    def close(self):
        if self.ser:
            self.ser.close()


