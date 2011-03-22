'''
Created on Mar 22, 2011

@author: jeroen
'''

class DirPrinter(object):
    
    def prnt(self, dir):
        return repr_as_indented_list(dir, 0)
        
def repr_as_indented_list(dir, indentLevel):
    segments = []
    indent = "    " * indentLevel
    
    segments.append('\n' + indent + dir.get_path())

    for file in dir.get_files():
        segments.append(indent +  "-- " + file.get_filename())
    
#    for subdir in dir.get_dirs():
#        segments.append('\n' + indent +  indent + subdir.__repr__())
#        segments.append(repr_as_indented_list(subdir, indentLevel + 1))              

    return '\n'.join(segments)        