"""
This type stub file was generated by pyright.
"""

import enum
import sys
from contextlib import contextmanager
from dataclasses import dataclass
from functools import cached_property
from typing import Dict, Iterable, Iterator, List, Literal, Optional, Sequence, Set, TYPE_CHECKING, Tuple, TypeVar, TypedDict, Union
from IPython.testing.skipdoctest import skip_doctest
from IPython.utils.decorators import sphinx_options
from IPython.utils.docs import GENERATING_DOCUMENTATION
from traitlets.config.configurable import Configurable
from typing_extensions import NotRequired, Protocol, TypeAlias, TypedDict

"""Completion for IPython.

This module started as fork of the rlcompleter module in the Python standard
library.  The original enhancements made to rlcompleter have been sent
upstream and were accepted as of Python 2.3,

This module now support a wide variety of completion mechanism both available
for normal classic Python code, as well as completer for IPython specific
Syntax like magics.

Latex and Unicode completion
============================

IPython and compatible frontends not only can complete your code, but can help
you to input a wide range of characters. In particular we allow you to insert
a unicode character using the tab completion mechanism.

Forward latex/unicode completion
--------------------------------

Forward completion allows you to easily type a unicode character using its latex
name, or unicode long description. To do so type a backslash follow by the
relevant name and press tab:


Using latex completion:

.. code::

    \\alpha<tab>
    α

or using unicode completion:


.. code::

    \\GREEK SMALL LETTER ALPHA<tab>
    α


Only valid Python identifiers will complete. Combining characters (like arrow or
dots) are also available, unlike latex they need to be put after the their
counterpart that is to say, ``F\\\\vec<tab>`` is correct, not ``\\\\vec<tab>F``.

Some browsers are known to display combining characters incorrectly.

Backward latex completion
-------------------------

It is sometime challenging to know how to type a character, if you are using
IPython, or any compatible frontend you can prepend backslash to the character
and press :kbd:`Tab` to expand it to its latex form.

.. code::

    \\α<tab>
    \\alpha


Both forward and backward completions can be deactivated by setting the
:std:configtrait:`Completer.backslash_combining_completions` option to
``False``.


Experimental
============

Starting with IPython 6.0, this module can make use of the Jedi library to
generate completions both using static analysis of the code, and dynamically
inspecting multiple namespaces. Jedi is an autocompletion and static analysis
for Python. The APIs attached to this new mechanism is unstable and will
raise unless use in an :any:`provisionalcompleter` context manager.

You will find that the following are experimental:

    - :any:`provisionalcompleter`
    - :any:`IPCompleter.completions`
    - :any:`Completion`
    - :any:`rectify_completions`

.. note::

    better name for :any:`rectify_completions` ?

We welcome any feedback on these new API, and we also encourage you to try this
module in debug mode (start IPython with ``--Completer.debug=True``) in order
to have extra logging information if :any:`jedi` is crashing, or if current
IPython completer pending deprecations are returning results not yet handled
by :any:`jedi`

Using Jedi for tab completion allow snippets like the following to work without
having to execute any code:

   >>> myvar = ['hello', 42]
   ... myvar[1].bi<tab>

Tab completion will be able to infer that ``myvar[1]`` is a real number without
executing almost any code unlike the deprecated :any:`IPCompleter.greedy`
option.

Be sure to update :any:`jedi` to the latest stable version or to try the
current development version to get better completions.

Matchers
========

All completions routines are implemented using unified *Matchers* API.
The matchers API is provisional and subject to change without notice.

The built-in matchers include:

- :any:`IPCompleter.dict_key_matcher`:  dictionary key completions,
- :any:`IPCompleter.magic_matcher`: completions for magics,
- :any:`IPCompleter.unicode_name_matcher`,
  :any:`IPCompleter.fwd_unicode_matcher`
  and :any:`IPCompleter.latex_name_matcher`: see `Forward latex/unicode completion`_,
- :any:`back_unicode_name_matcher` and :any:`back_latex_name_matcher`: see `Backward latex completion`_,
- :any:`IPCompleter.file_matcher`: paths to files and directories,
- :any:`IPCompleter.python_func_kw_matcher` - function keywords,
- :any:`IPCompleter.python_matches` - globals and attributes (v1 API),
- ``IPCompleter.jedi_matcher`` - static analysis with Jedi,
- :any:`IPCompleter.custom_completer_matcher` - pluggable completer with a default
  implementation in :any:`InteractiveShell` which uses IPython hooks system
  (`complete_command`) with string dispatch (including regular expressions).
  Differently to other matchers, ``custom_completer_matcher`` will not suppress
  Jedi results to match behaviour in earlier IPython versions.

Custom matchers can be added by appending to ``IPCompleter.custom_matchers`` list.

Matcher API
-----------

Simplifying some details, the ``Matcher`` interface can described as

.. code-block::

    MatcherAPIv1 = Callable[[str], list[str]]
    MatcherAPIv2 = Callable[[CompletionContext], SimpleMatcherResult]

    Matcher = MatcherAPIv1 | MatcherAPIv2

The ``MatcherAPIv1`` reflects the matcher API as available prior to IPython 8.6.0
and remains supported as a simplest way for generating completions. This is also
currently the only API supported by the IPython hooks system `complete_command`.

To distinguish between matcher versions ``matcher_api_version`` attribute is used.
More precisely, the API allows to omit ``matcher_api_version`` for v1 Matchers,
and requires a literal ``2`` for v2 Matchers.

Once the API stabilises future versions may relax the requirement for specifying
``matcher_api_version`` by switching to :any:`functools.singledispatch`, therefore
please do not rely on the presence of ``matcher_api_version`` for any purposes.

Suppression of competing matchers
---------------------------------

By default results from all matchers are combined, in the order determined by
their priority. Matchers can request to suppress results from subsequent
matchers by setting ``suppress`` to ``True`` in the ``MatcherResult``.

When multiple matchers simultaneously request surpression, the results from of
the matcher with higher priority will be returned.

Sometimes it is desirable to suppress most but not all other matchers;
this can be achieved by adding a set of identifiers of matchers which
should not be suppressed to ``MatcherResult`` under ``do_not_suppress`` key.

The suppression behaviour can is user-configurable via
:std:configtrait:`IPCompleter.suppress_competing_matchers`.
"""
__skip_doctest__ = ...
JEDI_INSTALLED = ...
if TYPE_CHECKING or GENERATING_DOCUMENTATION and sys.version_info >= (3, 11):
    ...
