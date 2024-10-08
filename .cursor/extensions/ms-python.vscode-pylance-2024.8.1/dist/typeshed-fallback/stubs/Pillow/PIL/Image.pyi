from _typeshed import Incomplete, SupportsRead, SupportsWrite, Unused
from collections.abc import Callable, Iterable, Iterator, MutableMapping, Sequence
from enum import IntEnum
from pathlib import Path
from typing import Any, ClassVar, Final, Literal, Protocol, SupportsBytes
from typing_extensions import Self, TypeAlias, TypeGuard

from PIL.PyAccess import PyAccess

from ._imaging import (
    DEFAULT_STRATEGY as DEFAULT_STRATEGY,
    FILTERED as FILTERED,
    FIXED as FIXED,
    HUFFMAN_ONLY as HUFFMAN_ONLY,
    RLE as RLE,
    _PixelAccessor,
)
from .ImageFilter import Filter
from .ImagePalette import ImagePalette

_Mode: TypeAlias = str
_Resample: TypeAlias = Literal[0, 1, 2, 3, 4, 5]
_Size: TypeAlias = tuple[int, int]
_Box: TypeAlias = tuple[int, int, int, int]

_ConversionMatrix: TypeAlias = (
    tuple[float, float, float, float] | tuple[float, float, float, float, float, float, float, float, float, float, float, float]
)
# `str` values are only accepted if mode="RGB" for an `Image` object
# `float` values are only accepted for certain modes such as "F"
# See https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
_Color: TypeAlias = (
    int | tuple[int] | tuple[int, int] | tuple[int, int, int] | tuple[int, int, int, int] | str | float | tuple[float]
)

class _Writeable(SupportsWrite[bytes], Protocol):
    def seek(self, offset: int, /) -> Any: ...

# Ref: https://numpy.org/doc/stable/reference/arrays.interface.html#python-side
class _SupportsArrayInterface(Protocol):
    @property
    def __array_interface__(self) -> dict[str, Any]: ...

class DecompressionBombWarning(RuntimeWarning): ...
class DecompressionBombError(Exception): ...

# Despite the ALL_CAPS spelling, Pillow's docs mention that this threshold can
# be altered at runtime. See
#     https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
# or the permalink
#     https://github.com/python-pillow/Pillow/blob/10.0.0/docs/reference/Image.rst?plain=1#L54-L55
MAX_IMAGE_PIXELS: int | None

USE_CFFI_ACCESS: bool

def isImageType(t: object) -> TypeGuard[Image]: ...

class Transpose(IntEnum):
    FLIP_LEFT_RIGHT = 0
    FLIP_TOP_BOTTOM = 1
    ROTATE_90 = 2
    ROTATE_180 = 3
    ROTATE_270 = 4
    TRANSPOSE = 5
    TRANSVERSE = 6

# All Transpose items
FLIP_LEFT_RIGHT: Final = 0
FLIP_TOP_BOTTOM: Final = 1
ROTATE_90: Final = 2
ROTATE_180: Final = 3
ROTATE_270: Final = 4
TRANSPOSE: Final = 5
TRANSVERSE: Final = 6

class Transform(IntEnum):
    AFFINE = 0
    EXTENT = 1
    PERSPECTIVE = 2
    QUAD = 3
    MESH = 4

# All Transform items
AFFINE: Final = 0
EXTENT: Final = 1
PERSPECTIVE: Final = 2
QUAD: Final = 3
MESH: Final = 4

class Resampling(IntEnum):
    NEAREST = 0
    LANCZOS = 1
    BILINEAR = 2
    BICUBIC = 3
    BOX = 4
    HAMMING = 5

# All Resampling items
NEAREST: Final = 0
LANCZOS: Final = 1
BILINEAR: Final = 2
BICUBIC: Final = 3
BOX: Final = 4
HAMMING: Final = 5

class Dither(IntEnum):
    NONE = 0
    ORDERED = 1
    RASTERIZE = 2
    FLOYDSTEINBERG = 3

# All Dither items
NONE: Final = 0
ORDERED: Final = 1
RASTERIZE: Final = 2
FLOYDSTEINBERG: Final = 3

class Palette(IntEnum):
    WEB = 0
    ADAPTIVE = 1

# All Palette items
WEB: Final = 0
ADAPTIVE: Final = 1

class Quantize(IntEnum):
    MEDIANCUT = 0
    MAXCOVERAGE = 1
    FASTOCTREE = 2
    LIBIMAGEQUANT = 3

# All Quantize items
MEDIANCUT: Final = 0
MAXCOVERAGE: Final = 1
FASTOCTREE: Final = 2
LIBIMAGEQUANT: Final = 3

