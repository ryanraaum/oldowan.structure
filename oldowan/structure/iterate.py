
__all__ = ['iterate_structure']

from oldowan.structure.parse import parse_structure
from oldowan.structure.parse import parse_structure_results

import re, StringIO

def iterate_structure(something, what='guess', raw=False):
    """Iterate through blocks of Structure format."""
    if what == 'guess':
        if type(something) == file:
            what = 'file'
        elif type(something) == str:
            if len(something) > 256:
                what = 'text'
            else:
                what = 'filename'
    if what == 'file':
        f = something
    elif what == 'filename':
        f = open(something, 'r')
    elif what == 'text':
        f = StringIO.StringIO(something)
    else:
        raise TypeError("don't know how to handle '%s'" % what)
    
    raise NotImplementedError

def iterate_structure_results(something, what='guess', raw=False):
    """Iterate through Structure results."""
    if what == 'guess':
        if type(something) == file:
            what = 'file'
        elif type(something) == str:
            if len(something) > 256:
                what = 'text'
            else:
                what = 'filename'
    if what == 'file':
        f = something
    elif what == 'filename':
        f = open(something, 'r')
    elif what == 'text':
        f = StringIO.StringIO(something)
    else:
        raise TypeError("don't know how to handle '%s'" % what)
    
    # find the beginning of the first entry
    buf = ''
    while not buf.startswith('----------------------------------------------------'):
        buf = f.readline()

    if buf == '':
        f.close()
        raise IOError("file '%s' does not appear to be a STRUCTURE results file" % filename)

    following = f.readline()
    if not following.startswith('STRUCTURE'):
        f.close()
        raise IOError("file '%s' does not appear to be a STRUCTURE results file" % filename)

    done = False
    while not done:
        entry = []
        while buf != '':
            entry.append(buf)
            if following is not None:
                entry.append(following)
                following = None
            buf = f.readline()
            # read until the next entry ('STRUCTURE') or end of file ('')
            if buf.startswith('STRUCTURE') or buf == '':
                if raw:
                    yield ''.join(entry[:-1])
                else:
                    yield parse_structure_results(''.join(entry[:-1]))
                entry = [entry[-1]]
        f.close()
        done = True

