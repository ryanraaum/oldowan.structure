from oldowan.structure.write import write_structure

ENTRY1 = {  'label': 'e1',
            'pop': 1,
            'usepop': True,
            'genotypes': [ (120,120), (210,210) ] }
ENTRY2 = {  'label': 'e2',
            'pop': 2, 
            'genotypes': [ (120,124), (210,212) ] }

SIMPLE_ENTRIES = [ENTRY1, ENTRY2]

def test_simple_output():
    """Write a simple structure file."""
    write_structure('test.structure', SIMPLE_ENTRIES)    
