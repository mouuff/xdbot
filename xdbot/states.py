from abc import ABC, abstractmethod
import pyautogui as auto
from . import misc


class WatcherBase:
    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def update(self):
        pass


class WatcherFindClickBase(WatcherBase):

    @abstractmethod
    def _get_image_to_find(self):
        pass

    def update(self):
        pos = auto.locateCenterOnScreen(self._get_image_to_find(), minSearchTime=500)
        if pos is not None:
            x, y = pos
            auto.click(x, y)


class WatcherFindAccept(WatcherFindClickBase):

    def _get_image_to_find(self):
        return misc.get_resource("accepter.png")

