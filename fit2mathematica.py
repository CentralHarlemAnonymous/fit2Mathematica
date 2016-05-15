#!/usr/bin/env python

import os
import sys

# Add folder to search path

PROJECT_PATH = os.path.realpath(os.path.join(sys.path[0], '..'))
sys.path.append(PROJECT_PATH)

from fitparse import Activity

quiet = 'quiet' in sys.argv or '-q' in sys.argv
#filenames = None
filenames = [os.path.join(PROJECT_PATH, 'tests', 'data', '2016-04-30-21-57-29.fit')]
outFile = os.path.join(PROJECT_PATH, 'tests', 'data', '2016-04-30-21-57-29.txt')

if len(sys.argv) >= 2:
    filenames = [f for f in sys.argv[1:] if os.path.exists(f)]

if not filenames:
    filenames = [os.path.join(PROJECT_PATH, 'tests', 'data', 'sample-activity.fit')]

def print_record(rec, ):
    global record_number
    global localString
    record_number += 1
    if record_number <= 9999999:  # for debugging, limits output to five records
        localString += ("\n<|\"record number\"-> %d, \"type\"-> \"%s\", \"fields\"->{" % (record_number, rec.type.name))
        shortFields = rec.fields[0:99] # for debugging, limits the number of fields per record
        for field in shortFields:
            localString += "<|\"name\"->\"%s\", \"type\"->\"%s\", \"data\"->\"%s\", \"unit\"->\"%s\"|>," % (field.name, field.type.name, field.data, field.units)
        localString = localString[:-1]
        localString += "}|>, "
    else:
    	localString+=""

# the program as such starts below
for f in filenames:
    #first prints a header?
    if quiet:
        print f
    else:
        print ('##### %s ' % f).ljust(60, '#')

    record_number = 0
    localString = ""
    a = Activity(f)
    localString= "{"
    a.parse(print_record) # calls the interesting function
    localString = localString[:-2]
    localString += "\n}"
    file = open(outFile,"w")
    file.write(localString)
    file.close()
#    print (" %s " % (localString))

