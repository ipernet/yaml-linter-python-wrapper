#!/usr/bin/python

import yaml, sys, getopt, os.path

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:")
    except getopt.GetoptError:
        print 'linter.py -i <inputfile.yml>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'linter.py -i <inputfile.yml>'
            sys.exit()
        elif opt == '-i':
            if os.path.isfile(arg):
                stream = open(arg, 'r')
                try:
                    yaml.safe_load(stream)
                    sys.exit()
                except yaml.scanner.ScannerError:
                    sys.exit(1)
            else:
                print "Input file is missing or not readable"
                sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
