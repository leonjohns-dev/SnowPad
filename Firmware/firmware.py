import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.RGB import RGB, AnimationModes


keyboard = KMKKeyboard()

# =========================
# Matrix
# =========================

keyboard.row_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP4,
)

keyboard.col_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


# =========================
# Keys
# =========================

keyboard.keymap = [
    [
        KC.KP_7, KC.KP_8, KC.KP_9,
        KC.KP_4, KC.KP_5, KC.KP_6,
        KC.KP_1, KC.KP_2, KC.KP_3,
        KC.KP_MINUS, KC.KP_0, KC.KP_PLUS,
    ]
]


# =========================
# RGB
# =========================

rgb = RGB(
    pixel_pin=board.GP29,
    num_pixels=18,
    animation_mode=AnimationModes.RAINBOW,
)

keyboard.extensions.append(rgb)


# =========================
# Start
# =========================

if __name__ == '__main__':
    keyboard.go()
