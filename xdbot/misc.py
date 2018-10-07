import os
import pyautogui as auto


def module_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_resource(file):
    if os.path.isdir(os.path.join(module_path(), "res")):
        return os.path.join(module_path(), "res", file)
    else:
        return os.path.join("res", file)


def locate_on_screen(image, minSearchTime=2):
    if not os.path.isfile(image):
        image = get_resource(image)
    print("LOCATING: %s" % image)
    try:
        res = auto.locateCenterOnScreen(image, minSearchTime=minSearchTime)
    except OSError as e:
        res = None
    if res is not None:
        print("Found: " + str(res))
    return res
