import sys, getopt


def read_argv(argv):
    # Get and parse command line argvs
    usage = 'Usage: newsGenerator.py --type <type> --topic <topic> --time <time> --position <position> --members <member1[，member2，member3]>'
    ret = {'type':'', 'topic': '', 'time': '', 'position': '', 'members': []}
    try:
        opts, args = getopt.getopt(argv, "h", ["type=", "topic=", "time=", "position=", "members="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    if(len(opts) != 5):
        print(usage)
        sys.exit(1)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
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
