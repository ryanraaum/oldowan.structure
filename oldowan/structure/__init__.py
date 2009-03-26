"""This is the OldowanGenbank package."""

import os

VERSION = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'VERSION')).read().strip()

__all__ = ['read_structure', 
           'read_structure_results',
           'iterate_structure', 
           'iterate_structure_results',
           'parse_structure', 
           'parse_structure_results',
           'write_structure']

from oldowan.structure.read import read_structure
from oldowan.structure.read import read_structure_results
from oldowan.structure.iterate import iterate_structure
from oldowan.structure.iterate import iterate_structure_results
from oldowan.structure.parse import parse_structure
from oldowan.structure.parse import parse_structure_results
from oldowan.structure.write import write_structure

