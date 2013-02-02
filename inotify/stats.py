import pyinotify
import os
from pyinotify import EventsCodes
from identity import Identity


def on_loop(notifier):
    # notifier.proc_fun() is Identity's instance
    s_inst = notifier.proc_fun().nested_pevent()
    # print repr(s_inst), '\n', s_inst, '\n'


# Watch Manager
wm = pyinotify.WatchManager()

# generate event
s = pyinotify.Stats()

# Actions will be watched
mask = pyinotify.IN_MODIFY | pyinotify.IN_DELETE

# Notifier
notifier = pyinotify.Notifier(wm, default_proc_fun=Identity(s), read_freq=5)

# Set directory/file
wm.add_watch('/tmp', mask, rec=True, auto_add=True)

# Notifier loop
notifier.loop(callback=on_loop)