else:
    ...
if GENERATING_DOCUMENTATION:
    ...
_UNICODE_RANGES = ...
__all__ = ["Completer", "IPCompleter"]
if sys.platform == 'win32':
    PROTECTABLES = ...
else:
    ...
MATCHES_LIMIT = ...
_UNKNOWN_TYPE = ...
not_found = ...
class ProvisionalCompleterWarning(FutureWarning):
    """
    Exception raise by an experimental feature in this module.

    Wrap code in :any:`provisionalcompleter` context manager if you
    are certain you want to use an unstable feature.
    """
    ...


@skip_doctest
@contextmanager
def provisionalcompleter(action=...):
    """
    This context manager has to be used in any place where unstable completer
    behavior and API may be called.

    >>> with provisionalcompleter():
    ...     completer.do_experimental_things() # works

    >>> completer.do_experimental_things() # raises.

    .. note::

        Unstable

        By using this context manager you agree that the API in use may change
        without warning, and that you won't complain if they do so.

        You also understand that, if the API is not to your liking, you should report
        a bug to explain your use case upstream.

        We'll be happy to get your feedback, feature requests, and improvements on
        any of the unstable APIs!
    """
    ...

def has_open_quotes(s):
    """Return whether a string has open quotes.

    This simply counts whether the number of quote characters of either type in
    the string is odd.

    Returns
    -------
    If there is an open quote, the quote character is returned.  Else, return
    False.
    """
    ...

