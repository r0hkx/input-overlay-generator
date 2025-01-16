from PIL import Image
import os
import json

# from https://github.com/kwhat/libuiohook/blob/1.2/include/uiohook.h#L137
# this is what the input overlay plugin uses presumably
keys = {
    "MOUSE_NOBUTTON": 0, # any mouse button
    "MOUSE_BUTTON1": 1, # left click
    "MOUSE_BUTTON2": 2, # right click
    "MOUSE_BUTTON3": 3, # middle click
    "MOUSE_BUTTON4": 4, # side mouse button (closer to you)
    "MOUSE_BUTTON5": 5, # side mouse button (further from you)
    "ESCAPE": 0x0001,
    "F1": 0x003B,
    "F2": 0x003C,
    "F3": 0x003D,
    "F4": 0x003E,
    "F5": 0x003F,
    "F6": 0x0040,
    "F7": 0x0041,
    "F8": 0x0042,
    "F9": 0x0043,
    "F10": 0x0044,
    "F11": 0x0057,
    "F12": 0x0058,
    "F13": 0x005B,
    "F14": 0x005C,
    "F15": 0x005D,
    "F16": 0x0063,
    "F17": 0x0064,
    "F18": 0x0065,
    "F19": 0x0066,
    "F20": 0x0067,
    "F21": 0x0068,
    "F22": 0x0069,
    "F23": 0x006A,
    "F24": 0x006B,
    "BACKQUOTE": 0x0029, #aka ` or ~
    "1": 0x0002,
    "2": 0x0003,
    "3": 0x0004,
    "4": 0x0005,
    "5": 0x0006,
    "6": 0x0007,
    "7": 0x0008,
    "8": 0x0009,
    "9": 0x000A,
    "0": 0x000B,
    "MINUS": 0x000C,
    "EQUALS": 0x000D,
    "BACKSPACE": 0x000E,
    "TAB": 0x000F,
    "CAPS_LOCK": 0x003A,
    "A": 0x001E,
    "B": 0x0030,
    "C": 0x002E,
    "D": 0x0020,
    "E": 0x0012,
    "F": 0x0021,
    "G": 0x0022,
    "H": 0x0023,
    "I": 0x0017,
    "J": 0x0024,
    "K": 0x0025,
    "L": 0x0026,
    "M": 0x0032,
    "N": 0x0031,
    "O": 0x0018,
    "P": 0x0019,
    "Q": 0x0010,
    "R": 0x0013,
    "S": 0x001F,
    "T": 0x0014,
    "U": 0x0016,
    "V": 0x002F,
    "W": 0x0011,
    "X": 0x002D,
    "Y": 0x0015,
    "Z": 0x002C,
    "OPEN_BRACKET": 0x001A,
    "CLOSE_BRACKET": 0x001B,
    "BACK_SLASH": 0x002B,
    "SEMICOLON": 0x0027,
    "QUOTE": 0x0028,
    "ENTER": 0x001C,
    "COMMA": 0x0033,
    "PERIOD": 0x0034,
    "SLASH": 0x0035,
    "SPACE": 0x0039,
    "PRINTSCREEN": 0x0E37,
    "SCROLL_LOCK": 0x0046,
    "PAUSE": 0x0E45,
    "LESSER_GREATER": 0x0E46,
    "INSERT": 0x0E52,
    "DELETE": 0x0E53,
    "HOME": 0x0E47,
    "END": 0x0E4F,
    "PAGE_UP": 0x0E49,
    "PAGE_DOWN": 0x0E51,
    "UP": 0xE048,
    "LEFT": 0xE04B,
    "CLEAR": 0xE04C,
    "RIGHT": 0xE04D,
    "DOWN": 0xE050,
    "NUM_LOCK": 0x0045,
    "KP_DIVIDE": 0x0E35, # KP = Keypad/Numpad
    "KP_MULTIPLY": 0x0037,
    "KP_SUBTRACT": 0x004A,
    "KP_EQUALS": 0x0E0D,
    "KP_ADD": 0x004E,
    "KP_ENTER": 0x0E1C,
    "KP_SEPARATOR": 0x0053,
    "KP_1": 0x004F,
    "KP_2": 0x0050,
    "KP_3": 0x0051,
    "KP_4": 0x004B,
    "KP_5": 0x004C,
    "KP_6": 0x004D,
    "KP_7": 0x0047,
    "KP_8": 0x0048,
    "KP_9": 0x0049,
    "KP_0": 0x0052,
    "KP_END": 0xEE00,
    "KP_DOWN": 0xEE00,
    "KP_PAGE_DOWN": 0xEE00,
    "KP_LEFT": 0xEE00,
    "KP_CLEAR": 0xEE00,
    "KP_RIGHT": 0xEE00,
    "KP_HOME": 0xEE00,
    "KP_UP": 0xEE00,
    "KP_PAGE_UP": 0xEE00,
    "KP_INSERT": 0xEE00,
    "KP_DELETE": 0xEE00,
    "SHIFT_L": 0x002A,
    "SHIFT_R": 0x0036,
    "CONTROL_L": 0x001D,
    "CONTROL_R": 0x0E1D,
    "ALT_L": 0x0038,
    "ALT_R": 0x0E38,
    "META_L": 0x0E5B,
    "META_R": 0x0E5C,
    "CONTEXT_MENU": 0x0E5D,
    "POWER": 0xE05E,
    "SLEEP": 0xE05F,
    "WAKE": 0xE063,
    "MEDIA_PLAY": 0xE022,
    "MEDIA_STOP": 0xE024,
    "MEDIA_PREVIOUS": 0xE010,
    "MEDIA_NEXT": 0xE019,
    "MEDIA_SELECT": 0xE06D,
    "MEDIA_EJECT": 0xE02C,
    "VOLUME_MUTE": 0xE020,
    "VOLUME_UP": 0xE030,
    "VOLUME_DOWN": 0xE02E,
    "APP_MAIL": 0xE06C,
    "APP_CALCULATOR": 0xE021,
    "APP_MUSIC": 0xE03C,
    "APP_PICTURES": 0xE064,
    "BROWSER_SEARCH": 0xE065,
    "BROWSER_HOME": 0xE032,
    "BROWSER_BACK": 0xE06A,
    "BROWSER_FORWARD": 0xE069,
    "BROWSER_STOP": 0xE068,
    "BROWSER_REFRESH": 0xE067,
    "BROWSER_FAVORITES": 0xE066,
    "KATAKANA": 0x0070,
    "UNDERSCORE": 0x0073,
    "FURIGANA": 0x0077,
    "KANJI": 0x0079,
    "HIRAGANA": 0x007B,
    "YEN": 0x007D,
    "KP_COMMA": 0x007E,
    "SUN_HELP": 0xFF75,
    "SUN_STOP": 0xFF78,
    "SUN_PROPS": 0xFF76,
    "SUN_FRONT": 0xFF77,
    "SUN_OPEN": 0xFF74,
    "SUN_FIND": 0xFF7E,
    "SUN_AGAIN": 0xFF79,
    "SUN_UNDO": 0xFF7A,
    "SUN_COPY": 0xFF7C,
    "SUN_INSERT": 0xFF7D,
    "SUN_CUT": 0xFF7B,
}

