from networkx.utils.backends import _dispatch

@_dispatch
def communicability(G): ...
@_dispatch
def communicability_exp(G): ...
