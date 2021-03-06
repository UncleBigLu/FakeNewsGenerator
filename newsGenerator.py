#!/usr/bin/python

import json
import sys
import os
import random
import readArgv
import latex


def main(argv):
    # Get and parse command line argvs
    argvDict = readArgv.read_argv(argv)
    dirpath = os.path.dirname(os.path.abspath(__file__)) + '/Data'
    # Open json data file
    with open(os.path.join(dirpath, argvDict['type'], 'data.json')) as f:
        data = json.load(f)
        # Randomly load one passage
        passage = [data['intro'][random.randint(0, len(data['intro']) - 1)], data['body'][random.randint(0, len(data['body']) - 1)], data['end'][random.randint(0, len(data['end']) - 1)]]
        # Replace args
    context = []
    for seg in passage:
        seg = seg.replace("#DATE#", argvDict['time'])
        while True:
            oldSeg = seg
            seg = seg.replace('#NAME#', argvDict['members'][random.randint(0, len(argvDict['members'])-1)], 1)
            if oldSeg == seg:
                break
        seg = seg.replace("#TOPIC#", argvDict['topic'])
        seg = seg.replace("#POSITION#", argvDict['position'])

        context.append(seg)
    latex.convertPDF(argvDict, context)


if __name__ == "__main__":
    main(sys.argv[1:])
