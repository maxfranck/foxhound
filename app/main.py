import cv2
import numpy as np

# Load source image
camera = cv2.VideoCapture(0)

while True:
    conectado, src = camera.read()

    # Remove noise by blurring with a Gaussian filter
    src  = cv2.GaussianBlur(src,(3,3),0)
    # Convert the image to grayscale
    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # Apply Laplace function
    edges = cv2.Laplacian(src_gray, -1, ksize=5, scale=1,delta=0,borderType=cv2.BORDER_DEFAULT)
    # Converting back to uint8
    resultado = cv2.convertScaleAbs(edges)
    # Display the result
    cv2.imshow('Video', resultado)

    if cv2.waitKey(1) == 27: # Esc
        break

camera.release()
cv2.destroyAllWindows()