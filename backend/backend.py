#!/usr/bin/env python3

import json
import os
import io
import base64
import argparse

from flask import Flask
from flask import request, abort
from PIL import Image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/images")
def list_images():
    imagelist= [file for file in os.listdir(PATH) if file.endswith(FILE_ENDING)]
    return json.dumps(imagelist)

@app.route("/dimensions/<image>")
def get_dimensions(image):
    try:
        theimage =  Image.open( os.path.join(PATH, image))
        dimx, dimy = theimage.size
        return json.dumps({'width':dimx, 'height':dimy})
    except Exception as e:
        print(e)
        return abort(404)

@app.route("/<image>")
def get_image(image):
    try:
        with open(os.path.join(PATH, image), 'rb') as f:
            theimage = Image.open(f)
            theimage = theimage.crop( tuple([int(request.args.get(i, '')) for i in ['left', 'top', 'right', 'bottom']]) )
            imgByteArr = io.BytesIO()
            theimage.save(imgByteArr, format='PNG')
            theimage = base64.b64encode( imgByteArr.getvalue() )
            return theimage
    except Exception as e:
        app.logger.error(e, exc_info=True)
        return abort(404)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', action='store', dest='port',
                    help='Port number to bind to', type=int, default=5000)
    parser.add_argument('-d', action='store', dest='path',
                    help='Path to images', default='images/')
    parser.add_argument('-a', action='store', dest='addr', help='Address to bind to', default='0.0.0.0')
    parser.add_argument('-e', action='store', dest='fileending', help='File ending', default='.png')

    args = parser.parse_args()

    PATH = args.path
    FILE_ENDING = args.fileending

    print(" - Image location: {}, File ending: {}".format(args.path, args.fileending))

    app.run(args.addr, port=args.port)
