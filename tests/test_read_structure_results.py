from oldowan.structure import read_structure_results
from oldowan.structure import iterate_structure_results

import os

STRUCTURE_OUT_FILEPATH = os.path.join(os.path.dirname(__file__), 
        'test_files', 'structure_out_1.txt')
_f = open(STRUCTURE_OUT_FILEPATH)
STRUCTURE_OUT_TEXT = _f.read()
_f.close()

def test_read_structure_results_from_text():
    """read_structure results given text"""
    # first, explicitly tell it this is text
    entries = read_structure_results(STRUCTURE_OUT_TEXT, what='text')
    assert 1 == len(entries)

    # next, make it guess
    entries = read_structure_results(STRUCTURE_OUT_TEXT)
    assert 1 == len(entries)

def test_read_structure_results_from_filename():
    """read_structure results given filename"""
    # first, explicitly tell it this is a filename
    entries = read_structure_results(STRUCTURE_OUT_FILEPATH, what='filename')
    assert 1 == len(entries)

    # next, make it guess
    entries = read_structure_results(STRUCTURE_OUT_FILEPATH)
    assert 1 == len(entries)

def test_read_structure_results_from_file():
    """read_structure results given file"""
    # first, explicitly tell it this is a file
    f = open(STRUCTURE_OUT_FILEPATH, 'r')
    entries = read_structure_results(f, what='file')
    assert 1 == len(entries)

    # next, make it guess
    f = open(STRUCTURE_OUT_FILEPATH, 'r')
    entries = read_structure_results(f)
    assert 1 == len(entries)

def test_iterate_structure_results_with_dict_return():
    """iterate_structure results with default options"""
    # first, from text
    for entry in iterate_structure_results(STRUCTURE_OUT_TEXT):
        assert isinstance(entry, dict)
    # next, from file
    for entry in iterate_structure_results(STRUCTURE_OUT_FILEPATH):
        assert isinstance(entry, dict)

def test_iterate_structure_results_with_raw_return():
    """iterate_structure results with raw option"""
    # first, from text
    for entry in iterate_structure_results(STRUCTURE_OUT_TEXT, raw=True):
        assert isinstance(entry, str)
    # next, from file
    for entry in iterate_structure_results(STRUCTURE_OUT_FILEPATH, raw=True):
        assert isinstance(entry, str)

