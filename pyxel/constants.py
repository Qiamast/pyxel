import glfw

VERSION = '0.7.11'

GLFW_VERSION = '3.2.1'

DEFAULT_CAPTION = 'Pyxel'
DEFAULT_SCALE = 0
DEFAULT_PALETTE = [
    0x000000, 0x1d2b53, 0x7e2553, 0x008751, 0xab5236, 0x5f574f, 0xc2c3c7,
    0xfff1e8, 0xff004d, 0xffa300, 0xffec27, 0x00e436, 0x29adff, 0x83769c,
    0xff77a8, 0xffccaa
]
DEFAULT_FPS = 30
DEFAULT_BORDER_WIDTH = 0
DEFAULT_BORDER_COLOR = 0x101018

ICON_DATA = [
    '0000000110000000',
    '0000011f71100000',
    '00011ff11ff11000',
    '011ff111111ff110',
    '1ae1111111111c71',
    '1e1ee111111cc1c1',
    '1e111ee11cc111c1',
    '1e11111e711111c1',
    '1e111111c11111c1',
    '1e111111c11111c1',
    '1e111111c11111c1',
    '1ae11111c1111c71',
    '011ee111c11cc110',
    '00011ee1ccc11000',
    '0000011e71100000',
    '0000000110000000',
]

APP_MAX_SCREEN_SIZE = 256
APP_SCREEN_SCALE_ADJUST = 2
APP_SCREEN_CAPTURE_COUNT = 900
APP_SCREEN_CAPTURE_SCALE = 2
APP_MEASURE_FRAME_COUNT = 10

RENDERER_IMAGE_COUNT = 4
RENDERER_IMAGE_WIDTH = 256
RENDERER_IMAGE_HEIGHT = 256
RENDERER_MIN_TEXTURE_SIZE = 256

DRAW_TYPE_PIX = 0
DRAW_TYPE_LINE = 1
DRAW_TYPE_RECT = 2
DRAW_TYPE_RECTB = 3
DRAW_TYPE_CIRC = 4
DRAW_TYPE_CIRCB = 5
DRAW_TYPE_BLT = 6
DRAW_TYPE_TEXT = 7
DRAW_MAX_COUNT = 10000

FONT_MIN_CODE = 32
FONT_MAX_CODE = 127
FONT_WIDTH = 4
FONT_HEIGHT = 6
FONT_ROW_COUNT = RENDERER_IMAGE_WIDTH // FONT_WIDTH
FONT_DATA = [
    0x000000, 0x444040, 0xaa0000, 0xaeaea0, 0x6c6c40, 0x824820, 0x4a4ac0,
    0x440000, 0x244420, 0x844480, 0xa4e4a0, 0x04e400, 0x000480, 0x00e000,
    0x000040, 0x224880, 0x6aaac0, 0x4c4440, 0xc248e0, 0xc242c0, 0xaae220,
    0xe8c2c0, 0x68eae0, 0xe24880, 0xeaeae0, 0xeae2c0, 0x040400, 0x040480,
    0x248420, 0x0e0e00, 0x842480, 0xe24040, 0x4aa860, 0x4aeaa0, 0xcacac0,
    0x688860, 0xcaaac0, 0xe8e8e0, 0xe8e880, 0x68ea60, 0xaaeaa0, 0xe444e0,
    0x222a40, 0xaacaa0, 0x8888e0, 0xaeeaa0, 0xcaaaa0, 0x4aaa40, 0xcac880,
    0x4aae60, 0xcaeca0, 0x6842c0, 0xe44440, 0xaaaa60, 0xaaaa40, 0xaaeea0,
    0xaa4aa0, 0xaa4440, 0xe248e0, 0x644460, 0x884220, 0xc444c0, 0x4a0000,
    0x0000e0, 0x840000, 0x06aa60, 0x8caac0, 0x068860, 0x26aa60, 0x06ac60,
    0x24e440, 0x06ae24, 0x8caaa0, 0x404440, 0x2022a4, 0x8acca0, 0xc444e0,
    0x0eeea0, 0x0caaa0, 0x04aa40, 0x0caac8, 0x06aa62, 0x068880, 0x06c6c0,
    0x4e4460, 0x0aaa60, 0x0aaa40, 0x0aaee0, 0x0a44a0, 0x0aa624, 0x0e24e0,
    0x64c460, 0x444440, 0xc464c0, 0x6c0000, 0xeeeee0
]