def protect_filename(s, protectables=...):
    """Escape a string to protect certain characters."""
    ...

def expand_user(path: str) -> Tuple[str, bool, str]:
    """Expand ``~``-style usernames in strings.

    This is similar to :func:`os.path.expanduser`, but it computes and returns
    extra information that will be useful if the input was being used in
    computing completions, and you wish to return the completions with the
    original '~' instead of its expanded value.

    Parameters
    ----------
    path : str
        String to be expanded.  If no ~ is present, the output is the same as the
        input.

    Returns
    -------
    newpath : str
        Result of ~ expansion in the input path.
    tilde_expand : bool
        Whether any expansion was performed or not.
    tilde_val : str
        The value that ~ was replaced with.
    """
    ...

def compress_user(path: str, tilde_expand: bool, tilde_val: str) -> str:
    """Does the opposite of expand_user, with its outputs.
    """
    ...

def completions_sorting_key(word):
    """key for sorting completions

    This does several things:

    - Demote any completions starting with underscores to the end
    - Insert any %magic and %%cellmagic completions in the alphabetical order
      by their name
    """
    ...

class _FakeJediCompletion:
    """
    This is a workaround to communicate to the UI that Jedi has crashed and to
    report a bug. Will be used only id :any:`IPCompleter.debug` is set to true.

    Added in IPython 6.0 so should likely be removed for 7.0

    """
    def __init__(self, name) -> None:
        ...
    
    def __repr__(self):
        ...
    


_JediCompletionLike = ...
class Completion:
    """
    Completion object used and returned by IPython completers.

    .. warning::

        Unstable

        This function is unstable, API may change without warning.
        It will also raise unless use in proper context manager.

    This act as a middle ground :any:`Completion` object between the
    :any:`jedi.api.classes.Completion` object and the Prompt Toolkit completion
    object. While Jedi need a lot of information about evaluator and how the
    code should be ran/inspected, PromptToolkit (and other frontend) mostly
    need user facing information.

    - Which range should be replaced replaced by what.
    - Some metadata (like completion type), or meta information to displayed to
      the use user.

    For debugging purpose we can also store the origin of the completion (``jedi``,
    ``IPython.python_matches``, ``IPython.magics_matches``...).
    """
    __slots__ = ...
    def __init__(self, start: int, end: int, text: str, *, type: Optional[str] = ..., _origin=..., signature=...) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def __eq__(self, other) -> bool:
        """
        Equality and hash do not hash the type (as some completer may not be
        able to infer the type), but are use to (partially) de-duplicate
        completion.

        Completely de-duplicating completion is a bit tricker that just
        comparing as it depends on surrounding text, which Completions are not
        aware of.
        """
        ...
    
    def __hash__(self) -> int:
        ...
    


class SimpleCompletion:
    """Completion item to be included in the dictionary returned by new-style Matcher (API v2).

    .. warning::

        Provisional

        This class is used to describe the currently supported attributes of
        simple completion items, and any additional implementation details
        should not be relied on. Additional attributes may be included in
        future versions, and meaning of text disambiguated from the current
        dual meaning of "text to insert" and "text to used as a label".
    """
    __slots__ = ...
    def __init__(self, text: str, *, type: Optional[str] = ...) -> None:
        ...
    
    def __repr__(self):
        ...
    


class _MatcherResultBase(TypedDict):
    """Definition of dictionary to be returned by new-style Matcher (API v2)."""
    matched_fragment: NotRequired[str]
    suppress: NotRequired[Union[bool, Set[str]]]
    do_not_suppress: NotRequired[Set[str]]
    ordered: NotRequired[bool]
    ...


