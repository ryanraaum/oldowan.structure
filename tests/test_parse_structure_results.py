from oldowan.structure import parse_structure_results

import os

STRUCTURE_OUT_FILEPATH = os.path.join(os.path.dirname(__file__), 
        'test_files', 'structure_out_1.txt')
_f = open(STRUCTURE_OUT_FILEPATH)
STRUCTURE_OUT_TEXT = _f.read()
_f.close()

def test_parser_returns_proper_type():
    """parser returns a dict."""
    result = parse_structure_results(STRUCTURE_OUT_TEXT) 
    assert isinstance(result, dict)

def test_keys_of_parsed_result_dict():
    """dict from parser has proper keys."""
    result = parse_structure_results(STRUCTURE_OUT_TEXT) 
    # note, most of this remains to be implemented
    #assert result.has_key('version')
    #assert result.has_key('run_parameters')
    #assert result.has_key('membership_proportions')
    #assert result.has_key('allele_frequency_divergence')
    #assert result.has_key('ln_prob_of_data')
    #assert result.has_key('mean_ln_likelihood')
    #assert result.has_key('var_ln_likelihood')
    #assert result.has_key('mean_alpha')
    #assert result.has_key('fsts')
    assert result.has_key('inferred_ancestry')
    #assert result.has_key('estimated_allele_frequencies')
    #assert result.has_key('analysis_parameters')

def test_inferred_ancestry_section_parsing():
    """inferred ancestry section correctly parsed."""
    result = parse_structure_results(STRUCTURE_OUT_TEXT) 
    ia = result['inferred_ancestry']
    assert isinstance(ia, list)
    assert 150 == len(ia)
    for l in ia:
        assert isinstance(l, dict)
        assert l.has_key('label')
        assert l.has_key('missing')
        assert l.has_key('pop')
        assert l.has_key('probs')
        assert l.has_key('usedpop')
        probs = l['probs']
        assert isinstance(probs, list)
        assert 2 == len(probs)
    # some spot checks...
    assert 1.000 == ia[0]['probs'][0]
    assert 0.000 == ia[0]['probs'][1]
    assert 0.998 == ia[10]['probs'][0]
    assert 0.002 == ia[10]['probs'][1]
    assert 0.000 == ia[50]['probs'][0]
    assert 1.000 == ia[50]['probs'][1]
    assert 0.001 == ia[99]['probs'][0]
    assert 0.999 == ia[99]['probs'][1]
    assert 0.513 == ia[100]['probs'][0]
    assert 0.487 == ia[100]['probs'][1]
    
