from generator import add_rectangle, add_image, generate_overlay_files

def c(key):
    key_conversion = {
        "CAPS_LOCK": "BACKSPACE",
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
hotbar_x_coord = 696
hotbar_keys = ["1", "2", "3", "4", "X", "V", "F", "Z", "C"]
for x in range(9):
    add_rectangle(key=c(hotbar_keys[x]), pos=(hotbar_x_coord, 1023), size=(48, 48), pressed_color=hotbar_color)
    hotbar_x_coord += 60

# offhand
add_rectangle(key="K", pos=(609, 1023), size=(48, 48), pressed_color=hotbar_color)

# left actionbar stuff
row0 = 720
row1 = 756
row2 = 792
row3 = 828
row4 = 864
add_image(key=c("BACKQUOTE"), pos=(669, row0), pressed_image="images/Sprint.png")
add_image(key=c("ESCAPE"), pos=(705, row1), pressed_image="images/Esc.png")
add_image(key=c("TAB"), pos=(723, row2), pressed_image="images/F5.png")
add_image(key=c("Q"), pos=(771, row2), pressed_image="images/Q.png")
add_image(key=c("W"), pos=(801, row2), pressed_image="images/W.png")
add_image(key=c("E"), pos=(831, row2), pressed_image="images/E.png")
add_image(key=c("F3"), pos=(861, row2), pressed_image="images/F3.png")
add_image(key=c("CAPS_LOCK"), pos=(681, row3), pressed_image="images/Chat.png")
add_image(key=c("A"), pos=(771, row3), pressed_image="images/A.png")
add_image(key=c("S"), pos=(801, row3), pressed_image="images/S.png")
add_image(key=c("D"), pos=(831, row3), pressed_image="images/D.png")
add_image(key=c("SHIFT_L"), pos=(678, row4), pressed_image="images/Shift.png")
add_image(key=c("SPACE"), pos=(765, row4), pressed_image="images/Space.png")

# right actionbar stuff
add_image(key="MOUSE_BUTTON1", pos=(1050, row4), pressed_image="images/LMB.png")
add_image(key="MOUSE_BUTTON2", pos=(1116, row4), pressed_image="images/RMB.png")
add_image(key="MOUSE_BUTTON3", pos=(1036, row3), pressed_image="images/Pick Block.png")

generate_overlay_files((1920, 1080))
