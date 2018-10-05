import time
from .watchers import WatcherFindAndAccept


class Manager:
    def __init__(self, interval=500):
        self._running = False
        self._interval = interval
        self._watchers = [
            WatcherFindAndAccept(self)
        ]

    def mainloop(self):
        assert not self._running
        self._running = True
        while self._running:
            for watcher in self._watchers:
                watcher.update()
            time.sleep(self._interval)
