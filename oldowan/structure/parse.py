"""This is oldowan.structure.parse."""

import re

__all__ = ['parse_structure']

#
# PARSER
#

def parse_structure(entry):
    """Parse Structure format."""
    raise NotImplementedError

def parse_structure_results(entry):
    """Parse Structure results."""
    result = {}
    
    ia_start = entry.find('Inferred ancestry of individuals')
    ia_end   = entry.find('Estimated Allele Frequencies in each cluster')

    if not isinstance(ia_start, int) or not isinstance(ia_end, int) or ia_start >= ia_end:
        # need to define a custom exception somewhere
        raise AttributeError

    K_mo = RE_K.search(entry)
    result['K'] = int(K_mo.group('K'))
    result['inferred_ancestry'] = parse_inferred_ancestry(entry[ia_start:(ia_end-1)])

    return result

# 
# PRIVATE UTILITY FUNCTIONS USED IN PARSER
#
# These functions are implementation details and should not be used outside of
# this parser. There is no guarantee that any of these will be maintained or
# necessarily function the same as the parser evolves. The call signature and
# return values of the 'parse_genbank' function are the only supported public
# interface.
#

def parse_inferred_ancestry(block):
    lines = RE_NEWLINE.split(block)
    result = []
    for l in lines:
        mo = RE_PROBSLINE.match(l)
        if mo is not None:
            cur = {}
            cur['label'] = mo.group('label')
            cur['missing'] = float(mo.group('missing'))
            cur['pop'] = mo.group('pop')
            probs = mo.group('probs')
            if probs.find('|') >= 0:
                if probs.find('*'):
                    cur['migrant'] = True
                cur['usedpop'] = True
                holder = {}
                pes = probs.split('|')
                holder[int(cur['pop'])] = float(pes[0].strip())
                prob_entries = list(x for x in pes[1:] if len(x.strip()) > 0 and not x.strip().startswith('*'))
                for s in prob_entries:
                    upmo = RE_USEPOP.match(s)
                    holder[int(upmo.group('pop'))] = float(upmo.group('prob'))
                hkeys = holder.keys()
                hkeys.sort()
                cprobs = []
                for k in hkeys:
                    cprobs.append(holder[k])
                cur['probs'] = cprobs
            else:
                cur['usedpop'] = False
                cur['probs'] = list(float(x) for x in probs.strip().split())
            result.append(cur)
    return result

#
# REGULAR EXPRESSIONS USED IN PARSER
#

#: Match newlines
RE_NEWLINE       = re.compile(r'\r\n|\r|\n')

#: Match integers
RE_INTEGER       = re.compile(r'[0-9]+')

#: Match inferred ancestry probabilities line
RE_PROBSLINE     = re.compile(r'\s*[0-9]+\s+(?P<label>\S+)\s+\((?P<missing>[0-9.]+)\)\s+(?P<pop>[0-9]+)\s+:(?P<probs>.*)')

#: Match USEPOP probabilities
RE_USEPOP        = re.compile(r'\s*Pop\s+(?P<pop>[0-9]+)\s*:\s+(?P<prob>[0-9.]+)')

#: Find the K parameter
RE_K             = re.compile(r'MAXPOPS=(?P<K>[0-9]+)')
