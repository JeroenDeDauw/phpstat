'''
Created on Mar 22, 2011

@author: jeroen
'''

import os
from fileinfo import FileInfo

class DirInfo(object):
    '''
    Simple class to represent a directory and obtain data about if when needed.
    '''
    
    def __init__(self, path, recursive=False):
        '''
        Constructor
        '''
        
        self._path = path
        self._initiated = False
        self._recursive = recursive
        
        self._files = []
        self._dirs = []
        
        self._filecount = 0
        self._dircount = 0
        self._totalsize = -1
        self._codelines = 0
        self._commentlines = 0
        self._whitespacelines = 0
        
    '''
    Check if the dir data is cached, and if not, obtain it.
    '''
    def _init_if_needed(self):
        if not self._initiated:
            self._initiated = True
            self._get_dir_info(self._path)
    
    def _get_dir_info(self, rootdir):
        for item in os.listdir(rootdir):
            fullname = os.path.join(rootdir, item)
            
            if not item.startswith('.') and not os.path.islink(fullname):
                if os.path.isdir(fullname):
                    dir = DirInfo(fullname, self._recursive)
                    self._dirs.append(dir)
                    self._dircount += 1
                    
                    if self._recursive:
                        self._filecount += dir.get_filecount()
                        self._dircount += dir.get_dircount()
                        self._totalsize += dir.get_totalsize()
                else:
                    file = FileInfo(rootdir, item)
                    self._files.append(file)
                    self._filecount += 1
                    self._totalsize += file.get_filesize()
    
    def __repr__(self, recursive=None):
        self.set_recursive(recursive)
        self._init_if_needed()
        return "%r (%r dirs, %r files) %r" % (
           self._path,
           self._dircount,
           self._filecount,
           self._totalsize
        )     
    
    '''
    Sets that the directory should report data obtained recursivly,
    or only look at what's directly in it. Note that changing the
    recursive setting invalidates the cached info.
    '''        
    def set_recursive(self, recursive):
        if recursive is not None and recursive != self._recursive:
            self._recursive = recursive
            self._initiated = False
    
    def get_files(self):
        self._init_if_needed()
        return self._files
    
    def get_dirs(self):
        self._init_if_needed()
        return self._dirs
    
    def get_path(self):
        return self._path
    
    def get_totalsize(self):
        self._init_if_needed()
        return self._totalsize
    
    def get_code_lines(self):
        self._init_if_needed()
        return self._codelines
    
    def get_comment_lines(self):
        self._init_if_needed()
        return self._commentlines
    
    def get_whitespace_lines(self):
        self._init_if_needed()
        return self._whitespacelines
    
    def get_line_count(self):
        self._init_if_needed()
        return self._codelines + self._commentlines + self._whitespacelines
    
    def get_filecount(self):
        self._init_if_needed()
        return self._filecount
    
    def get_dircount(self):
        self._init_if_needed()
        return self._dircount     