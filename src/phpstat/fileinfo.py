'''
Created on Mar 22, 2011

@author: jeroen
'''

import os

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
    
    def _get_file_stats(self):
        with open(os.path.join(self._dirpath, self._filename), 'r') as file:
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
                    self._codelines += 1
                    if stripped.count('/*') > 0:
                        inCommentBlock = True
    
    def __repr__(self):
        return "%r (%r lines: %r code, %r comment, %r empty) %r" % (
            self._filename,
            self.get_line_count(),
            self.get_code_lines(),
            self.get_comment_lines(),
            self.get_whitespace_lines(),
            self.get_filesize()
        )
        
    def init_if_needed(self):
        if not self._initiated:
            self._initiated = True
            self._get_file_stats()        
        
    def get_filename(self):
        return self._filename
    
    def get_filesize(self):
        self.init_if_needed()
        return self._filesize
    
    def get_code_lines(self):
        self.init_if_needed()
        return self._codelines
    
    def get_comment_lines(self):
        self.init_if_needed()
        return self._commentlines
    
    def get_whitespace_lines(self):
        self.init_if_needed()
        return self._whitespacelines
    
    def get_line_count(self):
        self.init_if_needed()
        return self._codelines + self._commentlines + self._whitespacelines