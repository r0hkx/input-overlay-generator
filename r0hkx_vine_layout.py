from generator import add_rectangle, add_image, generate_overlay_files

def c(key):
    key_conversion = {
        "CAPS_LOCK": "BACKSPACE",
    }
    if key not in key_conversion:
        return key
    else:
        return key_conversion[key]

# hotbar
hotbar_color = (255, 255, 255, 100)
hotbar_x_coord = 608
hotbar_keys = ["1", "2", "3", "4", "X", "V", "CAPS_LOCK", "Z", "C"]
hotbar_images = ["images/gui4/1.png",
                 "images/gui4/2.png",
                 "images/gui4/3.png",
                 "images/gui4/4.png",
                 "images/gui4/X.png",
                 "images/gui4/V.png",
                 "images/gui4/Caps.png",
                 "images/gui4/Z.png",
                 "images/gui4/C.png"]
for x in range(9):
    add_rectangle(key=c(hotbar_keys[x]), pos=(hotbar_x_coord, 1004), size=(64, 64), pressed_color=hotbar_color)
    if (x != 6):
        add_image(key=c(hotbar_keys[x]), pos=(hotbar_x_coord + 22, 1022), pressed_image=hotbar_images[x])
    hotbar_x_coord += 80
add_image(key=c(hotbar_keys[6]), pos=(1074, 1022), pressed_image=hotbar_images[6])

# offhand
add_rectangle(key="F", pos=(492, 1004), size=(64, 64), pressed_color=hotbar_color)
add_image(key="F", pos=(514, 1022), pressed_image="images/gui4/F.png")

# left actionbar stuff
row0 = 600
row1 = row0 + 48
row2 = row1 + 48
row3 = row2 + 48
row4 = row3 + 48
add_image(key=c("BACKQUOTE"), pos=(572, row0), pressed_image="images/gui4/Sprint.png")
add_image(key=c("ESCAPE"), pos=(620, row1), pressed_image="images/gui4/Esc.png")
add_image(key=c("TAB"), pos=(644, row2), pressed_image="images/gui4/F5.png")
add_image(key=c("Q"), pos=(708, row2), pressed_image="images/gui4/Q.png")
add_image(key=c("W"), pos=(748, row2), pressed_image="images/gui4/W.png")
add_image(key=c("E"), pos=(788, row2), pressed_image="images/gui4/E.png")
add_image(key=c("A"), pos=(708, row3), pressed_image="images/gui4/A.png")
add_image(key=c("S"), pos=(748, row3), pressed_image="images/gui4/S.png")
add_image(key=c("D"), pos=(788, row3), pressed_image="images/gui4/D.png")
add_image(key=c("SHIFT_L"), pos=(600, row4), pressed_image="images/gui4/Shift.png")
add_image(key=c("SPACE"), pos=(700, row4), pressed_image="images/gui4/Space.png")

# right actionbar stuff
add_image(key="MOUSE_BUTTON1", pos=(1080, row4), pressed_image="images/gui4/LMB.png")
add_image(key="MOUSE_BUTTON2", pos=(1168, row4), pressed_image="images/gui4/RMB.png")
add_image(key="MOUSE_BUTTON3", pos=(1060, row3), pressed_image="images/gui4/Pick Block.png")

generate_overlay_files((1920, 1080))