import time
from .watchers import WatcherFindAndAccept, WatcherFindCrossAndClose


class Manager:
    def __init__(self, interval=0.05):
        self._running = False
        self._interval = interval
        self._watchers = [
            WatcherFindAndAccept(self, interval=2),
            WatcherFindCrossAndClose(self, interval=2),
        ]

    def mainloop(self):
        for watcher in self._watchers:
            watcher.start()
        input()  # thread are running, press to exit
