# coding=utf-8
'''
Created on Jun 19, 2017

@author: Raphaël Zumer
'''

import os
import cv2
from numpy import mean

def getGlobalGradientMagnitude(path):
    if not os.path.exists(path):
        print(path, "does not exist")
        return None
    
    print "Handling", os.path.basename(path)
    
    depth = cv2.CV_32F
    
    vidcap = cv2.VideoCapture(path)
    magnitudes = []
    dxmags = []
    dymags = []
    ignoredmags = 0
    success, image = vidcap.read()
    lastframe = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lastblurred = lastframe
    lastmag = 0
    lastdx = 0
    lastdy = 0
    
    if not success:
        return 0
    
    success, image = vidcap.read()
    
    while success:
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        blurred = cv2.medianBlur(grey, 3)
        blurred = cv2.blur(blurred, (5,5))
        
        dfd = cv2.absdiff(grey, lastframe)
        dfdblurred = cv2.absdiff(blurred, lastblurred)
        dx = cv2.Sobel(dfd, depth, 1, 0)
        dxblurred = cv2.Sobel(dfdblurred, depth, 1, 0)
        dy = cv2.Sobel(dfd, depth, 0, 1)
        dyblurred = cv2.Sobel(dfdblurred, depth, 0, 1)
        dxabs = cv2.convertScaleAbs(dx)
        dxblurredabs = cv2.convertScaleAbs(dxblurred)
        dyabs = cv2.convertScaleAbs(dy)
        dyblurredabs = cv2.convertScaleAbs(dyblurred)
        mag = mean(cv2.addWeighted(dxabs, 0.5, dyabs, 0.5, 0))
        blurredmag = mean(cv2.addWeighted(dxblurredabs, 0.5, dyblurredabs, 0.5, 0))
        dxmag = mean(dxabs)
        dymag = mean(dyabs)
        
        graddiff = abs(lastmag - mag)
        dxdiff = abs(lastdx - dxmag)
        dydiff = abs(lastdy - dymag)
        
        if blurredmag < 0.6:
            ignoredmags += 1
        #else:
        magnitudes.append(graddiff)
        dxmags.append(dxdiff)
        dymags.append(dydiff)
        
        lastmag = mag
        lastframe = grey
        lastblurred = blurred
        lastdx = dxmag
        lastdy = dymag
        success, image = vidcap.read()
        
    meanmagnitude = mean(magnitudes)
    meandx = mean(dxmags)
    meandy = mean(dymags)
    print(meanmagnitude, "mean graddiff")
    print(ignoredmags, "ignored")
    
    return meanmagnitude, meandx, meandy, ignoredmags
