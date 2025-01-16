from generator import add_rectangle, add_image, generate_overlay_files

def c(key):
    key_conversion = {
        "CAPS_LOCK": "V",
        "V": "BACKSPACE",
        "A": "Z",
        "D": "X",
        "Z": "A",
        "X": "D",
    }
    if key not in key_conversion:
        return key
    else:
        return key_conversion[key]

# hotbar
hotbar_color = (255, 255, 255, 100)
hotbar_x_coord = 608
hotbar_keys = ["1", "2", "3", "4", "X", "V", "F", "Z", "C"]
for x in range(9):
    add_rectangle(key=c(hotbar_keys[x]), pos=(hotbar_x_coord, 1004), size=(64, 64), pressed_color=hotbar_color)
    hotbar_x_coord += 80

# offhand
add_rectangle(key="K", pos=(492, 1004), size=(64, 64), pressed_color=hotbar_color)

# left actionbar stuff
row0 = 600
row1 = row0 + 48
row2 = row1 + 48
row3 = row2 + 48
row4 = row3 + 48
add_image(key=c("BACKQUOTE"), pos=(572, row0), pressed_image="images/gui4/Sprint.png")
add_image(key=c("ESCAPE"), pos=(620, row1), pressed_image="images/gui4/Esc.png")
add_image(key=c("Q"), pos=(708, row2), pressed_image="images/gui4/Q.png")
add_image(key=c("W"), pos=(748, row2), pressed_image="images/gui4/W.png")
add_image(key=c("E"), pos=(788, row2), pressed_image="images/gui4/E.png")
add_image(key=c("F3"), pos=(828, row2), pressed_image="images/gui4/F3.png")
add_image(key=c("CAPS_LOCK"), pos=(604, row3), pressed_image="images/gui4/Chat.png")
add_image(key=c("A"), pos=(708, row3), pressed_image="images/gui4/A.png")
add_image(key=c("S"), pos=(748, row3), pressed_image="images/gui4/S.png")
add_image(key=c("D"), pos=(788, row3), pressed_image="images/gui4/D.png")
add_image(key=c("SHIFT_L"), pos=(600, row4), pressed_image="images/gui4/Shift.png")
add_image(key=c("SPACE"), pos=(700, row4), pressed_image="images/gui4/Space.png")

# right actionbar stuff
add_image(key="MOUSE_BUTTON1", pos=(1080, row4), pressed_image="images/gui4/LMB.png")
add_image(key="MOUSE_BUTTON2", pos=(1168, row4), pressed_image="images/gui4/RMB.png")
add_image(key="MOUSE_BUTTON4", pos=(1016, row4), pressed_image="images/gui4/F5.png")
add_image(key="MOUSE_BUTTON3", pos=(1060, row3), pressed_image="images/gui4/Pick Block.png")

generate_overlay_files((1920, 1080))
