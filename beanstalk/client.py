# stdlib imports
import sys
import time
import select

# pybeanstalk imports
from beanstalk import serverconn
from beanstalk import job


class Client():

    def __init__(self, server, port):
        self.server = server
        self.port = port

        self.connection = serverconn.ServerConn(self.server, self.port)
        self.connection.job = job.Job

    def producer_main(self):
        i = 0
        while True:
            data = 'This is data to be consumed (%s)!' % (i,)
            print data
            data = job.Job(data=data, conn=self.connection)
            data.Queue()
            time.sleep(1)
            i += 1

    def consumer_main(self):
        while True:
            j = self.connection.reserve()
            print 'got job! job is: %s' % j.data
            j.Finish()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Wrong usage"
        print "usage: example.py TYPE server [port]"
        print " TYPE is one of: [producer|consumer]"
    try:
        client_type = sys.argv[1]
        server = sys.argv[2]
        try:
            port = sys.argv[3]
        except:
            port = 11300

        client = Client(server, port)

    except Exception, e:
        print e
        sys.exit(1)

    if client_type == 'consumer':
        client.consumer_main()
    elif client_type == 'producer':
        client.producer_main()
    else:
        print "Wrong Type"
        sys.exit(1)
