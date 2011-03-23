'''
Created on Mar 22, 2011

@author: jeroen
'''

import os
from fileinfo import FileInfo

class DirInfo(object):
    '''
    classdocs
    '''
    
    def __init__(self, path):
        '''
        Constructor
        '''
        
        self._path = path
        self._files = []
        self._dirs = []
        self._initiated = False       
    
    def init_if_needed(self):
        if not self._initiated:
            self._initiated = True
            self._get_dir_info(self._path)
    
    def _get_dir_info(self, rootdir):
        for item in os.listdir(rootdir):
            fullname = os.path.join(rootdir, item)
            
            if not item.startswith('.') and not os.path.islink(fullname):
                if os.path.isdir(fullname):
                    self._dirs.append(DirInfo(fullname))
                else :
                    file = FileInfo(rootdir, item)
                    file.filesize = 42
                    self._files.append(file)
    
    def __repr__(self):
        self.init_if_needed()
        return "%r (%r dirs, %r files)" % (self._path, len(self._dirs), len(self._files))     
        
    def get_files(self):
        self.init_if_needed()
        return self._files
    
    def get_dirs(self):
        self.init_if_needed()
        return self._dirs
    
    def get_path(self):
        return self._path
        