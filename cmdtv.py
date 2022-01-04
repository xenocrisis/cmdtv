import sys
from types import FrameType
from PIL import Image
import cv2
from time import sleep
import os
import base64
from art import *

# Path del video
print('[!]Debes meter el video en formato mp4 a poder ser en la misma carpeta que el script.')
vidcap = cv2.VideoCapture(input('[?]Nombre del archivo: '))
success, image = vidcap.read()

count = 0
animation = "|/-\\"
idx = 0

try:
  while success:
    cv2.imwrite("frames/frame%d.jpg" % count, image)    
    success,image = vidcap.read()
    print('[+]Procesando video, frame ', count)
    print(animation[idx % len(animation)], end="\r")
    idx += 1
    count += 1

  # intro
  print('[+]Listo para reproducir!')
  print(text2art('xenonxss'))
  sleep(2)

  n = 0

  input('[?]Delay entre frames (Recomiendo entre 1 y 0.01): ')
  
  while n < count:
    # delay per frame
    sleep(0.01)
    image_path = 'frames/frame' + str(n) + '.jpg'
    image = Image.open(image_path)

    # tamaño
    width, height = image.size
    aspect_ratio = height/width
    new_width = 120
    new_height = aspect_ratio * new_width * 0.5
    img = image.resize((new_width, int(new_height)))

    # escala de grises
    img = img.convert('L')
    pixels = img.getdata()

    # chars para sustituir
    chars = ["·", ",", "-", "=", "O", "%", "&", "/", "Q", "B", "$", "#"]
    new_pixels = [chars[pixel//25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)
    new_pixels_count = len(new_pixels)
    ascii_image = [new_pixels[index:index + new_width] for index in range(0, new_pixels_count, new_width)]
    ascii_image = "\n".join(ascii_image)
    print(ascii_image)

    with open("ascii_image.txt", "w") as f:
      f.write(ascii_image)
      
    os.system('del ' + 'frames\\frame' + str(n) + '.jpg')
    n = n + 1
except:
  print('[-]Algo no esperado ocurrió :(')
    