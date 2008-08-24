"""This is oldowan.structure.read."""

__all__ = ['read_structure']

from oldowan.structure.iterate import iterate_structure
from oldowan.structure.iterate import iterate_structure_results

def read_structure(something, what='guess', raw=False):
    """Read Structure format."""
    items = []
    for item in iterate_structure(something, what=what, raw=raw):
        items.append(item)
    return items

def read_structure_results(something, what='guess', raw=False):
    """Read Structure results."""
    items = []
    for item in iterate_structure_results(something, what=what, raw=raw):
        items.append(item)
    return items
