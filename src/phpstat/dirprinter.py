'''
Created on Mar 22, 2011

@author: jeroen
'''

class DirPrinter(object):
    
    def prnt(self, dir):
        return self.repr_as_indented_list(dir, 0)
        
    def repr_as_indented_list(self, dir, indentLevel):
        if indentLevel > 10:
            raise Exception("recursion")
            #raise Exception("\n".join([d.__repr__() for d in dir.get_dirs()]))
        
        segments = []
        indent = "    " * indentLevel
        
        segments.append('\n' + indent + dir.__repr__())
    
        for file in dir.get_files():
            segments.append(indent +  "-- " + file.__repr__())
        
        for subdir in dir.get_dirs():
            segments.append(self.repr_as_indented_list(subdir, indentLevel + 1))              
    
        return '\n'.join(segments)        