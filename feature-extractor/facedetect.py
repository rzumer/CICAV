# coding=utf-8
'''
Created on Jun 19, 2017

@author: Raphaël Zumer
'''

import os
import cv2
import numpy as np
import peakutils
from numpy.f2py.auxfuncs import throw_error

def getFaceCount(path):
    if not os.path.exists(path):
        print(path, "does not exist")
        return None
    
    cascadefile = "haarcascade_frontalface_alt2.xml"
    
    if not os.path.exists(cascadefile):
        throw_error(cascadefile, "does not exist")
        
    cascade = cv2.CascadeClassifier(cascadefile)
    
    print "Handling", os.path.basename(path)
    
    vidcap = cv2.VideoCapture(path)
    faces = []
    
    success, image = vidcap.read()
    
    while success:
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        facesfound = cascade.detectMultiScale(
            grey,
            scaleFactor = 1.1, 
            minNeighbors = 3, 
            minSize = (8, 8), 
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        
        faces.append(len(facesfound))
        
        skipFrames(vidcap, 4)
        success, image = vidcap.read()
        
    meanfaces = np.mean(faces)
    print(meanfaces, "mean faces")
    
    return meanfaces

def skipFrames(vidcap, num):
    for _ in range(num):
        vidcap.read()
