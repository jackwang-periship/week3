'''
Created on Jun 11, 2017

@author: student
'''
import os
from PIL import Image


def extractFrames(inGif, outFolder):
    frame = Image.open(inGif)
    nframes = 0
    while frame:
        frame.save( '%s/%s-%s.gif' % (outFolder, os.path.basename(inGif), nframes ) , 'GIF')
        nframes += 1
        try:
            frame.seek( nframes )
        except EOFError:
            break;
    return True
    

extractFrames('NatLoop.gif', 'output')
