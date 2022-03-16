# An included library with Python install.   
# importing the module
import screen_brightness_control as sbc
import pymsgbox
response = int(pymsgbox.prompt("Brightness level"))


sbc.fade_brightness(response, increment = 5)
print(sbc.get_brightness())

