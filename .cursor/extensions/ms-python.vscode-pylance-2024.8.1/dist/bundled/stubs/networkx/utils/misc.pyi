import sys
import uuid
import warnings
from collections import defaultdict, deque
from collections.abc import Iterable, Iterator, Sized
from itertools import chain, tee

from ..classes.graph import Graph

__all__ = [
    "is_string_like",
    "iterable",
    "empty_generator",
    "flatten",
    "make_list_of_ints",
    "is_list_of_ints",
    "make_str",
    "generate_unique_node",
    "default_opener",
    "dict_to_numpy_array",
    "dict_to_numpy_array1",
    "dict_to_numpy_array2",
    "is_iterator",
    "arbitrary_element",
    "consume",
    "pairwise",
    "groups",
    "to_tuple",
    "create_random_state",
    "create_py_random_state",
    "PythonRandomInterface",
    "nodes_equal",
    "edges_equal",
    "graphs_equal",
]

# some cookbook stuff
# used in deciding whether something is a bunch of nodes, edges, etc.
# see G.add_nodes and others in Graph Class in networkx/base.py

def is_string_like(obj): ...
def iterable(obj): ...
def empty_generator(): ...
def flatten(obj, result=None): ...
def make_list_of_ints(sequence): ...
def is_list_of_ints(intlist): ...
def make_str(x): ...
def generate_unique_node(): ...
def default_opener(filename: str): ...
def dict_to_numpy_array(d, mapping=None): ...
def dict_to_numpy_array2(d, mapping=None): ...
def dict_to_numpy_array1(d, mapping=None): ...
def is_iterator(obj): ...
def arbitrary_element(iterable): ...

# Recipe from the itertools documentation.
def consume(iterator): ...

# Recipe from the itertools documentation.
def pairwise(iterable, cyclic=False): ...
def groups(many_to_one): ...
def to_tuple(x): ...
def create_random_state(random_state=None): ...

class PythonRandomInterface:
    def __init__(self, rng=None): ...
    def random(self): ...
    def uniform(self, a, b): ...
    def randrange(self, a, b=None): ...

    # NOTE: the numpy implementations of `choice` don't support strings, so
    # this cannot be replaced with self._rng.choice
    def choice(self, seq): ...
    def gauss(self, mu, sigma): ...
    def shuffle(self, seq): ...

    #    Some methods don't match API for numpy RandomState.
    #    Commented out versions are not used by NetworkX

    def sample(self, seq, k): ...
    def randint(self, a, b): ...

    #    exponential as expovariate with 1/argument,
    def expovariate(self, scale): ...

    #    pareto as paretovariate with 1/argument,
    def paretovariate(self, shape): ...

#    weibull as weibullvariate multiplied by beta,
#    def weibullvariate(self, alpha, beta):
#        return self._rng.weibull(alpha) * beta
#
#    def triangular(self, low, high, mode):
#        return self._rng.triangular(low, mode, high)
#
#    def choices(self, seq, weights=None, cum_weights=None, k=1):
#        return self._rng.choice(seq

def create_py_random_state(random_state=None): ...
def nodes_equal(nodes1, nodes2) -> bool: ...
def edges_equal(edges1, edges2) -> bool: ...
def graphs_equal(graph1, graph2) -> bool: ...
