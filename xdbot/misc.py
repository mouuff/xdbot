import os
import pyautogui as auto


def module_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_resource(file):
    return os.path.join(module_path(), "res", file)


def locate_on_screen(image):
    if not os.path.isfile(image):
        image = get_resource(image)
    print("LOCATING: %s" % image)
    res = auto.locateCenterOnScreen(image, minSearchTime=0)
    print("Found: " + str(res))
    return res
