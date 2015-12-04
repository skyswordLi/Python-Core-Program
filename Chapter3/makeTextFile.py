import os

ls = os.linesep

fileName = raw_input("filename = ")
# get filenames
while True:
    if os.path.exists(fileName):
        print"ERROR: %s already exits." % fileName
    else:
        break

# get file content (text) lines
all = []
print "\nEnter lines ('.' by itself to quit)."

# loop until user terminate input
while True:
    entry = raw_input('>>>')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fileObject = open(fileName, 'w')
fileObject.writelines(["%s%s" % (x, ls) for x in all])
fileObject.close()
print "DONE!"
