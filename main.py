import time
import pyautogui
from PIL import Image, ImageGrab
# from numpy import asarray

def is_collide(data):   
    for i in range(250, 450):
        for j in range(405, 450):
            if data[i, j] > 150 or data[i, j] == 0:
                hit("up")
                return True
    return False

def hit(key):
    pyautogui.keyDown(key)


if __name__ == "__main__":
    time.sleep(1)
    print("Game starts in 2 seconds")
    hit("up")
    while True:
        image = ImageGrab.grab().convert("L")
        data = image.load()
        is_collide(data)

        # # For Cactus
        # for i in range(250, 350):
        #     for j in range(350, 450):
        #         data[i, j] = 0
    
        # # For Birds
        # for i in range(200,250):
        #     for j in range(280, 390):
        #         data[i, j] = 71
        # image.show()
        # break
