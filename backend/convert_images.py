#!/usr/bin/env python3

import os
import argparse

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store', dest='path', help='Path to images', default='images/')
parser.add_argument('-e', action='store', dest='fileending', help='File ending', default='.png')
parser.add_argument('-w', action='store', dest='basewidth', help='Desired with', type=int, default=800)

args = parser.parse_args()

PATH = args.path
FILE_ENDING = args.fileending
BASEWIDTH = args.basewidth

print(" - Image location: {}, File ending: {}".format(args.path, args.fileending))

for imagepath in [os.path.join(PATH,file) for file in os.listdir(PATH)]:
    try:
        theimage = Image.open( imagepath)
        if theimage.size[0] != BASEWIDTH:
            wpercent = (BASEWIDTH/float(theimage.size[0]))
            hsize = int((float(theimage.size[1])*float(wpercent)))
            print('{}:{}x{} -> {}:{}x{}'.format(imagepath, theimage.size[0], theimage.size[1], imagepath.replace('.jpg', FILE_ENDING), BASEWIDTH,hsize))
            theimage = theimage.resize((BASEWIDTH,hsize), Image.ANTIALIAS)
            theimage.save(imagepath.replace('.jpg',FILE_ENDING))
            if '.jpg' in imagepath:
                os.remove(imagepath)
                print('Removed file: {}'.format(imagepath))
    except Exception as e:
        print(e)
