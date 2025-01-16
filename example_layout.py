from generator import add_rectangle, add_image, generate_overlay_files

# hotbar
add_rectangle(key="1", pos=(696, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="2", pos=(756, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="3", pos=(816, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="4", pos=(876, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="X", pos=(936, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="V", pos=(996, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="F", pos=(1056, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="Z", pos=(1116, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="C", pos=(1176, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100))
add_rectangle(key="K", pos=(609, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100), not_pressed_color=(100, 0, 100, 255))

# actionbar
add_image(key="W", pos=(801, 792), pressed_image="images/gui3/W.png", not_pressed_image="images/gui3/E.png")
add_image(key="A", pos=(771, 828), pressed_image="images/gui3/A.png")
add_image(key="S", pos=(801, 828), pressed_image="images/gui3/S.png")
add_image(key="D", pos=(831, 828), pressed_image="images/gui3/D.png")
add_image(key="SPACE", pos=(765, 864), pressed_image="images/gui3/Space.png")
add_image(key="MOUSE_BUTTON1", pos=(1050, 864), pressed_image="images/gui3/LMB.png")
add_image(key="MOUSE_BUTTON2", pos=(1116, 864), pressed_image="images/gui3/RMB.png")
add_image(key="MOUSE_BUTTON3", pos=(1036, 828), pressed_image="images/gui3/Pick Block.png")

generate_overlay_files((1920, 1080))