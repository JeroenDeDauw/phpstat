'''
Created on Mar 22, 2011

@author: jeroen
'''

class DirPrinter(object):
    
    def prnt(self, dir):
        return self.repr_as_indented_list(dir, 0)
        
    def repr_as_indented_list(self, dir, indentLevel):
        segments = []
        indent = "    " * indentLevel
        
        segments.append('\n' + indent +  "-- " + indent + dir.__repr__())
        
        for file in dir.get_files():
            segments.append(indent +  "-- " + file.__repr__())
        
        for dir in dir.get_dirs():
            segments.append(self.repr_as_indented_list(dir, indentLevel + 1))              
        
        return '\n'.join(segments)        