from enum import IntEnum, IntFlag
from typing import ClassVar, Final, Literal

from .ImageFile import ImageFile, PyDecoder

DDS_MAGIC: Final = 0x20534444

class DDSD(IntFlag):
    CAPS = 0x1
    HEIGHT = 0x2
    WIDTH = 0x4
    PITCH = 0x8
    PIXELFORMAT = 0x1000
    MIPMAPCOUNT = 0x20000
    LINEARSIZE = 0x80000
    DEPTH = 0x800000

class DDSCAPS(IntFlag):
    COMPLEX = 0x8
    TEXTURE = 0x1000
    MIPMAP = 0x400000

class DDSCAPS2(IntFlag):
    CUBEMAP = 0x200
    CUBEMAP_POSITIVEX = 0x400
    CUBEMAP_NEGATIVEX = 0x800
    CUBEMAP_POSITIVEY = 0x1000
    CUBEMAP_NEGATIVEY = 0x2000
    CUBEMAP_POSITIVEZ = 0x4000
    CUBEMAP_NEGATIVEZ = 0x8000
    VOLUME = 0x200000

class DDPF(IntFlag):
    ALPHAPIXELS = 0x1
    ALPHA = 0x2
    FOURCC = 0x4
    PALETTEINDEXED8 = 0x20
    RGB = 0x40
    LUMINANCE = 0x20000

class DXGI_FORMAT(IntEnum):
    UNKNOWN = 0
    R32G32B32A32_TYPELESS = 1
    R32G32B32A32_FLOAT = 2
    R32G32B32A32_UINT = 3
    R32G32B32A32_SINT = 4
    R32G32B32_TYPELESS = 5
    R32G32B32_FLOAT = 6
    R32G32B32_UINT = 7
    R32G32B32_SINT = 8
    R16G16B16A16_TYPELESS = 9
    R16G16B16A16_FLOAT = 10
    R16G16B16A16_UNORM = 11
    R16G16B16A16_UINT = 12
    R16G16B16A16_SNORM = 13
    R16G16B16A16_SINT = 14
    R32G32_TYPELESS = 15
    R32G32_FLOAT = 16
    R32G32_UINT = 17
    R32G32_SINT = 18
    R32G8X24_TYPELESS = 19
    D32_FLOAT_S8X24_UINT = 20
    R32_FLOAT_X8X24_TYPELESS = 21
    X32_TYPELESS_G8X24_UINT = 22
    R10G10B10A2_TYPELESS = 23
    R10G10B10A2_UNORM = 24
    R10G10B10A2_UINT = 25
    R11G11B10_FLOAT = 26
    R8G8B8A8_TYPELESS = 27
    R8G8B8A8_UNORM = 28
    R8G8B8A8_UNORM_SRGB = 29
    R8G8B8A8_UINT = 30
    R8G8B8A8_SNORM = 31
    R8G8B8A8_SINT = 32
    R16G16_TYPELESS = 33
    R16G16_FLOAT = 34
    R16G16_UNORM = 35
    R16G16_UINT = 36
    R16G16_SNORM = 37
    R16G16_SINT = 38
    R32_TYPELESS = 39
    D32_FLOAT = 40
    R32_FLOAT = 41
    R32_UINT = 42
    R32_SINT = 43
    R24G8_TYPELESS = 44
    D24_UNORM_S8_UINT = 45
    R24_UNORM_X8_TYPELESS = 46
    X24_TYPELESS_G8_UINT = 47
    R8G8_TYPELESS = 48
    R8G8_UNORM = 49
    R8G8_UINT = 50
    R8G8_SNORM = 51
    R8G8_SINT = 52
    R16_TYPELESS = 53
    R16_FLOAT = 54
    D16_UNORM = 55
    R16_UNORM = 56
    R16_UINT = 57
    R16_SNORM = 58
    R16_SINT = 59
    R8_TYPELESS = 60
    R8_UNORM = 61
    R8_UINT = 62
    R8_SNORM = 63
    R8_SINT = 64
    A8_UNORM = 65
    R1_UNORM = 66
    R9G9B9E5_SHAREDEXP = 67
    R8G8_B8G8_UNORM = 68
    G8R8_G8B8_UNORM = 69
    BC1_TYPELESS = 70
    BC1_UNORM = 71
    BC1_UNORM_SRGB = 72
    BC2_TYPELESS = 73
    BC2_UNORM = 74
    BC2_UNORM_SRGB = 75
    BC3_TYPELESS = 76
    BC3_UNORM = 77
    BC3_UNORM_SRGB = 78
    BC4_TYPELESS = 79
    BC4_UNORM = 80
    BC4_SNORM = 81
    BC5_TYPELESS = 82
    BC5_UNORM = 83
    BC5_SNORM = 84
    B5G6R5_UNORM = 85
    B5G5R5A1_UNORM = 86
    B8G8R8A8_UNORM = 87
    B8G8R8X8_UNORM = 88
    R10G10B10_XR_BIAS_A2_UNORM = 89
    B8G8R8A8_TYPELESS = 90
    B8G8R8A8_UNORM_SRGB = 91
    B8G8R8X8_TYPELESS = 92
    B8G8R8X8_UNORM_SRGB = 93
    BC6H_TYPELESS = 94
    BC6H_UF16 = 95
    BC6H_SF16 = 96
    BC7_TYPELESS = 97
    BC7_UNORM = 98
    BC7_UNORM_SRGB = 99
    AYUV = 100
    Y410 = 101
    Y416 = 102
    NV12 = 103
    P010 = 104
    P016 = 105
    OPAQUE_420 = 106
    YUY2 = 107
    Y210 = 108
    Y216 = 109
    NV11 = 110
    AI44 = 111
    IA44 = 112
    P8 = 113
    A8P8 = 114
    B4G4R4A4_UNORM = 115
    P208 = 130
    V208 = 131
    V408 = 132
    SAMPLER_FEEDBACK_MIN_MIP_OPAQUE = 189
    SAMPLER_FEEDBACK_MIP_REGION_USED_OPAQUE = 190

