fileName = raw_input('Enter file name:')
file_obj = open(fileName, 'r')
for eachLine in file_obj:
    print eachLine
fobj.close()
