'''
Created on Mar 22, 2011

@author: jeroen
'''

from fileinfo import FileInfo
from dirinfo import DirInfo

class DirPrinter(object):
    
    def prnt(self, dir):
        return repr_as_indented_list(dir, 0)
        
def repr_as_indented_list(dir, indentLevel):
    if indentLevel > 10:
        raise Exception("recursion")
        #raise Exception("\n".join([d.__repr__() for d in dir.get_dirs()]))
    
    segments = []
    indent = "    " * indentLevel
    
    segments.append('\n' + indent + dir.get_path())

    for file in dir.get_files():
        segments.append(indent +  "-- " + file.get_filename())
    
    for subdir in dir.get_dirs():
        #segments.append('\n' + indent +  indent + subdir.__repr__())
        segments.append(repr_as_indented_list(subdir, indentLevel + 1))              

    return '\n'.join(segments)        