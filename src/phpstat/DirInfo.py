'''
Created on Mar 22, 2011

@author: jeroen
'''

import os
from FileInfo import FileInfo

class DirInfo(object):
    '''
    classdocs
    '''
    
    _path = ''
    _files = []
    _dirs = []
    _initiated = False

    def __init__(self, path):
        '''
        Constructor
        '''
        
        self._path = path
    
    def init_if_needed(self):
        if not self._initiated:
            self._initiated = True
            self.get_dir_info(self._path)
    
    def get_dir_info(self, rootdir):
        self._files.append(FileInfo('foo'))
        #for item in os.listdir(rootdir):
#            fullname = os.path.join(rootdir, item)
            
#            if not item.startswith('.') and not os.path.islink(fullname):
#                if os.path.isdir(fullname):
#                    self._dirs.append(DirInfo(fullname))
#                else :
#            file = FileInfo(item)
#            file.filesize = 42
              #self._files.append(item)
        
    def __repr__(self):
        #self.init_if_needed()
        return self._path + " ~some fancy stats be here~"     
        
    def get_files(self):
        self.init_if_needed()
        return self._files
    
    def get_dirs(self):
        self.init_if_needed()
        return self._dirs
    
    def get_path(self):
        return self._path
        