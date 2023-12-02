import RPi.GPIO as GPIO 

class GpioDoorManager:
    def __init__(self, pin_num = 21):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin_num, GPIO.IN)
        self.door_pin = pin_num
        self.pre_status = 1
        self.now_status = 0
        
    def read(self):
        self.pre_status = self.now_status
        self.now_status = GPIO.input(self.door_pin)
        
    def check(self):
        return self.pre_status == self.now_status
    
    def get_now_status(self):
        return self.now_status
        
    