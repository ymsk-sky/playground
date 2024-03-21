# Bluetooth接続なら以下を記述
# import os
# os.environ['SDL_JOYSTICK_HIDAPI_PS4_RUMBLE'] = '1'

import time
import pygame

pygame.joystick.init()
if pygame.joystick.get_count() < 1:
    print("No controllers")
    exit()
joystick = pygame.joystick.Joystick(0)
joystick.init()

joystick.rumble(1.0, 1.0, 0)
time.sleep(10)
