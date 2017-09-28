#! /usr/bin/env python
__author__ = 'zieghailo'

import os
import cv2
import numpy as np
from datetime import datetime
import classify

import os
import glob

files = glob.glob('./images/*')
for f in files:
    os.remove(f)
print("Extracting frames from the video.....")
print("Please Wait...\n\n")
def video2frames(path, output=None, skip=1, mirror=False):
    video_object = cv2.VideoCapture(path)

    # setup the output folder
    if output is None:
        output = path[:-4]
    else:
        if not output.endswith('/') and not output.endswith('\\'):
            output += '/'
        output += 'py_image'

    index = 0
    last_mirrored = True
    while True:
        success, frame = video_object.read()
        if success:
            if index % skip == 0:
                if mirror and last_mirrored:
                    frame = _mirror_image(frame)
                last_mirrored = not last_mirrored

                cv2.imwrite(output + "_" + str(datetime.now()) + ".jpg", frame)  # assumes that the extension is three letters long
        else:
            break

        index += 1


def _mirror_image(image):
    return np.fliplr(image)


def main():
    import argparse
    parser = argparse.ArgumentParser("Enter the filename of a video")
    parser.add_argument('filename')
    parser.add_argument('-o', '--output')
    parser.add_argument('--skip', help="Only save every nth frame")
    parser.add_argument('--mirror', action='store_true', help="Flip every other image")
    args = parser.parse_args()

    if args.skip is None:
        args.skip = 1
    if args.mirror is None:
        args.mirror = False

    # In case the filename points to a directory
    if os.path.isdir(args.filename):
        files = [os.path.join(args.filename, f) for f in os.listdir(args.filename) if os.path.isfile(os.path.join(args.filename, f))]
        for video in files:
            video2frames(video, output=args.output, skip=int(args.skip), mirror=bool(args.mirror))

    else:
        video2frames(args.filename, output=args.output, skip=int(args.skip), mirror=bool(args.mirror))


if __name__ == "__main__":
    main()
    print("100% Extracted")
    print("Begin Analysis.....")
    print("Please Wait....\n\n")
    classify.run_classifier()