AUDIO_SAMPLE_RATE = 22050
AUDIO_BLOCK_SIZE = 2205
AUDIO_CHANNEL_COUNT = 4
AUDIO_SOUND_COUNT = 64
AUDIO_ONE_SPEED = AUDIO_SAMPLE_RATE // 120
AUDIO_ONE_VOLUME = 0x7fff // (AUDIO_CHANNEL_COUNT * 7)

SOUND_TONE_TRIANGLE = 0
SOUND_TONE_SQUARE = 1
SOUND_TONE_PULSE = 2
SOUND_TONE_NOISE = 3
SOUND_EFFECT_NONE = 0
SOUND_EFFECT_SLIDE = 1
SOUND_EFFECT_VIBRATO = 2
SOUND_EFFECT_FADEOUT = 3
SOUND_NOTE_TABLE = {
    'c': 0,
    'd': 2,
    'e': 4,
    'f': 5,
    'g': 7,
    'a': 9,
    'b': 11,
}
SOUND_TONE_TABLE = {
    't': SOUND_TONE_TRIANGLE,
    's': SOUND_TONE_SQUARE,
    'p': SOUND_TONE_PULSE,
    'n': SOUND_TONE_NOISE,
}
SOUND_EFFECT_TABLE = {
    'n': SOUND_EFFECT_NONE,
    's': SOUND_EFFECT_SLIDE,
    'v': SOUND_EFFECT_VIBRATO,
    'f': SOUND_EFFECT_FADEOUT,
}

