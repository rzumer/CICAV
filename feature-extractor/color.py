# coding=utf-8
'''
Created on Jun 19, 2017

@author: Raphaël Zumer
'''

import os
import cv2
import numpy as np
import peakutils
from skimage.feature.texture import local_binary_pattern
from scipy.stats import itemfreq
from sklearn.preprocessing import normalize
import heapq
import random

def getHistogramPeaks(path):
    if not os.path.exists(path):
        print(path, "does not exist")
        return None
    
    print "Handling", os.path.basename(path)
    
    vidcap = cv2.VideoCapture(path)
    framenum = 0
    peaks = 0
    peaks16 = 0
    peaks8 = 0
    lbppeaks = 0
    peakfreq = [0 for _ in range(34)]
    peakfreq16 = [0 for _ in range(18)]
    peakfreq8 = [0 for _ in range(10)]
    lbppeakfreq = [0 for _ in range(28)]
    lasthist = [0 for _ in range(32)]
    lasthist16 = [0 for _ in range(16)]
    lasthist8 = [0 for _ in range(8)]
    histdiffs = []
    histdiffs16 = []
    histdiffs8 = []
    
    success, image = vidcap.read()
    
    while success:
        grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.medianBlur(grey, 3)
        
        histogram = cv2.calcHist([blurred], [0], None, [32], [0, 256])
        cv2.normalize(histogram, histogram)
        hist16 = cv2.calcHist([blurred], [0], None, [16], [0, 256])
        cv2.normalize(hist16, hist16)
        hist8 = cv2.calcHist([blurred], [0], None, [8], [0, 256])
        cv2.normalize(hist8, hist8)
        histarray = np.asarray(histogram).ravel()
        hist16 = np.asarray(hist16).ravel()
        hist8 = np.asarray(hist8).ravel()
        
        if framenum % 5 == 0:
            radius = 3
            no_points = 8 * radius
            
            lbp = local_binary_pattern(grey, no_points, radius, method='uniform')
            cv2.normalize(lbp, lbp)
            lbpfreq = itemfreq(lbp.ravel())
            lbphist = lbpfreq[:, 1]/sum(lbpfreq[:, 1])
            lbphist = np.asarray(lbphist).ravel()
            lbphist = np.insert(lbphist, 0, 0)
            lbphist = np.append(lbphist, 0)
            currentlbppeaks = peakutils.indexes(lbphist, 0.3 * (28 / float(26)), 1) # change dist back to 2 if it worsens
            for val in currentlbppeaks:
                lbppeakfreq[val] += 1
                lbppeaks += len(currentlbppeaks)
        
        minbins = [0 for _ in range(32)]
        for idx, hbin in enumerate(histarray):
            minbins[idx] = min(hbin, lasthist[idx])
            
        minbins16 = [0 for _ in range(16)]
        for idx, hbin in enumerate(hist16):
            minbins16[idx] = min(hbin, lasthist16[idx])
            
        minbins8 = [0 for _ in range(8)]
        for idx, hbin in enumerate(hist8):
            minbins8[idx] = min(hbin, lasthist8[idx])
            
        histarray = np.insert(histarray, 0, 0)
        histarray = np.append(histarray, 0)
        hist16 = np.insert(hist16, 0, 0)
        hist16 = np.append(hist16, 0)
        hist8 = np.insert(hist8, 0, 0)
        hist8 = np.append(hist8, 0)
        
        currentpeaks = peakutils.indexes(histarray, 0.3 * (34 / float(32)), 1)
        curpeaks16 = peakutils.indexes(hist16, 0.3 * (18 / float(16)), 1)
        curpeaks8 = peakutils.indexes(hist8, 0.3 * (10 / float(8)), 1)
        
        for val in currentpeaks:
            peakfreq[val] += 1
            
        for val in curpeaks16:
            peakfreq16[val] += 1
            
        for val in curpeaks8:
            peakfreq8[val] += 1
            
        histdiffs.append(1 - (sum(minbins) / float(sum(histarray))))
        histdiffs16.append(1 - (sum(minbins16) / float(sum(hist16))))
        histdiffs8.append(1 - (sum(minbins8) / float(sum(hist8))))
        
        peaks += len(currentpeaks)
        peaks16 += len(curpeaks16)
        peaks8 += len(curpeaks8)
        
        lasthist = histarray
        lasthist16 = hist16
        lasthist8 = hist8
        framenum += 1
        
        success, image = vidcap.read()
    
    bias = 0
    bias16 = 0
    bias8 = 0
    lbpbias = 0
    if sum(peakfreq) != 0:
        #bias = (sum(heapq.nlargest(2, peakfreq)) / float(sum(peakfreq)))
        bias = np.var(peakfreq)
        bias16 = np.var(peakfreq16)
        bias8 = np.var(peakfreq8)
    if sum(lbppeakfreq) != 0:
        #lbpbias = max(lbppeakfreq) / float(sum(lbppeakfreq))
        lbpbias = np.var(lbppeakfreq)
        
    meandiff = np.mean(histdiffs)
    meandiff16 = np.mean(histdiffs16)
    meandiff8 = np.mean(histdiffs8)
    lbpmax = np.argmax(lbppeakfreq)
    
    print(peaks, "histogram peaks (32 bins),", lbppeaks, "lbp peaks")
    print(meandiff, "mean diff")
    
    return peaks, peaks16, peaks8, lbppeaks, lbpmax, meandiff, meandiff16, meandiff8, bias, bias16, bias8, lbpbias