@sphinx_options(show_inherited_members=True, exclude_inherited_from=["dict"])
class SimpleMatcherResult(_MatcherResultBase, TypedDict):
    """Result of new-style completion matcher."""
    completions: Sequence[SimpleCompletion] | Iterator[SimpleCompletion]
    ...


class _JediMatcherResult(_MatcherResultBase):
    """Matching result returned by Jedi (will be processed differently)"""
    completions: Iterator[_JediCompletionLike]
    ...


AnyMatcherCompletion = ...
AnyCompletion = TypeVar("AnyCompletion", AnyMatcherCompletion, Completion)
@dataclass
class CompletionContext:
    """Completion context provided as an argument to matchers in the Matcher API v2."""
    token: str
    full_text: str
    cursor_position: int
    cursor_line: int
    limit: Optional[int]
    @cached_property
    def text_until_cursor(self) -> str:
        ...
    
    @cached_property
    def line_with_cursor(self) -> str:
        ...
    


MatcherResult = ...
class _MatcherAPIv1Base(Protocol):
    def __call__(self, text: str) -> List[str]:
        """Call signature."""
        ...
    
    __qualname__: str


class _MatcherAPIv1Total(_MatcherAPIv1Base, Protocol):
    matcher_api_version: Optional[Literal[1]]
    def __call__(self, text: str) -> List[str]:
        """Call signature."""
        ...
    


MatcherAPIv1: TypeAlias = ...
class MatcherAPIv2(Protocol):
    """Protocol describing Matcher API v2."""
    matcher_api_version: Literal[2] = ...
    def __call__(self, context: CompletionContext) -> MatcherResult:
        """Call signature."""
        ...
    
    __qualname__: str


Matcher: TypeAlias = ...
def has_any_completions(result: MatcherResult) -> bool:
    """Check if any result includes any completions."""
    ...

def completion_matcher(*, priority: Optional[float] = ..., identifier: Optional[str] = ..., api_version: int = ...): # -> (func: Unknown) -> Unknown:
    """Adds attributes describing the matcher.

    Parameters
    ----------
    priority : Optional[float]
        The priority of the matcher, determines the order of execution of matchers.
        Higher priority means that the matcher will be executed first. Defaults to 0.
    identifier : Optional[str]
        identifier of the matcher allowing users to modify the behaviour via traitlets,
        and also used to for debugging (will be passed as ``origin`` with the completions).

        Defaults to matcher function's ``__qualname__`` (for example,
        ``IPCompleter.file_matcher`` for the built-in matched defined
        as a ``file_matcher`` method of the ``IPCompleter`` class).
    api_version: Optional[int]
        version of the Matcher API used by this matcher.
        Currently supported values are 1 and 2.
        Defaults to 1.
    """
    ...

context_matcher = ...
_IC = ...
def rectify_completions(text: str, completions: _IC, *, _debug: bool = ...) -> _IC:
    """
    Rectify a set of completions to all have the same ``start`` and ``end``

    .. warning::

        Unstable

        This function is unstable, API may change without warning.
        It will also raise unless use in proper context manager.

    Parameters
    ----------
    text : str
        text that should be completed.
    completions : Iterator[Completion]
        iterator over the completions to rectify
    _debug : bool
        Log failed completion

    Notes
    -----
    :any:`jedi.api.classes.Completion` s returned by Jedi may not have the same start and end, though
    the Jupyter Protocol requires them to behave like so. This will readjust
    the completion to have the same ``start`` and ``end`` by padding both
    extremities with surrounding text.

    During stabilisation should support a ``_debug`` option to log which
    completion are return by the IPython completer and not found in Jedi in
    order to make upstream bug report.
    """
    ...

if sys.platform == 'win32':
    DELIMS = ...
else:
    ...