ID: list[str]
OPEN: dict[str, Any]
MIME: dict[str, str]
SAVE: dict[str, Any]
SAVE_ALL: dict[str, Any]
EXTENSION: dict[str, str]
DECODERS: dict[str, Any]
ENCODERS: dict[str, Any]

MODES: list[_Mode]

def getmodebase(mode: _Mode) -> Literal["L", "RGB"]: ...
def getmodetype(mode: _Mode) -> Literal["L", "I", "F"]: ...
def getmodebandnames(mode: _Mode) -> tuple[str, ...]: ...
def getmodebands(mode: _Mode) -> int: ...
def preinit() -> None: ...
def init() -> None: ...

class _E:
    scale: Incomplete
    offset: Incomplete
    def __init__(self, scale, offset) -> None: ...
    def __neg__(self) -> _E: ...
    def __add__(self, other) -> _E: ...
    __radd__ = __add__
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other) -> _E: ...
    __rmul__ = __mul__
    def __truediv__(self, other) -> _E: ...

_ImageState: TypeAlias = tuple[dict[str, Any], str, tuple[int, int], Any, bytes]

class Image:
    format: ClassVar[str | None]
    format_description: ClassVar[str | None]
    im: Incomplete
    palette: Incomplete
    info: dict[Incomplete, Incomplete]
    readonly: int
    pyaccess: PyAccess | None
    is_animated: bool  # not present on all Image objects
    n_frames: int  # not present on all Image objects
    # Only defined after a call to save().
    encoderconfig: tuple[Incomplete, ...]
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def size(self) -> tuple[int, int]: ...
    @property
    def mode(self) -> _Mode: ...
    def __enter__(self) -> Self: ...
    def __exit__(self, *args: Unused) -> None: ...
    def close(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    @property
    def __array_interface__(self): ...
    def __getstate__(self) -> _ImageState: ...
    def __setstate__(self, state: _ImageState) -> None: ...
    def tobytes(self, encoder_name: str = "raw", *args) -> bytes: ...
    def tobitmap(self, name: str = "image") -> bytes: ...
    def frombytes(self, data: bytes, decoder_name: str = "raw", *args) -> None: ...
    def load(self) -> _PixelAccessor: ...
    def verify(self) -> None: ...
    def convert(
        self,
        mode: _Mode | None = None,
        matrix: _ConversionMatrix | None = None,
        dither: int | None = None,
        palette: Palette | Literal[0, 1] = ...,
        colors: int = 256,
    ) -> Image: ...
    def quantize(
        self,
        colors: int = 256,
        method: Quantize | Literal[0, 1, 2, 3] | None = None,
        kmeans: int = 0,
        palette: Image | None = None,
        dither: int = ...,
    ) -> Image: ...
    def copy(self) -> Image: ...
    __copy__ = copy
    def crop(self, box: _Box | None = None) -> Image: ...
    def draft(self, mode: _Mode, size: _Size) -> None: ...
    def filter(self, filter: Filter | Callable[[], Filter]) -> Image: ...
    def getbands(self) -> tuple[str, ...]: ...
    def getbbox(self, *, alpha_only: bool = True) -> tuple[int, int, int, int] | None: ...
    def getcolors(self, maxcolors: int = 256) -> list[tuple[int, int]]: ...
    def getdata(self, band: int | None = None): ...
    def getextrema(self): ...
    def getexif(self) -> Exif: ...
    def get_child_images(self) -> list[Image]: ...
    def getim(self): ...
    def getpalette(self, rawmode: str | None = "RGB") -> list[int] | None: ...
    @property
    def has_transparency_data(self) -> bool: ...
    def apply_transparency(self) -> None: ...
    def getpixel(self, xy: tuple[int, int]): ...
    def getprojection(self) -> tuple[list[int], list[int]]: ...
    def histogram(self, mask: Image | None = None, extrema: tuple[int, int] | tuple[float, float] | None = None) -> list[int]: ...
    def entropy(self, mask: Image | None = None, extrema: tuple[int, int] | tuple[float, float] | None = None) -> float: ...
    def paste(self, im: Image | _Color, box: tuple[int, int] | _Box | None = None, mask: Image | None = None) -> None: ...
    def alpha_composite(self, im: Image, dest: tuple[int, int] = (0, 0), source: tuple[int, int] = (0, 0)) -> None: ...
    def point(self, lut, mode: _Mode | None = None) -> Image: ...
    def putalpha(self, alpha: Image | int) -> None: ...
    def putdata(self, data: Sequence[int], scale: float = 1.0, offset: float = 0.0) -> None: ...
    def putpalette(self, data: ImagePalette | bytes | Iterable[int] | SupportsBytes, rawmode: _Mode | None = "RGB") -> None: ...
    def putpixel(self, xy: tuple[int, int], value: _Color | list[float]) -> None: ...
    def remap_palette(self, dest_map: Iterable[int], source_palette: Sequence[int] | None = None) -> Image: ...
    def resize(
        self,
        size: tuple[int, int],
        resample: Resampling | _Resample | None = None,
        box: tuple[float, float, float, float] | None = None,
        reducing_gap: float | None = None,
    ) -> Image: ...
    def reduce(self, factor: int | tuple[int, int] | list[int], box: _Box | None = None) -> Image: ...
    def rotate(
        self,
        angle: float,
        resample: Resampling | _Resample = ...,
        expand: bool = ...,
        center: tuple[float, float] | None = None,
        translate: tuple[float, float] | None = None,
        fillcolor: _Color | None = None,
    ) -> Image: ...
    def save(
        self,
        fp: str | bytes | Path | _Writeable,
        format: str | None = None,
        *,
        save_all: bool = ...,
        bitmap_format: Literal["bmp", "png"] = ...,  # for ICO files
        optimize: bool = ...,
        **params: Any,
    ) -> None: ...
    def seek(self, frame: int) -> None: ...
    def show(self, title: str | None = None) -> None: ...
    def split(self) -> tuple[Image, ...]: ...
    def getchannel(self, channel: int | str) -> Image: ...
    def tell(self) -> int: ...
    def thumbnail(self, size: tuple[int, int], resample: Resampling | _Resample = ..., reducing_gap: float = 2.0) -> None: ...
    def transform(
        self,
        size: _Size,
        method: Transform | Literal[0, 1, 2, 3, 4],
        data=None,
        resample: Resampling | _Resample = ...,
        fill: int = 1,
        fillcolor: _Color | int | None = None,
    ) -> Image: ...
    def transpose(self, method: Transpose | Literal[0, 1, 2, 3, 4, 5, 6]) -> Image: ...
    def effect_spread(self, distance: int) -> Image: ...
    def toqimage(self): ...
    def toqpixmap(self): ...

class ImagePointHandler: ...
class ImageTransformHandler: ...

def new(mode: _Mode, size: tuple[int, int], color: _Color = 0) -> Image: ...
def frombytes(mode: _Mode, size: tuple[int, int], data, decoder_name: str = "raw", *args) -> Image: ...
def frombuffer(mode: _Mode, size: tuple[int, int], data, decoder_name: str = "raw", *args) -> Image: ...

# If the __array_interface__ has "strides", then `obj` must also support `tobytes` or `tostring`, but we can't enforce that
def fromarray(obj: _SupportsArrayInterface, mode: _Mode | None = None) -> Image: ...
def fromqimage(im) -> Image: ...
def fromqpixmap(im) -> Image: ...
def open(
    fp: str | bytes | Path | SupportsRead[bytes], mode: Literal["r"] = "r", formats: list[str] | tuple[str, ...] | None = None
) -> Image: ...
def alpha_composite(im1: Image, im2: Image) -> Image: ...
def blend(im1: Image, im2: Image, alpha: float) -> Image: ...
def composite(image1: Image, image2: Image, mask: Image) -> Image: ...
def eval(image: Image, *args) -> Image: ...
def merge(mode: _Mode, bands: Sequence[Image]) -> Image: ...
def register_open(id: str, factory, accept=None) -> None: ...
def register_mime(id: str, mimetype: str) -> None: ...
def register_save(id: str, driver) -> None: ...
def register_save_all(id: str, driver) -> None: ...
def register_extension(id: str, extension: str) -> None: ...
def register_extensions(id: str, extensions: Iterable[str]) -> None: ...
def registered_extensions() -> dict[str, str]: ...
def register_decoder(name: str, decoder) -> None: ...
def register_encoder(name: str, encoder) -> None: ...
def effect_mandelbrot(size: tuple[int, int], extent: tuple[float, float, float, float], quality: int) -> Image: ...
def effect_noise(size: tuple[int, int], sigma: float) -> Image: ...
def linear_gradient(mode: _Mode) -> Image: ...
def radial_gradient(mode: _Mode) -> Image: ...

class Exif(MutableMapping[int, Any]):
    endian: Incomplete
    bigtiff: bool
    def load(self, data: bytes) -> None: ...
    def load_from_fp(self, fp, offset: Incomplete | None = None) -> None: ...
    def tobytes(self, offset: int = 8) -> bytes: ...
    def get_ifd(self, tag: int): ...
    def hide_offsets(self) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, tag: int) -> Any: ...
    def __contains__(self, tag: object) -> bool: ...
    def __setitem__(self, tag: int, value: Any) -> None: ...
    def __delitem__(self, tag: int) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
