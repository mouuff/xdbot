import os
import pyautogui as auto


def module_path():
    return os.path.dirname(os.path.realpath(__file__))


def get_lang():
    # TODO depend on config
    return "en"


def get_resource(file):
    res_path = os.path.join(module_path(), "res", get_lang())
    if os.path.isdir(res_path):
        return os.path.join(res_path, file)
    else:
        return os.path.join("res", get_lang(), file)


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
