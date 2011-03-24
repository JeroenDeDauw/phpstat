'''
Created on Mar 23, 2011

@author: jeroen
'''

import math

class ByteSize(object):
    '''
    Simple class to get a representatation of a byte size
    '''
    
    _units = {
        1: 'k',
        2: 'M',
        3: 'G',
        4: 'T',
        5: 'P',
        6: 'E',
        7: 'Z',
        8: 'Y'
    }
    
    def __init__(self, byteCount, binaryUnits=True):
        '''
        Constructor
        '''
        
        self._byteCount = byteCount
        self._binaryUnits = binaryUnits
        
    def __repr__(self):
        if self._byteCount > 0 :
            base = math.pow(2, 10) if self._binaryUnits else math.pow(10, 3)
            log = math.floor(math.log(self._byteCount, base))
        else:
            log = 0

        if log == 0:
            return str(self._byteCount) + " " + ("byte" if self._byteCount == 1 else "bytes")
        else:
            log = min([8, log])
            count = round(self._byteCount / pow(base, log), 2)
            return "%r %r%rB" % (str(count), self._units[log], "i" if self._binaryUnits else "")
