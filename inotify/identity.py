import pyinotify

class Identity(pyinotify.ProcessEvent):
    def process_default(self, event):
        # Does nothing, just to demonstrate how stuffs could trivially
        # be accomplished after having processed statistics.
        print 'Does nothing.'

    def process_IN_CREATE(self, event):
        print "CREATE %s/%s" % (event.path, event.name)

    def process_IN_DELETE(self, event):
        print "DELETE %s/%s" % (event.path, event.name)

    def process_IN_ACCESS(self, event):
        print "ACCESS %s/%s" % (event.path, event.name)

    def process_IN_ATTRIB(self, event):
        print "IN_ATTRIB"

    def process_IN_CLOSE_NOWRITE(self, event):
        print "IN_CLOSE_NOWRITE"

    def process_IN_CLOSE_WRITE(self, event):
        print "IN_CLOSE_WRITE"

    def process_IN_DELETE_SELF(self, event):
        print "IN_DELETE_SELF"

    def process_IN_DONT_FOLLOW(self, event):
        print "IN_DONW_FOLLOW"

    def process_IN_IGNORED(self, event):
        print "IN_IGNORED"

    def process_IN_ISDIR(self, event):
        print "IN_ISDIR"

    def process_IN_MASK_ADD(self, event):
        print "IN_MASK_ADD"

    def process_IN_MODIFY(self, event):
        print "IN_MODIFY %s" % (os.path.join(event.path, event.name))

    def process_IN_MOVE_SELF(self, event):
        print "IN_MODE_SELF"

    def process_IN_MOVED_FROM(self, event):
        print "IN_MOVED_FROM"

    def process_IN_MOVED_TO(self, event):
        print "IN_MOVED_TO"

    def process_IN_ONLYDIR(self, event):
        print "IN_ONLY_DIR"

    def process_IN_OPEN(self, event):
        print "IN_OPEN"

    def process_IN_Q_OVERFLOW(self, event):
        print "IN_Q_OVERFLOW"

    def process_IN_UNMOUNT(self, event):
        print "IN_ONMOUNT"
