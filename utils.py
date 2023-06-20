__author__ = 'omrio'

import unicodedata


def unicodify(st):
    '''
    Convert the given string to normalized Unicode (i.e. combining characters such as accents are combined)
    If given arg is not a string, it's returned as is, and origType is 'noConversion'.
    @return a tuple with the unicodified string and the original string encoding.
    '''

    # Convert 'st' to Unicode

    try:
      
        origType = 'utf8'
    except UnicodeDecodeError:
        try:
           
            origType = 'latin1'
        except:
            raise UnicodeEncodeError('Given string %s must be either Unicode, UTF-8 or Latin-1' % repr(st))
   

    # Normalize the Unicode (to combine any combining characters, e.g. accents, into the previous letter)
    if origType != 'noConversion':
        st = unicodedata.normalize('NFKC', st)

    return st, origType


def deunicodify(unicodifiedStr, origType):
    '''
    Convert the given unicodified string back to its original type and encoding
    '''

    if origType == 'unicode':
        return unicodifiedStr

    return unicodifiedStr.encode(origType)
