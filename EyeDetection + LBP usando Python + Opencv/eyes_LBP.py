import numpy as np
import cv2
from matplotlib import pyplot as plt

def thresholded(center, pixels):
    out = []
    for a in pixels:
        if a >= center:
            out.append(1)
        else:
            out.append(0)
    return out

def get_pixel_else_0(l, idx, idy, default=0):
    try:
        return l[idx,idy]
    except IndexError:
        return default

def computeLBP(img):
    LBPimg = img.copy()
    for x in range(0, len(img)):
        for y in range(0, len(img[0])):
            center        = img[x,y]
            top_left      = get_pixel_else_0(img, x-1, y-1)
            top_up        = get_pixel_else_0(img, x, y-1)
            top_right     = get_pixel_else_0(img, x+1, y-1)
            right         = get_pixel_else_0(img, x+1, y )
            left          = get_pixel_else_0(img, x-1, y )
            bottom_left   = get_pixel_else_0(img, x-1, y+1)
            bottom_right  = get_pixel_else_0(img, x+1, y+1)
            bottom_down   = get_pixel_else_0(img, x,   y+1 )
            values = thresholded(center, [top_left, top_up, top_right, right, bottom_right,
                                          bottom_down, bottom_left, left])
            weights = [1, 2, 4, 8, 16, 32, 64, 128]
            res = 0
            for a in range(0, len(values)):
                res += weights[a] * values[a]
            LBPimg.itemset((x,y), res)
        print (x)
    hist,bins = np.histogram(LBPimg.flatten(),256,[0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max()/ cdf.max()
    plt.plot(cdf_normalized, color = 'b')
    plt.hist(LBPimg.flatten(),256,[0,256], color = 'r')
    plt.xlim([0,256])
    plt.legend(('cdf','histogram'), loc = 'upper left')
    plt.show()
    return LBPimg
    

# Carrega o detector de olhos
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# Carrega a imagem a ser processada 
img = cv2.imread('teste.jpg')
# Converte para tons de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Redimensiona se for o caso
height, width = img.shape[:2]
gray = cv2.resize(gray,(int (0.2*width), int (0.2*height)))

# Detecta os olhos
eyes = eye_cascade.detectMultiScale(gray)
for (ex,ey,ew,eh) in eyes:
    crop_img = gray[ey:ey+eh, ex:ex+ew].copy() 
    LBP_img = computeLBP(crop_img)
    cv2.imshow('LBP',LBP_img)
    cv2.rectangle(gray,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.imshow('gray',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
