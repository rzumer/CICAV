# coding=utf-8
'''
Created on Jun 19, 2017

@author: Raphaël Zumer
'''

import os
import scenedetect
from numpy import mean

def countCuts(path):
    if not os.path.exists(path):
        print(path, "does not exist")
        return None
    
    print "Handling", os.path.basename(path)
    
    scene_list = []
    detector_list = [
        scenedetect.detectors.ContentDetector(threshold = 4)
    ]
    
    video_framerate, frames_read = scenedetect.detect_scenes_file(path, scene_list, detector_list)
    
    numcuts = len(scene_list)
    
    print numcuts, "cuts:", scene_list
    
    #scene_list_msec = [(1000.0 * x) / float(video_framerate) for x in scene_list]
    #scene_length_msec = []

    #for scene in xrange(len(scene_list_msec)):
    #    if scene == 0:
    #        scene_length_msec.append(scene_list_msec[scene])
    #    else:
    #        scene_length_msec.append(scene_list_msec[scene] - scene_list_msec[scene - 1])
    
    cutspersecond = numcuts / (frames_read / float(video_framerate))
    
    print cutspersecond, "cuts/second"
    
    return cutspersecond, video_framerate
