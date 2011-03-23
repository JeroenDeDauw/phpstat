'''
Created on Mar 22, 2011

@author: jeroen
'''

class FileInfo(object):
    '''
    classdocs
    '''
    
    def __init__(self, filename):
        '''
        Constructor
        '''
        self._filename = filename
            
        self._filesize = -1
        self._codelines = -1
        self._commentlines = -1
        self._whitespacelines = -1 
        
        self._initiated = False
    
    def _get_file_stats(self):
        pass 
    
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