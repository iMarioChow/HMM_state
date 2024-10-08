"""
This type stub file was generated by pyright.
"""

from traitlets.config.configurable import Configurable

"""Payload system for IPython.

Authors:

* Fernando Perez
* Brian Granger
"""
class PayloadManager(Configurable):
    _payload = ...
    def write_payload(self, data, single=...): # -> None:
        """Include or update the specified `data` payload in the PayloadManager.

        If a previous payload with the same source exists and `single` is True,
        it will be overwritten with the new one.
        """
        ...
    
    def read_payload(self): # -> List:
        ...
    
    def clear_payload(self): # -> None:
        ...
    


