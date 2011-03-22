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
            
        self.filesize = -1
        self.codelines = -1
        self.commentlines = -1
        self.whitespacelines = -1 
    
    def get_file_stats(self, filepath):
        return filepath    
    
    def __repr__(self):
        return self._filename + " ~fancy stats be here~"
        
    def get_filename(self):
        return self._filename