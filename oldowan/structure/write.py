"""This is oldowan.structure.write."""

__all__ = ['write_structure']

def write_structure(something, entry_list, what='guess'):
    """Write list of structure data to file.
    
    The expected configuration of the structure_data is as follows:
    * entry_list is a list
    * each entry is a dict
    * each entry requires keys:
        * 'label' - value is a string
        * 'genotypes' - value is a list of tuples
        * 'pop' - value is an integer
    * an optional key:
        * 'usepop' - True or False (False by default)
    """
    if what == 'guess':
        if type(something) == file:
            what = 'file'
        elif type(something) == str:
            what = 'filename'
    if what == 'file':
        f = something
    elif what == 'filename':
        f = open(something, 'w')
    else:
        raise TypeError("don't know how to handle '%s'" % what)

    for entry in entry_list:
        write_structure_entry(f, entry)
    if what == 'filename':
        f.close()

def write_structure_entry(f, entry):
    """Write a structure entry to the given file object."""
    usepop = entry.has_key('usepop') and entry['usepop'] or False
    usepop = usepop and 1 or 0
    alleles1 = []
    alleles2 = []
    for t in entry['genotypes']:
        alleles1.append(str(t[0]))
        alleles2.append(str(t[1]))
    row1_alleles = ' '.join(alleles1)
    row2_alleles = ' '.join(alleles2)

    row1 = '%s %d %d %s\n' % (entry['label'], entry['pop'], usepop, row1_alleles)
    row2 = '%s %d %d %s\n' % (entry['label'], entry['pop'], usepop, row2_alleles)

    f.write(row1)
    f.write(row2)

