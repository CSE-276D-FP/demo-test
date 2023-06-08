import PiCamera
from time import sleep

camera = PiCamera()

image_number = 0
while True:
    sleep(60) #images are taken every minute
    image_name = 'image{0:04d}.jpg'.format(image_number)
    camera.capture(image_name)
    image_number += 1
    
# run this code in the terminal: 
# fmpeg -r 10 -i image%04d.jpg -r 10 -vcodec libx264 -crf 20 -g 15 timelapse.mp4


