import pyinotify
import os
from pyinotify import EventsCodes
from identity import Identity


class MyInotifyWatch():

    def __init__(self):
        # Watch Manager
        wm = pyinotify.WatchManager()

        # generate event
        s = pyinotify.Stats()

        # Actions will be watched
        # mask = pyinotify.IN_MODIFY | pyinotify.IN_DELETE
        mask = pyinotify.ALL_EVENTS

        # Notifier
        self.notifier = pyinotify.Notifier(wm,
                                           default_proc_fun=Identity(s),
                                           read_freq=5)

        # Set directory/file
        wm.add_watch('/tmp', mask, rec=True, auto_add=True)

        # Notifier loop
        self.notifier.loop(callback=self.on_loop)

    def on_loop(self, notifier):
        # notifier.proc_fun() is Identity's instance
        s_inst = self.notifier.proc_fun().nested_pevent()
        # print repr(s_inst), '\n', s_inst, '\n'


if __name__ == '__main__':
    my_inotify = MyInotifyWatch()
