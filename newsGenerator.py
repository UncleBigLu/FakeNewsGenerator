#!/usr/bin/python

import json
import sys, getopt
import os
import random

def main(argv):
    type = ''
    topic = ''
    time = ''
    position = ''
    members = ''


    # Get and parse command line argvs
    try:
        opts, args = getopt.getopt(argv, "h", ["type=","topic=", "time=", "position=", "members="])
    except getopt.GetoptError:
        print('Usage: newsGenerator.py --topic <topic> --time <time> --position <position> --members <member1[，member2，member3]>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('Usage: newsGenerator.py --topic <topic> --time <time> --position <position> --members <member1[,member2,member3]>')
            sys.exit()
        elif opt == '--type':
            type = arg
        elif opt == '--topic':
            topic = arg
        elif opt == '--time':
            time = arg
        elif opt == '--position':
            position = arg
        elif opt == '--members':
            members = arg

    memberList = members.split('，')

    # Open json data file
    with open(os.path.join('./Data', type, 'data.json')) as f:
        data = json.load(f)
        passage = [data['intro'][0], data['body'][0], data['end'][0]]
        for seg in passage:
            seg = seg.replace("#DATE#", time)
            while True:
                oldSeg = seg
                seg = seg.replace('#NAME#', memberList[random.randint(0, len(memberList)-1)], 1)
                if oldSeg == seg:
                    break
            seg = seg.replace("#TOPIC#", topic)
            seg = seg.replace("#POSITION#", position)

            print(seg)



# # open json data file
# with open('./Data/项目讨论/data.json') as f:
# #     data = json.load(f)
# #     print(data['intro'][0])

if __name__ == "__main__":
    main(sys.argv[1:])
