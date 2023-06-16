import cv2
import matplotlib.pyplot as plt
import random
import numpy as np

vid = cv2.VideoCapture(0)

_rand = False

def plot(frame, _rand):
    x, y = np.meshgrid(np.linspace(-5, 5, 960), np.linspace(-5, 5, 960))
    if _rand:
        frame*=random.randint(1,10)
    fig, ax = plt.subplots(1,1)
    qr = ax.quiver(x,y,frame)
    plt.savefig('picplot.png')
    plt.close()


while (True):
    ret, frame = vid.read()
    x, y = np.meshgrid(np.linspace(-5, 5, 960), np.linspace(-5, 5, 960))
    cv2.imshow('To Ty!', frame)
    if cv2.waitKey(1) & 0xFF == ord('r'):
        _rand = not _rand
    if cv2.waitKey(1) & 0xFF == ord('p'):
        plot(frame, _rand)
        image= cv2.imread('picplot.png')
        cv2.imshow('Jestes wektorem!', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