GREEDY_DELIMS = ...
class CompletionSplitter:
    """An object to split an input line in a manner similar to readline.

    By having our own implementation, we can expose readline-like completion in
    a uniform manner to all frontends.  This object only needs to be given the
    line of text to be split and the cursor position on said line, and it
    returns the 'word' to be completed on at the cursor after splitting the
    entire line.

    What characters are used as splitting delimiters can be controlled by
    setting the ``delims`` attribute (this is a property that internally
    automatically builds the necessary regular expression)"""
    _delims = ...
    _delim_expr = ...
    _delim_re = ...
    def __init__(self, delims=...) -> None:
        ...
    
    @property
    def delims(self):
        """Return the string of delimiter characters."""
        ...
    
    @delims.setter
    def delims(self, delims): # -> None:
        """Set the delimiters for line splitting."""
        ...
    
    def split_line(self, line, cursor_pos=...):
        """Split a line of text with a cursor at the given position.
        """
        ...
    


class Completer(Configurable):
    greedy = ...
    evaluation = ...
    use_jedi = ...
    jedi_compute_type_timeout = ...
    debug = ...
    backslash_combining_completions = ...
    auto_close_dict_keys = ...
    def __init__(self, namespace=..., global_namespace=..., **kwargs) -> None:
        """Create a new completer for the command line.

        Completer(namespace=ns, global_namespace=ns2) -> completer instance.

        If unspecified, the default namespace where completions are performed
        is __main__ (technically, __main__.__dict__). Namespaces should be
        given as dictionaries.

        An optional second namespace can be given.  This allows the completer
        to handle cases where both the local and global scopes need to be
        distinguished.
        """
        ...
    
    def complete(self, text, state): # -> None:
        """Return the next possible completion for 'text'.

        This is called successively with state == 0, 1, 2, ... until it
        returns None.  The completion should begin with 'text'.

        """
        ...
    
    def global_matches(self, text):
        """Compute matches when text is a simple name.

        Return a list of all keywords, built-in functions and names currently
        defined in self.namespace or self.global_namespace that match.

        """
        ...
    
    def attr_matches(self, text):
        """Compute matches when text contains a dot.

        Assuming the text is of the form NAME.NAME....[NAME], and is
        evaluatable in self.namespace or self.global_namespace, it will be
        evaluated and its attributes (as revealed by dir()) are used as
        possible completions.  (For class instances, class members are
        also considered.)

        WARNING: this can still invoke arbitrary C code, if an object
        with a __getattr__ hook is evaluated.

        """
        ...
    


def get__all__entries(obj):
    """returns the strings in the __all__ attribute"""
    ...

class _DictKeyState(enum.Flag):
    """Represent state of the key match in context of other possible matches.

    - given `d1 = {'a': 1}` completion on `d1['<tab>` will yield `{'a': END_OF_ITEM}` as there is no tuple.
    - given `d2 = {('a', 'b'): 1}`: `d2['a', '<tab>` will yield `{'b': END_OF_TUPLE}` as there is no tuple members to add beyond `'b'`.
    - given `d3 = {('a', 'b'): 1}`: `d3['<tab>` will yield `{'a': IN_TUPLE}` as `'a'` can be added.
    - given `d4 = {'a': 1, ('a', 'b'): 2}`: `d4['<tab>` will yield `{'a': END_OF_ITEM & END_OF_TUPLE}`
    """
    BASELINE = ...
    END_OF_ITEM = ...
    END_OF_TUPLE = ...
    IN_TUPLE = ...


_INT_FORMATS = ...
def match_dict_keys(keys: List[Union[str, bytes, Tuple[Union[str, bytes], ...]]], prefix: str, delims: str, extra_prefix: Optional[Tuple[Union[str, bytes], ...]] = ...) -> Tuple[str, int, Dict[str, _DictKeyState]]:
    """Used by dict_key_matches, matching the prefix to a list of keys

    Parameters
    ----------
    keys
        list of keys in dictionary currently being completed.
    prefix
        Part of the text already typed by the user. E.g. `mydict[b'fo`
    delims
        String of delimiters to consider when finding the current key.
    extra_prefix : optional
        Part of the text already typed in multi-key index cases. E.g. for
        `mydict['foo', "bar", 'b`, this would be `('foo', 'bar')`.

    Returns
    -------
    A tuple of three elements: ``quote``, ``token_start``, ``matched``, with
    ``quote`` being the quote that need to be used to close current string.
    ``token_start`` the position where the replacement should start occurring,
    ``matches`` a dictionary of replacement/completion keys on keys and values
        indicating whether the state.
    """
    ...

