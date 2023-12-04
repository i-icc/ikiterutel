from firestore_sender import FireStoreSender
import time
from gpio_door_manager import GpioDoorManager

fss = FireStoreSender()
gdm = GpioDoorManager()

def main():
    start()
    while True:
        time.sleep(1)
        loop()
    
    
def start():
    print("start")
    gdm.read()
    gdm.read()

def loop():
    gdm.read()
    print(gdm.get_now_status())
    if gdm.check():
        is_open = gdm.get_now_status()
        # fss.send2ikiterutel(1, is_open)
        print(is_open)

if __name__ == "__main__":
    main()