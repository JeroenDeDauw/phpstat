'''
Created on Mar 21, 2011

@author: jeroen
'''

import os

class DirWalker(object):
    '''
    classdocs
    '''
    
    _files = []
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
    def walk(self, rootdir):
        fileList = {}
        dirStack = [rootdir]

        while dirStack:
            directory = dirStack.pop()
            fileList[directory] = []
            
            for item in os.listdir(directory):
                if not item.startswith('.'):
                    fullname = os.path.join(directory, item)
                    
                    if os.path.isdir(fullname):
                        if not os.path.islink(fullname): dirStack.append(fullname)
                    else :
                        fileList[directory].append(item)
        
        self._files =  fileList 
        
    def get_file_stats(self, filepath):
        return filepath
    
    def get_stats(self):
        files = []
        for dir, data in self._files.iteritems():
            files.append(dir + "\n-- " + "\n-- ".join(data) + "\n")
        return '\n'.join(files)