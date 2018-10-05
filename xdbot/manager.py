import time
from .watchers import WatcherFindAndAccept, WatcherBanChampion


class Manager:
    def __init__(self, interval=0.1):
        self._running = False
        self._interval = interval
        self._watchers = [
            WatcherFindAndAccept(self),
            WatcherBanChampion(self),
        ]

    def mainloop(self):
        assert not self._running
        self._running = True
        while self._running:
            for watcher in self._watchers:
                watcher.update()
            time.sleep(self._interval)
