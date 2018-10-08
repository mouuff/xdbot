from abc import ABC, abstractmethod
import time
import pyautogui as auto
import threading
from . import misc
from .constants import Constants


class WatcherBase(ABC):
    def __init__(self, manager, interval):
        self.manager = manager
        self._running = False
        self._interval = interval
        self._thread = threading.Thread(target=self._mainloop)
        self._thread.daemon = True

    def _mainloop(self):
        self._running = True
        while self._running:
            self._update()
            time.sleep(self._interval)

    @abstractmethod
    def _update(self):
        pass

    def start(self):
        self._thread.start()


class WatcherFindAndClickBase(WatcherBase):

    @abstractmethod
    def _get_res_to_find(self):
        pass

    def _found_res(self, x, y):
        auto.click(x, y)

    def _update(self):
        pos = misc.locate_on_screen(self._get_res_to_find())
        if pos is not None:
            x, y = pos
            self._found_res(x, y)


class WatcherLockBanChampion(WatcherFindAndClickBase):
    def _get_res_to_find(self):
        return Constants.RES_LOCK_BAN


class WatcherFindAndAccept(WatcherFindAndClickBase):
    def _get_res_to_find(self):
        return Constants.RES_ACCEPT_GAME


class WatcherFindCrossAndClose(WatcherFindAndClickBase):
    def _get_res_to_find(self):
        return Constants.RES_CROSS


class WatcherBanChampion(WatcherFindAndClickBase):
    def _get_res_to_find(self):
        return Constants.RES_FIND_BAN

    def _found_res(self, x, y):
        # ban = misc.locate_on_screen(Constants.RES_TITLE_BAN)
        # if ban is not None:
        super()._found_res(x, y)  # click on find ban bar
        auto.typewrite("morgana")  # test wip