def cursor_to_position(text: str, line: int, column: int) -> int:
    """
    Convert the (line,column) position of the cursor in text to an offset in a
    string.

    Parameters
    ----------
    text : str
        The text in which to calculate the cursor offset
    line : int
        Line of the cursor; 0-indexed
    column : int
        Column of the cursor 0-indexed

    Returns
    -------
    Position of the cursor in ``text``, 0-indexed.

    See Also
    --------
    position_to_cursor : reciprocal of this function

    """
    ...

def position_to_cursor(text: str, offset: int) -> Tuple[int, int]:
    """
    Convert the position of the cursor in text (0 indexed) to a line
    number(0-indexed) and a column number (0-indexed) pair

    Position should be a valid position in ``text``.

    Parameters
    ----------
    text : str
        The text in which to calculate the cursor offset
    offset : int
        Position of the cursor in ``text``, 0-indexed.

    Returns
    -------
    (line, column) : (int, int)
        Line of the cursor; 0-indexed, column of the cursor 0-indexed

    See Also
    --------
    cursor_to_position : reciprocal of this function

    """
    ...

@context_matcher()
def back_unicode_name_matcher(context: CompletionContext): # -> SimpleMatcherResult:
    """Match Unicode characters back to Unicode name

    Same as :any:`back_unicode_name_matches`, but adopted to new Matcher API.
    """
    ...

def back_unicode_name_matches(text: str) -> Tuple[str, Sequence[str]]:
    """Match Unicode characters back to Unicode name

    This does  ``☃`` -> ``\\snowman``

    Note that snowman is not a valid python3 combining character but will be expanded.
    Though it will not recombine back to the snowman character by the completion machinery.

    This will not either back-complete standard sequences like \\n, \\b ...

    .. deprecated:: 8.6
        You can use :meth:`back_unicode_name_matcher` instead.

    Returns
    =======

    Return a tuple with two elements:

    - The Unicode character that was matched (preceded with a backslash), or
        empty string,
    - a sequence (of 1), name for the match Unicode character, preceded by
        backslash, or empty if no match.
    """
    ...

@context_matcher()
def back_latex_name_matcher(context: CompletionContext): # -> SimpleMatcherResult:
    """Match latex characters back to unicode name

    Same as :any:`back_latex_name_matches`, but adopted to new Matcher API.
    """
    ...

def back_latex_name_matches(text: str) -> Tuple[str, Sequence[str]]:
    """Match latex characters back to unicode name

    This does ``\\ℵ`` -> ``\\aleph``

    .. deprecated:: 8.6
        You can use :meth:`back_latex_name_matcher` instead.
    """
    ...

