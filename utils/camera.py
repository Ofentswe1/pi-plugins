import picamera
from time import time
from time import sleep

class Camera:
    def capture(self):
        picamera.PiCamera.capture('image-' + str(time.now()) + '.jpg')

    def status_on(self):
        pass

    def status_off(self):
        pass