class D3DFMT(IntEnum):
    UNKNOWN = 0
    R8G8B8 = 20
    A8R8G8B8 = 21
    X8R8G8B8 = 22
    R5G6B5 = 23
    X1R5G5B5 = 24
    A1R5G5B5 = 25
    A4R4G4B4 = 26
    R3G3B2 = 27
    A8 = 28
    A8R3G3B2 = 29
    X4R4G4B4 = 30
    A2B10G10R10 = 31
    A8B8G8R8 = 32
    X8B8G8R8 = 33
    G16R16 = 34
    A2R10G10B10 = 35
    A16B16G16R16 = 36
    A8P8 = 40
    P8 = 41
    L8 = 50
    A8L8 = 51
    A4L4 = 52
    V8U8 = 60
    L6V5U5 = 61
    X8L8V8U8 = 62
    Q8W8V8U8 = 63
    V16U16 = 64
    A2W10V10U10 = 67
    D16_LOCKABLE = 70
    D32 = 71
    D15S1 = 73
    D24S8 = 75
    D24X8 = 77
    D24X4S4 = 79
    D16 = 80
    D32F_LOCKABLE = 82
    D24FS8 = 83
    D32_LOCKABLE = 84
    S8_LOCKABLE = 85
    L16 = 81
    VERTEXDATA = 100
    INDEX16 = 101
    INDEX32 = 102
    Q16W16V16U16 = 110
    R16F = 111
    G16R16F = 112
    A16B16G16R16F = 113
    R32F = 114
    G32R32F = 115
    A32B32G32R32F = 116
    CxV8U8 = 117
    A1 = 118
    A2B10G10R10_XR_BIAS = 119
    BINARYBUFFER = 199

    UYVY = 1498831189  # i32(b"UYVY")
    R8G8_B8G8 = 1195525970  # i32(b"RGBG")
    YUY2 = 844715353  # i32(b"YUY2")
    G8R8_G8B8 = 1111970375  # i32(b"GRGB")
    DXT1 = 827611204  # i32(b"DXT1")
    DXT2 = 844388420  # i32(b"DXT2")
    DXT3 = 861165636  # i32(b"DXT3")
    DXT4 = 877942852  # i32(b"DXT4")
    DXT5 = 894720068  # i32(b"DXT5")
    DX10 = 808540228  # i32(b"DX10")
    BC4S = 1395934018  # i32(b"BC4S")
    BC4U = 1429488450  # i32(b"BC4U")
    BC5S = 1395999554  # i32(b"BC5S")
    BC5U = 1429553986  # i32(b"BC5U")
    ATI1 = 826889281  # i32(b"ATI1")
    ATI2 = 843666497  # i32(b"ATI2")
    MULTI2_ARGB8 = 827606349  # i32(b"MET1")

