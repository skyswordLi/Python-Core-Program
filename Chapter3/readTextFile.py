# get filename
fileName = raw_input('Enter filename:')

# attempt to open file for reading
try:
    fileObject = open(fileName, 'r')
except IOError:
    print "*** file open error!"
else:
    # display contents to screen
    for eachLine in fileObject:
        print eachLine
    fileObject.close()