elements = []


def add_image(key, pos, pressed_image, not_pressed_image=None):

    if isinstance(pressed_image, str):
        try:
            pressed_image = Image.open(pressed_image)
        except FileNotFoundError:
            print("Skipping element " + key +
                  ". Reason: File not found. Is the file path correct?")
            return

    if not_pressed_image == None:
        not_pressed_image = Image.new("RGBA", pressed_image.size, (0, 0, 0, 0))

    if isinstance(not_pressed_image, str):
        not_pressed_image = Image.open(not_pressed_image)
        
    if key[:5] == "MOUSE":
        type = 3
    else:
        type = 1
        
    if pressed_image.size != not_pressed_image.size:
        print("Skipping element " + key +
              ". Reason: pressed_image size and not_pressed_image "
              "size are not equal. The sizes of these two images "
              "need to be exactly equal.")
        return
    
    elements.append(
        {
            "key": key,
            "type": type,
            "pos": pos,
            "size": pressed_image.size,
            "pressed_image": pressed_image,
            "not_pressed_image": not_pressed_image,
        }
    )
    
    print("Added element: Key: " + key + ", Type: " + str(type) +
              ", Pos: " + str(pos) + ", Size: " + str(pressed_image.size))


def add_rectangle(key, pos, size, pressed_color, not_pressed_color=None):

    if pressed_color != None:
        pressed_image = Image.new("RGBA", size, pressed_color)
    else:
        pressed_image = Image.new("RGBA", size, (0, 0, 0, 0))

    if not_pressed_color != None:
        not_pressed_image = Image.new("RGBA", size, not_pressed_color)
    else:
        not_pressed_image = Image.new("RGBA", size, (0, 0, 0, 0))

    add_image(
        key=key,
        pos=pos,
        pressed_image=pressed_image,
        not_pressed_image=not_pressed_image,
    )


def generate_overlay_files(resolution):

    total_x = 1
    largest_y = 0
    for element in elements:
        # 3 pixel buffer between each image
        total_x += element["size"][0] + 3

        if largest_y < element["size"][1]:
            largest_y = element["size"][1]
    # 1 pixel buffer on the top and bottom, 3 in between pressed and
    # not pressed image
    total_y = (largest_y * 2) + 1 + 3 + 1

    output_image = Image.new("RGBA", (total_x, total_y))

    config = {
        # i don't think these values matter
        "default_height": 100,
        "default_width": 100,
        "space_h": 0,
        "space_v": 0,
        # this sets the source size in obs, doesn't fully matter though
        "overlay_width": resolution[0],
        "overlay_height": resolution[1],
    }
    
    config_elements = []
    
    x_offset = 1
    for element in elements:
        output_image.paste(element["pressed_image"], (x_offset, largest_y + 3 + 1))
        output_image.paste(
            element["not_pressed_image"],
            (x_offset, (largest_y - element["size"][1]) + 1),
        )
        config_element = {
            "id": element["key"],
            "code": keys[element["key"]],
            "type": element["type"],
            "z_level": 1,
            "pos": element["pos"],
            "size": element["size"],
            "mapping": [
                x_offset,
                largest_y - element["size"][1],
                element["size"][0],
                element["size"][1] + 1,
            ]
        }
        
        config_elements.append(config_element)
        x_offset += element["size"][0] + 3
    
    config["elements"] = config_elements

    output_image.save("overlay_image.png")
    output_config_json = json.dumps(config, indent=4)
    with open("overlay_config.json", "w") as output_config:
        output_config.write(output_config_json)

    print("Output files to " + os.getcwd())