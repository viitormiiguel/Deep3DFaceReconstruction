
import dlib
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

from imutils import face_utils
from PIL import Image

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('model/shape_predictor_68_face_landmarks.dat')

## Reshape image grayscale to RBG. Add new dimension
def reshapeImg(imagesp):

    pasta = os.listdir(imagesp)
    
    for p in pasta:
    
        stpath = p.split('.')
        if 'jpg' in stpath[1] and 'SN' not in stpath[0]:            
            
            print(imagesp + p)
                    
            image = cv2.imread(imagesp + p)
            img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            cv2.imwrite(imagesp + p, img)

            img = cv2.imread(imagesp + p, 0)
            img = np.array(img, dtype=np.uint8)

            imgr = np.dstack((img, np.zeros_like(img), np.zeros_like(img)))
            imgp = Image.fromarray(imgr, 'RGB')
            imgp.save(imagesp + p)
            
        if 'png' in stpath[1] and 'SN' not in stpath[0]:   
            
            print(imagesp + p)
                    
            image = cv2.imread(imagesp + p)
            img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            cv2.imwrite(imagesp + p, img)

            img = cv2.imread(imagesp + p, 0)
            img = np.array(img, dtype=np.uint8)

            imgr = np.dstack((img, np.zeros_like(img), np.zeros_like(img)))
            imgp = Image.fromarray(imgr, 'RGB')
            imgp.save(imagesp + p)
            

def createTxt(imagesp):
    
    subpastas = os.listdir(imagesp)
    
    for p in subpastas:

        pimg = imagesp + p
        
        print(pimg)

        img = cv2.imread(pimg)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        
        if len(rects) > 0:
    
            for rect in rects:

                x = rect.left()
                y = rect.top()
                w = rect.right()
                h = rect.bottom()

            shape = predictor(gray, rect)
            shape_np = face_utils.shape_to_np(shape).tolist()
            left_eye = midpoint(shape_np[36], shape_np[39])
            right_eye = midpoint(shape_np[42], shape_np[45])
            features = [left_eye, right_eye, shape_np[33], shape_np[48], shape_np[54]]   

            with open(pimg.split('.')[0] + ".txt", "a") as f:
                for i in features:
                    print(str(i[0]) + ' ' + str(i[1]), file=f)   

def midpoint(p1, p2):
    
    coords = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
	
    return [int(x) for x in coords]

if __name__ == '__main__':
    
    path = 'input/Real/Will/anger/'
    
    # reshapeImg(path)
    
    createTxt(path)
    # print('## Coordinates Files created!')