KEY_UNKNOWN = glfw.KEY_UNKNOWN
KEY_SPACE = glfw.KEY_SPACE
KEY_APOSTROPHE = glfw.KEY_APOSTROPHE
KEY_COMMA = glfw.KEY_COMMA
KEY_MINUS = glfw.KEY_MINUS
KEY_PERIOD = glfw.KEY_PERIOD
KEY_SLASH = glfw.KEY_SLASH
KEY_0 = glfw.KEY_0
KEY_1 = glfw.KEY_1
KEY_2 = glfw.KEY_2
KEY_3 = glfw.KEY_3
KEY_4 = glfw.KEY_4
KEY_5 = glfw.KEY_5
KEY_6 = glfw.KEY_6
KEY_7 = glfw.KEY_7
KEY_8 = glfw.KEY_8
KEY_9 = glfw.KEY_9
KEY_SEMICOLON = glfw.KEY_SEMICOLON
KEY_EQUAL = glfw.KEY_EQUAL
KEY_A = glfw.KEY_A
KEY_B = glfw.KEY_B
KEY_C = glfw.KEY_C
KEY_D = glfw.KEY_D
KEY_E = glfw.KEY_E
KEY_F = glfw.KEY_F
KEY_G = glfw.KEY_G
KEY_H = glfw.KEY_H
KEY_I = glfw.KEY_I
KEY_J = glfw.KEY_J
KEY_K = glfw.KEY_K
KEY_L = glfw.KEY_L
KEY_M = glfw.KEY_M
KEY_N = glfw.KEY_N
KEY_O = glfw.KEY_O
KEY_P = glfw.KEY_P
KEY_Q = glfw.KEY_Q
KEY_R = glfw.KEY_R
KEY_S = glfw.KEY_S
KEY_T = glfw.KEY_T
KEY_U = glfw.KEY_U
KEY_V = glfw.KEY_V
KEY_W = glfw.KEY_W
KEY_X = glfw.KEY_X
KEY_Y = glfw.KEY_Y
KEY_Z = glfw.KEY_Z
KEY_LEFT_BRACKET = glfw.KEY_LEFT_BRACKET
KEY_BACKSLASH = glfw.KEY_BACKSLASH
KEY_RIGHT_BRACKET = glfw.KEY_RIGHT_BRACKET
KEY_GRAVE_ACCENT = glfw.KEY_GRAVE_ACCENT
KEY_WORLD_1 = glfw.KEY_WORLD_1
KEY_WORLD_2 = glfw.KEY_WORLD_2
KEY_ESCAPE = glfw.KEY_ESCAPE
KEY_ENTER = glfw.KEY_ENTER
KEY_TAB = glfw.KEY_TAB
KEY_BACKSPACE = glfw.KEY_BACKSPACE
KEY_INSERT = glfw.KEY_INSERT
KEY_DELETE = glfw.KEY_DELETE
KEY_RIGHT = glfw.KEY_RIGHT
KEY_LEFT = glfw.KEY_LEFT
KEY_DOWN = glfw.KEY_DOWN
KEY_UP = glfw.KEY_UP
KEY_PAGE_UP = glfw.KEY_PAGE_UP
KEY_PAGE_DOWN = glfw.KEY_PAGE_DOWN
KEY_HOME = glfw.KEY_HOME
KEY_END = glfw.KEY_END
KEY_CAPS_LOCK = glfw.KEY_CAPS_LOCK
KEY_SCROLL_LOCK = glfw.KEY_SCROLL_LOCK
KEY_NUM_LOCK = glfw.KEY_NUM_LOCK
KEY_PRINT_SCREEN = glfw.KEY_PRINT_SCREEN
KEY_PAUSE = glfw.KEY_PAUSE
KEY_F1 = glfw.KEY_F1
KEY_F2 = glfw.KEY_F2
KEY_F3 = glfw.KEY_F3
KEY_F4 = glfw.KEY_F4
KEY_F5 = glfw.KEY_F5
KEY_F6 = glfw.KEY_F6
KEY_F7 = glfw.KEY_F7
KEY_F8 = glfw.KEY_F8
KEY_F9 = glfw.KEY_F9
KEY_F10 = glfw.KEY_F10
KEY_F11 = glfw.KEY_F11
KEY_F12 = glfw.KEY_F12
KEY_F13 = glfw.KEY_F13
KEY_F14 = glfw.KEY_F14
KEY_F15 = glfw.KEY_F15
KEY_F16 = glfw.KEY_F16
KEY_F17 = glfw.KEY_F17
KEY_F18 = glfw.KEY_F18
KEY_F19 = glfw.KEY_F19
KEY_F20 = glfw.KEY_F20
KEY_F21 = glfw.KEY_F21
KEY_F22 = glfw.KEY_F22
KEY_F23 = glfw.KEY_F23
KEY_F24 = glfw.KEY_F24
KEY_F25 = glfw.KEY_F25
KEY_KP_0 = glfw.KEY_KP_0
KEY_KP_1 = glfw.KEY_KP_1
KEY_KP_2 = glfw.KEY_KP_2
KEY_KP_3 = glfw.KEY_KP_3
KEY_KP_4 = glfw.KEY_KP_4
KEY_KP_5 = glfw.KEY_KP_5
KEY_KP_6 = glfw.KEY_KP_6
KEY_KP_7 = glfw.KEY_KP_7
KEY_KP_8 = glfw.KEY_KP_8
KEY_KP_9 = glfw.KEY_KP_9
KEY_KP_DECIMAL = glfw.KEY_KP_DECIMAL
KEY_KP_DIVIDE = glfw.KEY_KP_DIVIDE
KEY_KP_MULTIPLY = glfw.KEY_KP_MULTIPLY
KEY_KP_SUBTRACT = glfw.KEY_KP_SUBTRACT
KEY_KP_ADD = glfw.KEY_KP_ADD
KEY_KP_ENTER = glfw.KEY_KP_ENTER
KEY_KP_EQUAL = glfw.KEY_KP_EQUAL
KEY_LEFT_SHIFT = glfw.KEY_LEFT_SHIFT
KEY_LEFT_CONTROL = glfw.KEY_LEFT_CONTROL
KEY_LEFT_ALT = glfw.KEY_LEFT_ALT
KEY_LEFT_SUPER = glfw.KEY_LEFT_SUPER
KEY_RIGHT_SHIFT = glfw.KEY_RIGHT_SHIFT
KEY_RIGHT_CONTROL = glfw.KEY_RIGHT_CONTROL
KEY_RIGHT_ALT = glfw.KEY_RIGHT_ALT
KEY_RIGHT_SUPER = glfw.KEY_RIGHT_SUPER
KEY_MENU = glfw.KEY_MENU

KEY_LEFT_BUTTON = 1001
KEY_MIDDLE_BUTTON = 1002
KEY_RIGHT_BUTTON = 1003
