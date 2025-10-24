import os

from kivy.utils import get_color_from_hex


class AppConfig:
    BASE_DIR = os.path.dirname(__file__)
    KV_PATH = os.path.join(BASE_DIR, "kv")
    ASSETS_PATH = os.path.join(BASE_DIR, "assets")
    IMAGES_PATH = os.path.join(ASSETS_PATH, "images")

    # --- Color Palette ---
    # Main Background (Light Sage/Olive)
    COLOR_LAVENDER = get_color_from_hex('#CCB6C5')
    COLOR_SOFT_CORAL = get_color_from_hex('#F7A78A')
    COLOR_BUTTER_YELLOW = get_color_from_hex('#F4D986')
    COLOR_SAGE_GREEN = get_color_from_hex('#A7BB88')
    COLOR_SEAFOAM_GREEN = get_color_from_hex('#95B9A5')
    COLOR_WARM_CREAM = get_color_from_hex('#F7EAD1')
    COLOR_FOREST_GREEN = get_color_from_hex('#2F4538')
    COLOR_TEAL = get_color_from_hex('#8AAFA1')
