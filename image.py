# First we must get the image from the camera
# Create a camera class that will handle the getting of the image
from time import time

class Camera(object):
    def __init__(self):
        self.frames = [open(f + '.jpg', 'rb').read() for f in['1','2','3']]

    def get_frame(self):
        return self.frames[int(time()) % 3]
import cv2
cam_ip = '192.168.1.225'
cap = cv2.VideoCapture('rtsp://'+cam_ip':8554/CH001.sdp')

while True:
    _, frame = cap.read()
    cv2.imshow(('Camera', frame))

    k = cv2.waitKey(0) & 0xFF
    if k == 27: #esc key ends process
        cap.release()
        break
cv2.destroyAllWindows()




# Using OpenCV to apply the fft to the image.

# This copied from https://opencv-python-tutroals.readthedocs.io/en/latest/py_tu
#torials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
