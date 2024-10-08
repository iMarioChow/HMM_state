"""
This type stub file was generated by pyright.
"""

""" Import Qt in a manner suitable for an IPython kernel.

This is the import used for the `gui=qt` or `matplotlib=qt` initialization.

Import Priority:

if Qt has been imported anywhere else:
   use that

if matplotlib has been imported and doesn't support v2 (<= 1.0.1):
    use PyQt4 @v1

Next, ask QT_API env variable

if QT_API not set:
    ask matplotlib what it's using. If Qt4Agg or Qt5Agg, then use the
        version matplotlib is configured with

    else: (matplotlib said nothing)
        # this is the default path - nobody told us anything
        try in this order:
            PyQt default version, PySide, PyQt5
else:
    use what QT_API says

    Note that %gui's implementation will always set a `QT_API`, see
    `IPython.terminal.pt_inputhooks.get_inputhook_name_and_func`

"""
_qt_apis = ...
def matplotlib_options(mpl): # -> None:
    """Constraints placed on an imported matplotlib."""
    ...

def get_options():
    """Return a list of acceptable QT APIs, in decreasing order of preference."""
    ...

api_opts = ...
enum_helper = ...