_CompleteResult = ...
DICT_MATCHER_REGEX = ...
class IPCompleter(Completer):
    """Extension of the completer class with IPython-specific features"""
    dict_keys_only = ...
    suppress_competing_matchers = ...
    merge_completions = ...
    disable_matchers = ...
    omit__names = ...
    limit_to__all__ = ...
    profile_completions = ...
    profiler_output_dir = ...
    def __init__(self, shell=..., namespace=..., global_namespace=..., config=..., **kwargs) -> None:
        """IPCompleter() -> completer

        Return a completer object.

        Parameters
        ----------
        shell
            a pointer to the ipython shell itself.  This is needed
            because this completer knows about magic functions, and those can
            only be accessed via the ipython instance.
        namespace : dict, optional
            an optional dict where completions are performed.
        global_namespace : dict, optional
            secondary optional dict for completions, to
            handle cases (such as IPython embedded inside functions) where
            both Python scopes are visible.
        config : Config
            traitlet's config object
        **kwargs
            passed to super class unmodified.
        """
        ...
    
    @property
    def matchers(self) -> List[Matcher]:
        """All active matcher routines for completion"""
        ...
    
    def all_completions(self, text: str) -> List[str]:
        """
        Wrapper around the completion methods for the benefit of emacs.
        """
        ...
    
    @context_matcher()
    def file_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Same as :any:`file_matches`, but adopted to new Matcher API."""
        ...
    
    def file_matches(self, text: str) -> List[str]:
        """Match filenames, expanding ~USER type strings.

        Most of the seemingly convoluted logic in this completer is an
        attempt to handle filenames with spaces in them.  And yet it's not
        quite perfect, because Python's readline doesn't expose all of the
        GNU readline details needed for this to be done correctly.

        For a filename with a space in it, the printed completions will be
        only the parts after what's already been typed (instead of the
        full completions, as is normally done).  I don't think with the
        current (as of Python 2.3) Python readline it's possible to do
        better.

        .. deprecated:: 8.6
            You can use :meth:`file_matcher` instead.
        """
        ...
    
    @context_matcher()
    def magic_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match magics."""
        ...
    
    def magic_matches(self, text: str):
        """Match magics.

        .. deprecated:: 8.6
            You can use :meth:`magic_matcher` instead.
        """
        ...
    
    @context_matcher()
    def magic_config_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match class names and attributes for %config magic."""
        ...
    
    def magic_config_matches(self, text: str) -> List[str]:
        """Match class names and attributes for %config magic.

        .. deprecated:: 8.6
            You can use :meth:`magic_config_matcher` instead.
        """
        ...
    
    @context_matcher()
    def magic_color_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match color schemes for %colors magic."""
        ...
    
    def magic_color_matches(self, text: str) -> List[str]:
        """Match color schemes for %colors magic.

        .. deprecated:: 8.6
            You can use :meth:`magic_color_matcher` instead.
        """
        ...
    
    @completion_matcher(api_version=1)
    def python_matches(self, text: str) -> Iterable[str]:
        """Match attributes or global python names"""
        ...
    
    @context_matcher()
    def python_func_kw_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match named parameters (kwargs) of the last open function."""
        ...
    
    def python_func_kw_matches(self, text):
        """Match named parameters (kwargs) of the last open function.

        .. deprecated:: 8.6
            You can use :meth:`python_func_kw_matcher` instead.
        """
        ...
    
    @context_matcher()
    def dict_key_matcher(self, context: CompletionContext) -> SimpleMatcherResult:
        """Match string keys in a dictionary, after e.g. ``foo[``."""
        ...
    
    def dict_key_matches(self, text: str) -> List[str]:
        """Match string keys in a dictionary, after e.g. ``foo[``.

        .. deprecated:: 8.6
            You can use :meth:`dict_key_matcher` instead.
        """
        ...
    
    @context_matcher()
    def unicode_name_matcher(self, context: CompletionContext): # -> SimpleMatcherResult:
        """Same as :any:`unicode_name_matches`, but adopted to new Matcher API."""
        ...
    
    @staticmethod
    def unicode_name_matches(text: str) -> Tuple[str, List[str]]:
        """Match Latex-like syntax for unicode characters base
        on the name of the character.

        This does  ``\\GREEK SMALL LETTER ETA`` -> ``η``

        Works only on valid python 3 identifier, or on combining characters that
        will combine to form a valid identifier.
        """
        ...
    
    @context_matcher()
    def latex_name_matcher(self, context: CompletionContext): # -> SimpleMatcherResult:
        """Match Latex syntax for unicode characters.

        This does both ``\\alp`` -> ``\\alpha`` and ``\\alpha`` -> ``α``
        """
        ...
    
    def latex_matches(self, text: str) -> Tuple[str, Sequence[str]]:
        """Match Latex syntax for unicode characters.

        This does both ``\\alp`` -> ``\\alpha`` and ``\\alpha`` -> ``α``

        .. deprecated:: 8.6
            You can use :meth:`latex_name_matcher` instead.
        """
        ...
    
    @context_matcher()
    def custom_completer_matcher(self, context): # -> SimpleMatcherResult:
        """Dispatch custom completer.

        If a match is found, suppresses all other matchers except for Jedi.
        """
        ...
    
    def dispatch_custom_completer(self, text):
        """
        .. deprecated:: 8.6
            You can use :meth:`custom_completer_matcher` instead.
        """
        ...
    
    def completions(self, text: str, offset: int) -> Iterator[Completion]:
        """
        Returns an iterator over the possible completions

        .. warning::

            Unstable

            This function is unstable, API may change without warning.
            It will also raise unless use in proper context manager.

        Parameters
        ----------
        text : str
            Full text of the current input, multi line string.
        offset : int
            Integer representing the position of the cursor in ``text``. Offset
            is 0-based indexed.

        Yields
        ------
        Completion

        Notes
        -----
        The cursor on a text can either be seen as being "in between"
        characters or "On" a character depending on the interface visible to
        the user. For consistency the cursor being on "in between" characters X
        and Y is equivalent to the cursor being "on" character Y, that is to say
        the character the cursor is on is considered as being after the cursor.

        Combining characters may span more that one position in the
        text.

        .. note::

            If ``IPCompleter.debug`` is :any:`True` will yield a ``--jedi/ipython--``
            fake Completion token to distinguish completion returned by Jedi
            and usual IPython completion.

        .. note::

            Completions are not completely deduplicated yet. If identical
            completions are coming from different sources this function does not
            ensure that each completion object will only be present once.
        """
        ...
    
    def complete(self, text=..., line_buffer=..., cursor_pos=...) -> Tuple[str, Sequence[str]]:
        """Find completions for the given text and line context.

        Note that both the text and the line_buffer are optional, but at least
        one of them must be given.

        Parameters
        ----------
        text : string, optional
            Text to perform the completion on.  If not given, the line buffer
            is split using the instance's CompletionSplitter object.
        line_buffer : string, optional
            If not given, the completer attempts to obtain the current line
            buffer via readline.  This keyword allows clients which are
            requesting for text completions in non-readline contexts to inform
            the completer of the entire text.
        cursor_pos : int, optional
            Index of the cursor in the full line buffer.  Should be provided by
            remote frontends where kernel has no access to frontend state.

        Returns
        -------
        Tuple of two items:
        text : str
            Text that was actually used in the completion.
        matches : list
            A list of completion matches.

        Notes
        -----
            This API is likely to be deprecated and replaced by
            :any:`IPCompleter.completions` in the future.

        """
        ...
    
    @context_matcher()
    def fwd_unicode_matcher(self, context: CompletionContext): # -> SimpleMatcherResult:
        """Same as :any:`fwd_unicode_match`, but adopted to new Matcher API."""
        ...
    
    def fwd_unicode_match(self, text: str) -> Tuple[str, Sequence[str]]:
        """
        Forward match a string starting with a backslash with a list of
        potential Unicode completions.

        Will compute list of Unicode character names on first call and cache it.

        .. deprecated:: 8.6
            You can use :meth:`fwd_unicode_matcher` instead.

        Returns
        -------
        At tuple with:
            - matched text (empty if no matches)
            - list of potential completions, empty tuple  otherwise)
        """
        ...
    
    @property
    def unicode_names(self) -> List[str]:
        """List of names of unicode code points that can be completed.

        The list is lazily initialized on first access.
        """
        ...
    


