'''
Created on Mar 21, 2011

@author: jeroen
'''

import os

class DirWalker(object):
    '''
    classdocs
    '''
    
    _tree = []
    
    def __init__(self):
        '''
        Constructor
        '''
        
        
    def walk(self, rootdir):
        self._tree = self.walk_through_dir(rootdir)
        
    def walk_through_dir(self, rootdir):
        itemList = {'files': {}, 'dirs': {}}

        for item in os.listdir(rootdir):
            fullname = os.path.join(rootdir, item)
            
            if not item.startswith('.') and not os.path.islink(fullname):
                if os.path.isdir(fullname):
                    itemList['dirs'][item] = self.walk_through_dir(fullname)
                else :
                    itemList['files'][item] = self.get_file_stats(fullname)
        
        return itemList     
        
    def get_file_stats(self, filepath):
        return filepath
    
    def get_stats(self):
        return self.repr_as_indented_list(self._tree, 0)
    
    def repr_as_indented_list(self, tree, indentLevel):
        segments = []
        
        for file, data in tree['files'].iteritems():
            segments.append("  " * indentLevel +  "-- " + file + ": " + "example data" + "\n")
            
        for dir, data in tree['dirs'].iteritems():
            segments.append("  " * indentLevel +  "-- " + dir + ": " + "example dir data" + "\n")
            segments.append(self.repr_as_indented_list(data, indentLevel + 1))            
        
        return ''.join(segments)
        