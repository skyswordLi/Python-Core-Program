import os
import sys
files = []

def getAllFiles( dirName ):
    for file in os.listdir( dirName ):
        if os.path.isdir( dirName + os.sep + file ):
            getAllFiles( dirName + os.sep + file )
        else:
            files.append( dirName + os.sep + file )

getAllFiles( r'F:\Applications\Python34\Lib\asyncio' )

hasDoc = False
strTemp = ''

try:
    with open( 'hasdoc.txt', 'a+' ) as file1:
        try:
            with open( 'nodoc.txt', 'a+' ) as file2:
                for file in files:
                    try:
                        with open( file, mode = 'r', buffering = -1, encoding = 'utf-8' ) as fobj:
                            for line in fobj:
                                if not hasDoc and line.startswith( '"""' ):
                                    hasDoc = True
                                elif hasDoc and line.startswith( '"""' ):
                                    hasDoc = False
                                    strTemp += line
                                    break
                                if hasDoc:
                                    strTemp += line
                                else:
                                    break
                            if strTemp != '':
                                file1.write( 'File name: ' + file + '\n' )
                                file1.write( '__doc__ is: ' + '\n' )
                                file1.write( strTemp + '\n' )
                            else:
                                file2.write( 'File name: ' + file + '\n' )
                            strTemp = ''
                    except Exception as e:
                        print( e )
        except Exception as e:
            print( e )
except Exception as e:
    print( e )
    
