import os
import pyautogui as auto


def module_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_resource(file):
    if os.path.isdir(os.path.join(module_path(), "res")):
        return os.path.join(module_path(), "res", file)
    else:
        return os.path.join("res", file)


def locate_on_screen(image, minSearchTime=1):
    if not os.path.isfile(image):
        image = get_resource(image)
    print("LOCATING: %s" % image)
    res = auto.locateCenterOnScreen(image, minSearchTime=minSearchTime)
    print("Found: " + str(res))
    return res
