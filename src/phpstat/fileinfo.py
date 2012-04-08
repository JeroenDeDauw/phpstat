'''
Created on Mar 22, 2011

@author: jeroen
'''

import os
from bytesize import ByteSize

class FileInfo(object):
    '''
    Simple class to represent a file and obtain data about if when needed.
    '''
    
    def __init__(self, dirpath, filename):
        '''
        Constructor
        '''
        self._filename = filename
        self._dirpath = dirpath
            
        self._filesize = -1
        self._codelines = 0
        self._commentlines = 0
        self._whitespacelines = 0 
        
        self._initiated = False
    
    '''
    Check if the file data is cached, and if not, obtain it.
    '''        
    def _init_if_needed(self):
        if not self._initiated:
            self._initiated = True
            self._get_file_stats()     
    
    def _get_file_stats(self):
        path = os.path.join(self._dirpath, self._filename)
        self._filesize = os.path.getsize(path)
        
        with open(path, 'r') as file:
            inCommentBlock = False
            
            for line in file.readlines():
                stripped = line.strip()
                if len(stripped) == 0:
                    self._whitespacelines += 1
                elif inCommentBlock or stripped.startswith('#') or stripped.startswith('//'):
                    self._commentlines += 1
                    if stripped.count('*/') > 0:
                        inCommentBlock = False
                else:
                    if stripped.count('/*') > 0:
                        inCommentBlock = True
                        self._commentlines += 1
                    else:
                        self._codelines += 1
    
    def __repr__(self):
        return "%s (%s lines: %s code, %s comment, %s empty) %s" % (
            self._filename,
            self.get_line_count(),
            self.get_code_lines(),
            self.get_comment_lines(),
            self.get_whitespace_lines(),
            ByteSize(self.get_filesize()).__repr__()
        )       
        
    def get_filename(self):
        return self._filename
    
    def get_filesize(self):
        self._init_if_needed()
        return self._filesize
    
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