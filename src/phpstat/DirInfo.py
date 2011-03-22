'''
Created on Mar 22, 2011

@author: jeroen
'''

class DirInfo(object):
    '''
    classdocs
    '''
    
    _path = ''
    _files = []
    _dirs = []

    def __init__(self, path):
        '''
        Constructor
        '''
        
        self._path = path
        
    def __repr__(self):
        pass
        
    def add_file(self, file):
        self._files.append(file)
        
    def add_dir(self, dir):
        self._dirs.append(dir)        
        
    def get_files(self):
        return self._files
    
    def get_dirs(self):
        return self._dirs
    
    def get_path(self):
        return self._path
        