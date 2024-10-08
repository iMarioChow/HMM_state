from collections.abc import Iterable
from typing import Any, TypeVar
from xml.etree.ElementTree import Element, ElementTree

from markdown import blockprocessors, util
from markdown.core import Markdown

_T = TypeVar("_T")

class State(list[_T]):
    def set(self, state: _T) -> None: ...
    def reset(self) -> None: ...
    def isstate(self, state: _T) -> bool: ...

class BlockParser:
    blockprocessors: util.Registry[blockprocessors.BlockProcessor]
    state: State[Any]  # TODO: possible to get rid of Any?
    md: Markdown
    def __init__(self, md: Markdown) -> None: ...
    root: Element
    def parseDocument(self, lines: Iterable[str]) -> ElementTree: ...
    def parseChunk(self, parent: Element, text: str) -> None: ...
    def parseBlocks(self, parent: Element, blocks: list[str]) -> None: ...
