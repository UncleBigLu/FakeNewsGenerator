import sys, getopt

def readArgv(argv):
    # Get and parse command line argvs
    ret = {'type':'', 'topic': '', 'time': '', 'position': '', 'members': []}
    try:
        opts, args = getopt.getopt(argv, "h", ["type=", "topic=", "time=", "position=", "members="])
    except getopt.GetoptError:
        print(
            'Usage: newsGenerator.py --topic <topic> --time <time> --position <position> --members <member1[，member2，member3]>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(
                'Usage: newsGenerator.py --topic <topic> --time <time> --position <position> --members <member1[,member2,member3]>')
            sys.exit()
        elif opt == '--type':
            ret['type'] = arg
        elif opt == '--topic':
            ret['topic'] = arg
        elif opt == '--time':
            ret['time'] = arg
        elif opt == '--position':
            ret['position'] = arg
        elif opt == '--members':
            members = arg

    ret['members'] = members.split('，')
    return ret