DDSD_CAPS: Final = 0x1
DDSD_HEIGHT: Final = 0x2
DDSD_WIDTH: Final = 0x4
DDSD_PITCH: Final = 0x8
DDSD_PIXELFORMAT: Final = 0x1000
DDSD_MIPMAPCOUNT: Final = 0x20000
DDSD_LINEARSIZE: Final = 0x80000
DDSD_DEPTH: Final = 0x800000

DDSCAPS_COMPLEX: Final = 0x8
DDSCAPS_TEXTURE: Final = 0x1000
DDSCAPS_MIPMAP: Final = 0x400000

DDSCAPS2_CUBEMAP: Final = 0x200
DDSCAPS2_CUBEMAP_POSITIVEX: Final = 0x400
DDSCAPS2_CUBEMAP_NEGATIVEX: Final = 0x800
DDSCAPS2_CUBEMAP_POSITIVEY: Final = 0x1000
DDSCAPS2_CUBEMAP_NEGATIVEY: Final = 0x2000
DDSCAPS2_CUBEMAP_POSITIVEZ: Final = 0x4000
DDSCAPS2_CUBEMAP_NEGATIVEZ: Final = 0x8000
DDSCAPS2_VOLUME: Final = 0x200000

DDPF_ALPHAPIXELS: Final = 0x1
DDPF_ALPHA: Final = 0x2
DDPF_FOURCC: Final = 0x4
DDPF_PALETTEINDEXED8: Final = 0x20
DDPF_RGB: Final = 0x40
DDPF_LUMINANCE: Final = 0x20000

DDS_FOURCC: Final = 0x4
DDS_RGB: Final = 0x40
DDS_RGBA: Final = 0x41
DDS_LUMINANCE: Final = 0x20000
DDS_LUMINANCEA: Final = 0x20001
DDS_ALPHA: Final = 0x2
DDS_PAL8: Final = 0x20

DDS_HEADER_FLAGS_TEXTURE: int
DDS_HEADER_FLAGS_MIPMAP: int
DDS_HEADER_FLAGS_VOLUME: int
DDS_HEADER_FLAGS_PITCH: int
DDS_HEADER_FLAGS_LINEARSIZE: int
DDS_HEIGHT: int
DDS_WIDTH: int
DDS_SURFACE_FLAGS_TEXTURE: int
DDS_SURFACE_FLAGS_MIPMAP: int
DDS_SURFACE_FLAGS_CUBEMAP: int
DDS_CUBEMAP_POSITIVEX: int
DDS_CUBEMAP_NEGATIVEX: int
DDS_CUBEMAP_POSITIVEY: int
DDS_CUBEMAP_NEGATIVEY: int
DDS_CUBEMAP_POSITIVEZ: int
DDS_CUBEMAP_NEGATIVEZ: int

DXT1_FOURCC: Final = 0x31545844
DXT3_FOURCC: Final = 0x33545844
DXT5_FOURCC: Final = 0x35545844

DXGI_FORMAT_R8G8B8A8_TYPELESS: Final = 27
DXGI_FORMAT_R8G8B8A8_UNORM: Final = 28
DXGI_FORMAT_R8G8B8A8_UNORM_SRGB: Final = 29
DXGI_FORMAT_BC5_TYPELESS: Final = 82
DXGI_FORMAT_BC5_UNORM: Final = 83
DXGI_FORMAT_BC5_SNORM: Final = 84
DXGI_FORMAT_BC6H_UF16: Final = 95
DXGI_FORMAT_BC6H_SF16: Final = 96
DXGI_FORMAT_BC7_TYPELESS: Final = 97
DXGI_FORMAT_BC7_UNORM: Final = 98
DXGI_FORMAT_BC7_UNORM_SRGB: Final = 99

class DdsImageFile(ImageFile):
    format: ClassVar[Literal["DDS"]]
    format_description: ClassVar[str]
    def load_seek(self, pos: int) -> None: ...

class DdsRgbDecoder(PyDecoder): ...
