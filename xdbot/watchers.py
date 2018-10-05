from abc import ABC, abstractmethod
import pyautogui as auto
from . import misc


class WatcherBase:
    def __init__(self, manager):
        self.manager = manager

    @abstractmethod
    def update(self):
        pass


class WatcherFindAndClickBase(WatcherBase):

    @abstractmethod
    def _get_image_to_find(self):
        pass

    def update(self):
        pos = auto.locateCenterOnScreen(self._get_image_to_find(), minSearchTime=100)
        if pos is not None:
            x, y = pos
            auto.click(x, y)


class WatcherFindAndAccept(WatcherFindAndClickBase):

    def _get_image_to_find(self):
        return misc.get_resource("accepter.png")
