'''
Created on Mar 21, 2011

@author: jeroen
'''

import os
from phpstat import FileInfo, DirInfo

class DirWalker(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        
    def get_dir_info(self, rootdir):
        dir = DirInfo(rootdir)

        for item in os.listdir(rootdir):
            fullname = os.path.join(rootdir, item)
            
            if not item.startswith('.') and not os.path.islink(fullname):
                if os.path.isdir(fullname):
                    dir.add_dir(self.get_dir_info(fullname))
                else :
                    file = FileInfo(item)
                    file.filesize = 42
                    dir.add_file(file)
        
        return dir
        
    def get_file_stats(self, filepath):
        return filepath
        