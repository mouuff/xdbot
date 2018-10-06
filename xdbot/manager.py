import time
from .watchers import WatcherFindAndAccept, WatcherBanChampion, WatcherLockBanChampion


class Manager:
    def __init__(self, interval=0.05):
        self._running = False
        self._interval = interval
        watcher_args = (self, interval)
        self._watchers = [
            WatcherFindAndAccept(self, interval=1),
            # WatcherBanChampion(*watcher_args),
            # WatcherLockBanChampion(*watcher_args),
        ]

    def mainloop(self):
        for watcher in self._watchers:
            watcher.start()
        input()  # thread are running, press to exit
