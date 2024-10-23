# input-overlay-generator
Simple python script to generate image and config files for use with the [OBS Input Overlay plugin](https://obsproject.com/forum/resources/input-overlay.552/).
This is NOT affiliated with OBS or the plugin.

## Capabilities and Limitations
This is a simple script written for a limited use case, and as such has many limitations. Any limitations are easily bypassed by using the recommend process for creating a custom overlay, as detailed on the plugin's page, linked above. This script was created because I don't like using io-cct, as well as the fact I wanted to create a non-standard overlay.

Capabilities:
* Programmatically generate both image and config files that immediately work
* Quickly make small and large changes to your overlay
* Easily share editable files
* Avoid using io-cct!

Limitations:
* Cannot use anything other than keyboard and mouse button inputs
* Cannot specify Z level of element (which element appears on top)

If you really want these features, contact me on discord and I can help you out.

## How to use
1. Install the [OBS Input Overlay Plugin](https://obsproject.com/forum/resources/input-overlay.552/) (tutorial on linked page). Note that only Windows and Linux are supported (sorry mac users)
2. Install [Python](https://www.python.org/downloads/)
3. Scroll up on [this Github repo](https://github.com/r0hkx/input-overlay-generator), click the green "Code" button, then click "Download ZIP"
4. Extract the ZIP. There should be five files and one folder:
    1. `images`
    2. `example_layout.py`
    3. `generator.py`
    4. `r0hkx_layout.py`
    5. `README.md`
    6. `RUN_THIS.bat`
5. You can delete `README.md`
6. Double click `RUN_THIS.bat` to run it, or run `pip install pillow` in the command line. This installs a required dependency for the script. You only need to run this once, and you can delete `RUN_THIS.bat` after running it
7. Make a copy of `example_layout.py`. Name it whatever you want. It needs to stay in the same folder as `generator.py`
8. Open your copy of `example_layout.py` with a text editor (notepad works fine)
9. Notice `from generator import...` at the top of the file. This has the be the first line in the file.
10. Likewise, notice `generate_overlay_files((1920, 1080))` at the bottom of the file. This has to be the last line in the file.
    1. You may want to change those numbers to match your desktop resolution.
11. To add an image to the overlay, use `add_image()` with the following parameters:
    1. `key`. Example: `key="W"`. `key` needs to *exactly* match a key in the list at the beginning of `generator.py`. Open that file with a text editor to view the list (ignore the letters and numbers after the key). The name of the key needs to be in quotes.
    2. `pos`. Example: `pos=(801, 792)`. `pos` is the position of the top left corner of `pressed_image` and `not_pressed_image`, in pixels. There need to be exactly two numbers, separated by a comma, all within parentheses.
    3. `pressed_image`. Example: `pressed_image="images/W_pressed.png"`. `pressed_image` is the image that appears when `key` is pressed. `pressed_image` needs to be the exact same size as `not_pressed_image`. The file path can be relative or absolute, but note that if using absolute file paths on windows, you need to use double backslashes. For example, this is proper file path: "C:\\\Users\\\User\\\Pictures\\\picture.png"
    4. `not_pressed_image`. Example: `not_pressed_image="images/W_not_pressed.png"`. `not_pressed_image` is the image that appears when `key` is not pressed. `not_pressed_image` needs to be the exact same size as `pressed_image`. `not_pressed_image` is not a required parameter and can be omitted.
    5. Example usage: `add_image(key="W", pos=(801, 792), pressed_image="images/W_pressed.png", not_pressed_image="images/W_not_pressed.png")`
    6. Note that the included images folder only includes a limited set of images, just the ones that I use in `r0hkx_layout.py` (and for Minecraft overlays, they are particular to GUI scale 3 at 1080p).
12. You can add a rectangle without an image file very similarly to adding an image by using `add_rectangle()`, with the following differences:
    1. Replace `pressed_image` and `not_pressed_image` with `pressed_color` and `not_pressed_color`. Example: `pressed_color=(255, 255, 255, 100)`. `pressed_color` and `not_pressed_color` are the colors when `key` is pressed and not pressed, respectively. The four numbers are red, green, blue, and alpha (transparency), and each range from 0 to 255. `not_pressed_color` can be omitted. To find a color, google "color picker".
    2. Include `size` Example: `size=(48, 48)`. `size` is the width and height of the rectangle. There need to be exactly two numbers, separated by a comma, all within parentheses.
    3. Example usage: `add_rectangle(key="1", pos=(696, 1023), size=(48, 48), pressed_color=(255, 255, 255, 100), not_pressed_color=(50, 0, 50, 100))`
13. Once you have finished making your layout, run the file containing your layout with python. Your layout file MUST be in the same folder as `generator.py` Two files, one called `overlay_image.png` and `overlay_config.json`, will be created. These two files will work with the input overlay plugin. For information on how to use or install the input overlay plugin, see it's [tutorial](https://www.youtube.com/watch?v=7DTVIh3w6U8)
