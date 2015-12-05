import os
import sys
files = []


def get_all_files(dir_name):
    for every_file in os.listdir(dir_name):
        if os.path.isdir(dir_name + os.sep + every_file):
            get_all_files(dir_name + os.sep + every_file)
        else:
            files.append(dir_name + os.sep + every_file)

get_all_files(r'F:\Applications\Python34\Lib\asyncio')

hasDoc = False
strTemp = ''

try:
    with open('hasdoc.txt', 'a+') as file1:
        try:
            with open('nodoc.txt', 'a+') as file2:
                for each_file in files:
                    try:
                        with open(each_file, mode='r', buffering=-1, encoding='utf-8') as file_obj:
                            for line in file_obj:
                                if not hasDoc and line.startswith('"""'):
                                    hasDoc = True
                                elif hasDoc and line.startswith('"""'):
                                    hasDoc = False
                                    strTemp += line
                                    break
                                if hasDoc:
                                    strTemp += line
                                else:
                                    break
                            if strTemp != '':
                                file1.write('File name: ' + each_file + '\n')
                                file1.write('__doc__ is: ' + '\n')
                                file1.write(strTemp + '\n')
                            else:
                                file2.write('File name: ' + each_file + '\n')
                            strTemp = ''
                    except Exception as e:
                        print e
        except Exception as e:
            print e
except Exception as e:
    print e
