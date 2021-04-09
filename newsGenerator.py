#!/usr/bin/python

import json
import sys, getopt
import os
import random
import readArgv

def main(argv):
    # Get and parse command line argvs
    argvDict = readArgv.readArgv(argv)

    # Open json data file
    with open(os.path.join('./Data', argvDict['type'], 'data.json')) as f:
        data = json.load(f)
        # Randomly load one passage
        passage = [data['intro'][random.randint(0, len(data['intro']) - 1)], data['body'][random.randint(0, len(data['body']) - 1)], data['end'][random.randint(0, len(data['end']) - 1)]]
        # Replace args
        for seg in passage:
            seg = seg.replace("#DATE#", argvDict['time'])
            while True:
                oldSeg = seg
                seg = seg.replace('#NAME#', argvDict['members'][random.randint(0, len(argvDict['members'])-1)], 1)
                if oldSeg == seg:
                    break
            seg = seg.replace("#TOPIC#", argvDict['topic'])
            seg = seg.replace("#POSITION#", argvDict['position'])

            print(seg)

if __name__ == "__main__":
    main(sys.argv[1:])
