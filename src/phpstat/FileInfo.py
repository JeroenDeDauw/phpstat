'''
Created on Mar 22, 2011

@author: jeroen
'''

class FileInfo(object):
    '''
    classdocs
    '''
    
    filesize = -1
    codelines = -1
    commentlines = -1
    whitespacelines = -1 
    
    _filename = ''
    
    def __init__(self, filename):
        '''
        Constructor
        '''
        self._filename = filename
        
    def __repr__(self):
        pass
        
    def get_filename(self):
        return self._filename