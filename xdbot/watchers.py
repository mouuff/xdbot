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
    def _get_res_to_find(self):
        pass

    def click(self, x, y):
        auto.click(x, y)

    def update(self):
        pos = misc.locate_on_screen(self._get_res_to_find())
        if pos is not None:
            x, y = pos
            self.click(x, y)


class WatcherBanChampion(WatcherFindAndClickBase):
    def _get_res_to_find(self):
        return misc.get_resource("test.png")

    def click(self, x, y):
        print("found")
        ban = misc.locate_on_screen("bannissez.png")
        if ban is not None:
            super().click(x, y)
            auto.typewrite("morgana")


class WatcherFindAndAccept(WatcherFindAndClickBase):
    def _get_res_to_find(self):
        return "accepter.png"
