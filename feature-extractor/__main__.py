# coding=utf-8
'''
Created on Jun 19, 2017

@author: Raphaël Zumer
'''

import sys, os
import unicodecsv as csv
import scenecounter, gradient, color, facedetect
import arff
import itertools

def main():
    if len(sys.argv) < 2:
        print("Usage: FeatureExtractor <basepath>")
        return None
    else:
        # Set the base path, where pre-processed input should be classified into subdirectories for labeling
        basepath = sys.argv[1]
        if not os.path.isdir(basepath):
            print("Invalid path provided")
            return None
        
        csvpath = os.path.join(os.path.dirname(basepath), "features.csv")
        arffpath = os.path.join(os.path.dirname(basepath), "features.arff")
        if os.path.exists(csvpath):
            os.remove(csvpath)
        if os.path.exists(arffpath):
            os.remove(arffpath)
        
        arffobj = {
            'description': '',
            'relation': 'animationtype',
            'attributes': [
                ('mean transitions/s', 'REAL'),
                ('frame rate', 'REAL'),
                ('mean gradient mag', 'REAL'),
                ('mean gradient x', 'REAL'),
                ('mean gradient y', 'REAL'),
                ('immobile frames', 'REAL'),
                ('hist peaks', 'REAL'),
                ('16bin peaks', 'REAL'),
                ('8bin peaks', 'REAL'),
                ('histogram variance', 'REAL'),
                ('16bin variance', 'REAL'),
                ('8bin variance', 'REAL'),
                ('texture hist peaks', 'REAL'),
                ('max texture hist index', 'REAL'),
                ('texture hist variance', 'REAL'),
                ('mean hist diff', 'REAL'),
                ('16bin mean diff', 'REAL'),
                ('8bin mean diff', 'REAL'),
                ('mean face count', 'REAL'),
                ('animation type', next(os.walk(basepath))[1])
            ],
            'data': [],
        }
        
        with open(csvpath, 'wt') as csvfile:
            csvwriter = csv.writer(csvfile, encoding='utf-8')
            csvwriter.writerow( ('Filename', 'Mean transitions/second', 'Frame rate', 'Mean movement gradient magnitude', 'Mean movement gradient dx', 'Mean movement gradient dy', 'Immobile frames', 'Color peaks', '16bin peaks', '8bin peaks', 'Color bias', '16bin bias', '8bin bias', 'Local binary pattern peaks', 'Max local binary pattern', 'Local binary pattern bias', 'Mean histogram difference', '16bin diff', '8bin diff', 'Face count', 'Class') )
            
            #for filename in itertools.islice(absoluteFilePaths(basepath), 5):
            for filename in absoluteFilePaths(basepath):
                unicodefilename = filename.decode('shift-jis', 'ignore')
                
                outclass = os.path.basename(os.path.dirname(unicodefilename))
                outfile = os.path.basename(unicodefilename)
                meancuts, framerate = 0,0
                gradientmagnitude, dxmag, dymag = 0,0,0
                colorpeaks, peaks16, peaks8, lbppeaks, lbpmax, histdiff, diff16, diff8, bias, bias16, bias8, lbpbias = 0,0,0,0,0,0,0,0,0,0,0,0
                facecount = 0
                meancuts, framerate = scenecounter.countCuts(filename)
                gradientmagnitude, dxmag, dymag, immobileframes = gradient.getGlobalGradientMagnitude(filename)
                colorpeaks, peaks16, peaks8, lbppeaks, lbpmax, histdiff, diff16, diff8, bias, bias16, bias8, lbpbias = color.getHistogramPeaks(filename)
                facecount = facedetect.getFaceCount(filename)
                csvwriter.writerow( (outfile, meancuts, framerate, gradientmagnitude, dxmag, dymag, immobileframes, colorpeaks, peaks16, peaks8, bias, bias16, bias8, lbppeaks, lbpmax, lbpbias, histdiff, diff16, diff8, facecount, outclass) )
                
                arffobj['data'].append([meancuts, framerate, gradientmagnitude, dxmag, dymag, immobileframes, colorpeaks, peaks16, peaks8, bias, bias16, bias8, lbppeaks, lbpmax, lbpbias, histdiff, diff16, diff8, facecount, outclass])
                
        with open(arffpath, 'wt') as arfffile:
            arfffile.write(arff.dumps(arffobj))
            
def absoluteFilePaths(directory):
    for dirpath,_,filenames in os.walk(directory):
        for f in filenames:
            yield os.path.abspath(os.path.join(dirpath, f))

if __name__ == '__main__':
    main()
