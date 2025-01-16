from generator import add_rectangle, add_image, generate_overlay_files

# hotbar
hotbar_color = (255, 255, 255, 100)
hotbar_x_coord = 608
hotbar_keys = ["1", "2", "3", "4", "R", "X", "C", "V", "Z"]
for x in range(9):
    add_rectangle(key=hotbar_keys[x], pos=(hotbar_x_coord, 1004), size=(64, 64), pressed_color=hotbar_color)
    hotbar_x_coord += 80

# offhand
add_rectangle(key="MOUSE_BUTTON4", pos=(492, 1004), size=(64, 64), pressed_color=hotbar_color)

# left actionbar stuff
row0 = 600
row1 = row0 + 48
row2 = row1 + 48
row3 = row2 + 48
row4 = row3 + 48

add_image(key="ESCAPE", pos=(620, row2), pressed_image="images/gui4/Esc.png")
add_image(key="Q", pos=(708, row2), pressed_image="images/gui4/Q.png")
add_image(key="W", pos=(748, row2), pressed_image="images/gui4/W.png")
add_image(key="E", pos=(788, row2), pressed_image="images/gui4/E.png")
add_image(key="F3", pos=(828, row2), pressed_image="images/gui4/F3.png")

add_image(key="SHIFT_L", pos=(572, row3), pressed_image="images/gui4/Sprint.png")
add_image(key="A", pos=(708, row3), pressed_image="images/gui4/A.png")
add_image(key="S", pos=(748, row3), pressed_image="images/gui4/S.png")
add_image(key="D", pos=(788, row3), pressed_image="images/gui4/D.png")
add_image(key="F", pos=(828, row3), pressed_image="images/gui4/F5.png")

add_image(key="CONTROL_L", pos=(576, row4), pressed_image="images/gui4/Sneak.png")
add_image(key="SPACE", pos=(700, row4), pressed_image="images/gui4/Space.png")
add_image(key="ALT_L", pos=(828, row4), pressed_image="images/gui4/Chat.png")

# right actionbar stuff
add_image(key="MOUSE_BUTTON1", pos=(1080, row4), pressed_image="images/gui4/LMB.png")
add_image(key="MOUSE_BUTTON2", pos=(1168, row4), pressed_image="images/gui4/RMB.png")
add_image(key="MOUSE_BUTTON3", pos=(1060, row3), pressed_image="images/gui4/Pick Block.png")

generate_overlay_files((1920, 1080))
